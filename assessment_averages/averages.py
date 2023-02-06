from pydoc_data.topics import topics
import pandas as pd

# To clean up unorganized data
import math

# Set configuration variables

# column of 30+ NSs
NS_COLUMN = 'What is the name of the supported National Society?'

# columns of 10+ themes
THEMES_COLUMN = 'Themes'

# column of names of participants
CONTACT_PERSON = 'What is the name of the interview participant?'

# Output name is the output file name
OUTPUT_NAME = "output_fileName.xlsx"

# Questions numbers to filter rating 1-10 answers
QUESTION_NUMBERS = [
    5,
    6,
    9,
    24,
    25,
    26,
    27,
    28,
    29,
    32,
    33,
    34,
    37,
    38,
    41,
    42,
    43,
    44,
    45,
    48,
    49,
    50,
    54,
    55,
    62
    ]

# Reading the impact-assessment table
def readData():
    xl = pd.ExcelFile("impact-assesment.xlsx")
    df = xl.parse("substantiveData")
    return df

# Filter out double themes in the column and filter out everything that is not a string
def getUniqueThemes(df):
    themesCol = df[THEMES_COLUMN].tolist()
    myset = set(themesCol)
    themesList = list(myset)
    filteredThemes = []
    for theme in themesList:
        if isinstance(theme, str):
            filteredThemes.append(theme)
    return filteredThemes

# Get averages per unique theme - sum of ratings / number of answers, returns the average and the number of answers on which it is based
def getThemeAverageOfQuestion(df, question, themeName):
    count = 0
    sumRatings = 0

    filteredDf = df.loc[df[THEMES_COLUMN] == themeName]
    uniqueNs = []
    for index, row in filteredDf.iterrows(): #--"index" is not accessedPylance--
        if row[NS_COLUMN] not in uniqueNs and type(row[question]) != str and not math.isnan(row[question]):
            uniqueNs.append(row[NS_COLUMN])
            count = count + 1
            sumRatings = sumRatings + row[question]           

    if count == 0:
        return '', 0
    else:
        themeAverage = sumRatings / count 
        return themeAverage, count

# Get averages per question where the answer is a number - sum of answers / number of answers, returns the average and the number of answers on which it is based (count)
def getAverageOfQuestion(df, question):
    count = 0
    sumGrade = 0
    lastNs = ''
    last_contact_p = ''
    for index, row in df.iterrows():
        if type(row[question]) != str and not math.isnan(row[question]):
            if lastNs != row[NS_COLUMN] or last_contact_p != row[CONTACT_PERSON]:
                last_contact_p = row[CONTACT_PERSON]
                lastNs = row[NS_COLUMN]
                count = count + 1
                sumGrade = sumGrade + row[question]

    if count == 0:
        return '', 0
    else:
        questionAverage = sumGrade / count
        return questionAverage, count

# Returns the questions with rating 1-10 answers only
def getRatingQuestions(df):
    ratingQuestions = []
    allQuestions = list(df.columns.values)
    for n in QUESTION_NUMBERS:
        for question in allQuestions:
            start = str(n) + ' '
            if type(question) is str and question.startswith(start):
                ratingQuestions.append(question)
    return ratingQuestions

def createOutputDf(uniqueThemes, inDf):
    # Creates list rating questions (1-10) questions
    themeAveragesAllQuestions = []

    questions = getRatingQuestions(inDf)
    print('questions: ', questions)

    # Creates theme averages and overall average per rating (1-10) question
    for question in questions:
        themeAverages = getAllThemeAverageForQuestion(
            question, uniqueThemes,  inDf)
        themeAveragesAllQuestions.append(themeAverages)

    df = pd.DataFrame(themeAveragesAllQuestions)
    print('df: ', df)
    df.to_excel(OUTPUT_NAME)

# Creates object with the following columns with calculated rows: 'question', 'Average: All', 'Count:All', Average per unique theme, Count per Unique theme
def getAllThemeAverageForQuestion(question, uniqueThemes, inDf):
    themeAverages = {'question': question}

    av, count = getAverageOfQuestion(inDf, question)
    themeAverages['Average: All '] = av
    themeAverages['Count: All'] = count
    for theme in uniqueThemes:
        av, count =  getThemeAverageOfQuestion(inDf, question, theme)
        themeAverages['Average: ' + theme] = av
        themeAverages['Count: ' + theme] = count
    return themeAverages

if __name__ == '__main__':
    inDf = readData()
    uniqueThemes = getUniqueThemes(inDf)
    createOutputDf(uniqueThemes, inDf)




