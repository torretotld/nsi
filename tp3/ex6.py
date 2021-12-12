#module
import os
from random import randint
import csv

#variable
question={}
i=int(0)
point=int(0)
limit_question=len(question)
nom=str(input("Quelle est votre nom ? : "))
prenom=str(input("Quelle est votre prenom ? : "))

#fonction
def random_nombre():
    final=list()
    global limit_question
    for i in range(5):
        nmbr=randint(1,limit_question)
        while nmbr in final:
            nmbr=randint(1,limit_question)
        final.append(nmbr)
    return(final)


#code
os.chdir('C:/Users/torre/Desktop/nsi/nsi/tp3')
file=open('question.csv','r')
line=csv.reader(file, delimiter=';')
for ligne in line:
    question[i]=ligne
    i+=1
limit_question=5
file2=open('nom_utilisateur_resultat.txt','w')
file2.write('Nom : ')
file2.write(nom)
file2.write('\n')
file2.write('Prenom : ')
file2.write(prenom)
file2.write('\n')
id_question=random_nombre()
for f in range(5):
    i=id_question[f]
    print(question[i][0])
    print('1 : ',question[i][1])
    print('2 : ',question[i][2])
    print('3 : ',question[i][3])
    print('4 : ',question[i][4])
    rep=str(input())
    while rep!='1' and rep!='2' and rep!='3' and rep!='4' and rep!="":
        print("Merci d'entrez une réponse valide")
        rep=str(input())
    if rep==question[i][5]:
        rep=int(rep)
        print("Bonne réponse")
        point+=2
        file2.write(question[i][0])
        file2.write(' : ')
        file2.write(question[i][rep])
        file2.write('\n')
    elif rep=="":
        print("la bonne réponse était la ",question[i][5])
        file2.write(question[i][0])
        file2.write(' : Aucune')
        file2.write('\n')
    else:
        point-=1
        rep=int(rep)
        print("Mauvaise réponse, la bonne était la ",question[i][5])
        file2.write(question[i][0])
        file2.write(' : ')
        file2.write(question[i][rep])
        file2.write('\n')
point=str(point)    
file2.write('Score final : ')
file2.write(point)
file2.write('\n')
file2.close()