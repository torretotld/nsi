#module
import os
from random import randint

#variable
mot2=str()
mothide=list()
chance=3
chance_used=0
lettre=list()

#cde
os.chdir('C:/Users/torre/OneDrive/Bureau/travail/nsi/tp3')
file=open('mot.txt','r')
line=file.readlines()
nmbrmot=randint(0,len(line))
mot=str(line[nmbrmot])
for i in range(len(mot)-1):
    mot2+=str(mot[i])
lettre=list(input("Entrez 5 lettres : "))
while len(lettre)!=5:
    print("Merci d'entrez 5 lettres")
    lettre=list(input("Entrez 5 lettre : "))
for i in range(len(mot)):
    if mot[i] in lettre:
        mothide=