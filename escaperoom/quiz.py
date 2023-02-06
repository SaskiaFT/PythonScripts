# Dit is een quiz

# pip install pygame
# pip install pygame

#from mutagen.mp3 import MP3 - De soundfiles ontbreken bij deze versie van de escaperoom, alle audio is in deze versie gecommend
import time
from question import Question
import os.path

#import playsound - De soundfiles ontbreken bij deze versie van de escaperoom
TEST = False

#Part I INTRODUCTION

def do_intro():
    if not TEST:
        time.sleep(3)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print("Hi children of the Earth and the Tovergieter! So glad you game to join us in the Trollenberg. We have been quarantining here all alone for ages.")
    #play_audio('1-1-intro')
    time.sleep(4)

    print("I hope you guys like escape rooms. You can now take your blindfolds off.")
    #play_audio('1-2-blindfold')
    time.sleep(4)

    print("Please do not close the current window on this laptop, do not cheat, and do not break stuff in the master bedroom.")
    #play_audio('1-4-no-cheats')
    time.sleep(4)

    print("What are your names? Please enter them and press enter.")
    #play_audio('1-3-names')

    Names = input()
    print( "Nice to meet you " + Names + ", I think it would be fun to play a game. Are you up for it? Please enter 'yes' and press enter.")
    #play_audio('1-7-meet')
    Answer = input()
    if Answer == 'yes':
        print( 'Oke, let us commence.')
        #play_audio('1-5-commence')\
        time.sleep(2)
    else:
        print( 'Let us play anyway!')
        #play_audio('1-6-anyway')
        time.sleep(2)

#Part II QUIZ

#runs to all of the multiple choice questions one by one and takes lower case chars as input
def run_quiz(questionObjects):
    score = 0
    for questionObject in questionObjects: #--Loop syntax?--
        #if os.path.isfile(question.mp3 + '.mp3'): 
            #play_audio(question.mp3)\
        answer = input(questionObject.prompt + 'Enter the letter of your answer than press enter.\n\n')
        
        #converts answer to lower case if uppercase
        if answer.lower() == questionObject.answer: 
            score += 1

    #Prints how many answers are correct out of the total amount of questions, if not all answers are correct, the quiz is run again
    time.sleep(2)
    print('\nYou have got ' + str(score) + ' out of ' + str(len(questionObjects)) + ' correct.\n')
    if score < len(questionObjects):
        #play_audio('2-0-incorrect')
        time.sleep(2)
        print('You need to get all the questions correct. How well do you know us anyway? Try again.') 
        time.sleep(2)
        run_quiz(questionObjects)
    else: 
        time.sleep(2)
        print("Nicely done!\n")
        time.sleep(1)
        print("Now the light in the room should turn on!\n")
        time.sleep(2)
        #play_audio('3-1-bergen')')

questionObjects = [
    Question("\nWhat color are Rubens eyes?\n\n(a) Brown/Green\n(b) Green/Blue\n(c) Blue/Gray\n\n", 'c', '2-1-quiz'),
    Question("\nWhat is Saskia's secret talent?\n\n(a) Touching hip with feet\n(b) Licking elbow with tongue\n(c) A splits\n\n", 'a' , '2-2-quiz'),
    Question("\nWhat sport did Ruben practice as a child?\n\n(a) Volleyball\n(b) Gymnastics\n(c) Ballet\n\n", 'b', '2-3-quiz'),
    Question("\nWhat was the name of Wiepke's club when she was young?\n\n(a) The coole Wiepke club\n(b) Wiepke is awsomeness\n(c) Conquer and divide, Wiepke Style\n\n", 'a', '2-4-quiz'),
    Question("\nWhat is the name of the cat?\n\n(a) Leo\n(b) Leeuw\n(c) Jochie\n\n", 'a', '2-5-quiz'),
    Question("\nWhere has Rico been searched?\n\n(a) His armpit\n(b) His shoe\n(c) His a'hole\n\n", 'c', '2-6-quiz'),
    Question("\nWhy has Freek pucked red once?\n\n(a) Too much red wine\n(b) Beetroot juice\n(c) Hit in the stomach\n\n", 'b', '2-7-quiz'),
    Question("\nWhat did Freek say to Rikke?\n\n(a) Let's go banana's\n(b) Let's go avocado's\n(c) Let's go tomato's\n\n", 'a', '2-8-quiz'),
]

#Part III RAADSEL SERIE

#Quiz that gives output for player to search in one of the books in the escaperoom and takes input
def raadselSerie():
    print("Now a riddle for you all...\n\n\n")
    time.sleep(2)
    riddle()
    zoekBoek('HP4 - page 154 word 1', 'slytherins')
    zoekBoek('Use the melody - page 60 word 1', 'god', '4-1-got') 
    time.sleep(2)
    print("\nThe first number is 5\nHave fun searching!")

    #play_audio('4-2-champ')

#Quiz gives output accepts input in lower case, if correct run the rest of the program, if incorrect output wrong answer and runs 'raadsel' quiz again    
def riddle():
    #play_audio('3-2-raadsel')
    print('I am light as a feather, and can keep it aloft\nMost of the time I am silent and soft\nI am with you always, in whispers and song\nThe strongest of men cannot hold me for long')
    time.sleep(2)
    answer = input('\n\n\nType in your answer to the riddle and press enter:\n\n')
    if 'breath' in answer.lower():
        pass
    else:
        print('\nWrong answer')
        riddle()

#Checks if answers given in the zoekBoek quiz are correct
def zoekBoek(text, correctAnswer, audio=None):
    #if audio is not None:
        #play_audio(audio)
    print('\n')
    userInput = input(text + '\n\nPlease enter the correct word and press enter\n')
    print('\n')
    if correctAnswer in userInput.lower(): #--Why lower?--
        print('\nCorrect\n')
        pass
    else: 
        print('\nIncorrect\n')
        zoekBoek(text, correctAnswer)

#def play_audio(mp3):
    #playsound.playsound(mp3 + '.mp3')
    #audio = MP3(mp3 + '.mp3')


do_intro()
run_quiz(questionObjects)
raadselSerie()

time.sleep(3)






    
