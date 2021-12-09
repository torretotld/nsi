from random import randint

compteur = 0
nbr_rep_cor = 0
nbr_rep_incor = 0

def random_binaire():
    d=int()
    final=list()
    final2=list()
    e=int()
    for i in range(8):
        d=randint(0,1)
        final.append(d)
    for i in range(8):
        e=randint(0,1)
        final2.append(d)
    return(final,final2)

def DeuxEnDix(a):
    final=int()
    a.reverse()
    for i in range(len(a)):
        a[i] = int(a[i])
    for i in range(len(a)):
        final=final+(a[i]*(2**i))
    final=str(final)
    return(final)

def random_decimal():
    final=int()
    final=randint(0,1000)
    final2=int()
    final2=randint(0,1000)
    return(final,final2)

def DixEnDeux(c):
    liste=list()
    while c>0:
        liste.append(c%2)
        c=c//2

    liste.reverse()
    nombre = str(liste[0])

    for i in range(1, len(liste)):
        nombre += str(liste[i])

    return(nombre)

def random_hexadecimal():
    d=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    final=list()
    final2=list()
    for i in range(4):
        e=int()
        e=randint(0,15)
        final.append(d[e])
    for i in range(4):
        e=int()
        e=randint(0,15)
        final2.append(d[e])
    return(final,final2)

def SeizeEnDix(d):
    final=int()
    liste=list()
    f=len(d)
    d.reverse()

    for i in range(f):

        if d[i] == 'A':
            d[i] = 10
        elif d[i] == 'B':
            d[i] = 11
        elif d[i] == 'C':
            d[i] = 12
        elif d[i] == 'D':
            d[i] = 13
        elif d[i] == 'E':
            d[i] = 14
        elif d[i] == 'F':
            d[i] = 15
        d[i] = int(d[i])

    for i in range(f):
        final=final+(d[i]*(16**i))
    final=str(final)
    return(final)



f=list()
a=int(input("Combien de question voulez vous ? "))
c=int(a/2)
for i in range(c):
    base=['2','10','16']
    d=randint(0,2)
    e=base[d]
    if e == '2':
        print('Base 2 en 10 :')
        f=random_binaire()
        print(f[0])
        reponse=str(input())
        rep=DeuxEnDix(f[0])
        if rep==reponse:
            print("Bonne réponse")
            compteur+=2
            nbr_rep_cor+=1
        else:
            print("Mauvaise Reponse")
            compteur=compteur-1
            nbr_rep_incor+=1
            print(rep)
        print(f[1])
        reponse=str(input())
        rep=DeuxEnDix(f[1])
        if rep==reponse:
            print("Bonne réponse")
            compteur+=2
            nbr_rep_cor+=1
        else:
            print("Mauvaise Reponse")
            compteur=compteur-1
            nbr_rep_incor+=1
            print(rep)
    elif e == '10' :
        print('Base 10 en 2 :')
        f=random_decimal()
        print(f[0])
        reponse=str(input())
        rep=DixEnDeux(f[0])
        if rep==reponse:
            print("Bonne réponse")
            compteur+=2
            nbr_rep_cor+=1
        else:
            print("Mauvaise Reponse")
            compteur=compteur-1
            nbr_rep_incor+=1
            print(rep)
        print(f[1])
        reponse=str(input())
        rep=DixEnDeux(f[1])
        if rep==reponse:
            print("Bonne réponse")
            compteur+=2
            nbr_rep_cor+=1
        else:
            print("Mauvaise Reponse")
            compteur=compteur-1
            nbr_rep_incor+=1
            print(rep)
    else :
        print('Base 16 en 10')
        f=random_hexadecimal()
        print(f[0])
        reponse=str(input())
        rep=SeizeEnDix(f[0])
        if rep==reponse:
            print("Bonne réponse")
            compteur+=2
            nbr_rep_cor+=1
        else:
            print("Mauvaise Reponse")
            compteur=compteur-1
            nbr_rep_incor+=1
            print(rep)
        print(f[1])
        reponse=str(input())
        rep=SeizeEnDix(f[1])
        if rep==reponse:
            print("Bonne réponse")
            compteur+=2
            nbr_rep_cor+=1
        else:
            print("Mauvaise Reponse")
            compteur=compteur-1
            nbr_rep_incor+=1
            print(rep)

print('Vous avez eu : ',compteur,'points sur ',a,' questions')
print('Vous avez eu',nbr_rep_cor,'réponses correcte et',nbr_rep_incor,'incorrectes')

