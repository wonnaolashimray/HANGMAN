import random
# from words import list1
print("You are in  Hangman World")
def my():
    list1=["cat","elephant","tiger","crocodile","parrot","butterfly","bear","monkey"]
    word=random.choice(list1)
    guessed_letter=6
    used_letter=''
    v=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        word_var=""
        for letter in word:
            if letter in used_letter:
                word_var=word_var+letter
            else:
                word_var=word_var+"_ "
        if word_var==word:
            print(word_var)
            print("Wow! you win the game 🥳")
            break
        print("guess the word",word_var,)
        guess=input("enter the letter...")
        if guess in v:
            used_letter+=guess
        else:
            print("enter valid character")
            guess=input()
        if guess not in word:
            if guessed_letter==6:
                print("  __")
                print("       |")
                print("       |")
                print("       |")
                print(" =======")
            if guessed_letter==5:
                print("o___")
                print("     |")
                print("     |")
                print(" =====")
            if guessed_letter ==4:
                print(" o__")
                print(" |   |")
                print("     |")
                print(" =====")
            if guessed_letter ==3:
                print("3 time is left ")
                print(" o___")
                print("/|    |")
                print("      |")
                print(" ======")
            if guessed_letter ==2:
                print("2 time is left choose right")
                print(" o___")
                print("/|\   |")
                print("      |")
                print(" =======")
            if guessed_letter ==1:
                print("only one trun is left):!!")
                print(" o___")
                print("/|\   |")
                print("/     |")
                print(" =======")
            if guessed_letter ==0:
                print("ooppssss sorry you loss")
                print(" o___")
                print("/|\    |")
                print("/ \    |")
                print(" =======")
                break
            guessed_letter=guessed_letter-1
name=input("enter your name__:")
print("WELCOME To Hangman Game ",name)
my()

                                                                                                                                                                                                                                                                                                                         