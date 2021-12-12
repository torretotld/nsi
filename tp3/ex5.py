#module
import os
from random import randint

#variable
mot2=str()
mothide=str()
lettre=list()
chance=3

#code
os.chdir('C:/Users/torre/Desktop/nsi/nsi/tp3')
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
for i in range(len(mot2)):
    if mot2[i] in lettre:
        mothide+=mot[i]
    else:
        mothide+='*'
print(mothide)
while chance>0:
    print("Entrez le mot qui correspond, il vous reste",chance,"chances")
    rep=str(input())
    if rep==mot2:
        print("Bien jouez, vous avez trouver le mot")
        chance=0
    else:
        chance-=1
        if chance==0:
            print("Perdu, le mot était : ",mot2)
