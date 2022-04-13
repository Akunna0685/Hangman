#create hangman word file
#f = open("hangman.txt", "x")
#call hang man file
Letters = True
f = open("Pretext", "r")
Pretext = (f.read())
print(Pretext)
f.close()

f = open("hangman.txt", "r")
hangmanword = (f.read())
f.close()
#Splice the word in the file
Letterlist = list(hangmanword)
#puttint _ intsed of letters
from Hangman_Graphics import Hangmanpics
tries = len(Hangmanpics)
presentlist =[]
Wrong_Gessed_Letters = []
counter = 1



for l in Letterlist:
    presentlist.append("_")
# code to gusse the letters




def letterguesser():
    global Letterlist
    global Wrong_Gessed_Letters
    global life
    counter = 0
    x = 0
    guess = input("Please Guess: ")  # Imput letters
    for l in Letterlist:
        if guess == l:
            presentlist.pop(counter)
            presentlist.insert(counter,guess)
            counter = counter + 1
            x = 1

        else:
            counter = counter + 1

    if x == 0:
        Wrong_Gessed_Letters.append(guess)
        life = life + 1
        Wrong_Gessed_Letters = list(dict.fromkeys(Wrong_Gessed_Letters)) #prevents doubles in the Wrong Gusse list
        #print("You already guessed this letter:( Please try again! :/")



life = 0
#running function above
while Letters == True:
    letterguesser()
    print(presentlist)
    print("These are wrongly guessed letters:", Wrong_Gessed_Letters)
    print(Hangmanpics[life])

    if life == 9:
        print("You DEAD!! }:-) LOL! You loser! Better Luck next time. ")
        exit()


    '_'.join(presentlist)   #turn word into list
    if Letterlist == presentlist:
        print("YAY!! YOU WON!! XD")
        exit()












