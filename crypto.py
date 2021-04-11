from tkinter import *
from tkinter.filedialog import askopenfilename

lettre = {
"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, 
"I" : 8, "J" : 9, "K" : 10, "L" : 11, "M" : 12, "N" : 13, "O" : 14,
"P" : 15, "Q" : 16, "R" : 17, "S" : 18, "T" : 19, "U" : 20,
"V" : 21, "W" : 22, "X" : 23, "Y" : 24, "Z" : 25
}   
lettre_reversed = {value : key for (key, value) in lettre.items()}

#selectionner un fichier
def selectFile():
    file = Tk().withdraw() 
    filename = askopenfilename() 
    return filename

# explit function to return the letter count
def letterFrequency(fileName, letter):
    # open file in read mode
    file = open(fileName, 'r')
  
    # store content of the file in a variable
    text = file.read()
  
    # using count()
    return text.count(letter) + text.count(letter.casefold())
  
# Program to get letter count in a text file
  
def letterstatic(file):
    lettretext ={}
    for c in lettre.keys() :
        lettretext[c] = letterFrequency(file,c)
    return lettretext

#fonction pour trouver le cle
def getkey(lettersta):
    max_let ={}
    max_key = max(lettersta.values())
    for c in lettersta.keys() :
        if lettersta[c] == max_key :
            max_let[c] = max_key
    cles =[]
    for c in max_let.keys() :
        cles.append(lettre[c] - lettre["E"])
    return cles


  
def decrypt(file):
    f = open(file, "r")
    texto = f.read()
    cles = getkey(letterstatic(file))
    for cle in cles :
        file_d = open('file_decrypte'+str(cle)+".txt", "w")
        text =""
        for c in texto :
            if ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')):
                g =(lettre[c.upper()]-cle)%25
                if(g<0):
                    g = g + 25
                if(not c.isupper()):
                    text += lettre_reversed[g].casefold()
                else :
                    text += lettre_reversed[g]
            else :
                text += str(c)
        file_d.write(text)
        file_d.close()


#A python program to illustrate Caesar Cipher Technique
def encrypt(text,cle):
    result = ""
 
    # traverse text
    for c in text :
        if ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')):
            g =lettre[c.upper()]+cle
            if(g>25):
                g = g -25
            if(not c.isupper()):
                result += lettre_reversed[g].casefold()
            else :
                result += lettre_reversed[g]
        else :
            result += str(c)
    file_d = open('file_crypte',"w")
    file_d.write(result)
    file_d.close()
 

#The main function for using this program
def maincrypto():
    choix = 1
    print("\n\n***************************************** Cryptographie ******************************************")
    print("\n\t0- Quitter le programe \n")
    print("\n\t1- crypter un fichier text \n")
    print("\n\t2- decrypter un fichier text \n")
    while(choix != 0):
        choix = int(input("Votre choix est :"))
        if(choix == 0) :
            exit()
        elif(choix == 1):
            #check the above function
            text = selectFile()
            text = open(text,"r")
            text = text.read()
            cle = -1
            while(cle == -1):
                cle = int(input("\n\t\t Entrer un cle entre (0-25) :"))
                if(cle < 0 or cle > 25) :
                    print("\n\t\t\t!!! Mauvais cle !!!")
                    cle = -1

            encrypt(text,cle)
        elif(choix == 2):
            decrypt(selectFile())
        
        else :
            print("!!! Erreur mauvais choix !!!")

maincrypto()

