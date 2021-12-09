# Fonction
def VerifFormat(a,b):
    Error=False
    if len(a)!=len(b):
        Error=True
    else:
        if len(a)==5:
            if a[2]!='-':
                Error=True
            elif b[2]!='-':
                Error=True
            if '-' in a:
                a.remove('-')
            else:
                Error=True
            if '-' in b:
                b.remove('-')
            else:
                Error=True
            for i in range(len(a)):
                if a[i]!='0' and a[i]!='1' and a[i]!='2' and a[i]!='3' and a[i]!='4' and a[i]!='5' and a[i]!='6' and a[i]!='7' and a[i]!='8' and a[i]!='9':
                    Error=True
                if b[i]!='0' and b[i]!='1' and b[i]!='2' and b[i]!='3' and b[i]!='4' and b[i]!='5' and b[i]!='6' and b[i]!='7' and b[i]!='8' and b[i]!='9':
                    Error=True
        elif len(a)==10:
            if a[2]!='-' or a[5]!='-':
                Error=True
            elif b[2]!='-' or b[5]!='-':
                Error=True
            if '-' in a:
                a.remove('-')
                a.remove('-')
            else:
                Error=True
            if '-' in b:
                b.remove('-')
                b.remove('-')
            else:
                Error=True
            for i in range(len(a)):
                if a[i]!='0' and a[i]!='1' and a[i]!='2' and a[i]!='3' and a[i]!='4' and a[i]!='5' and a[i]!='6' and a[i]!='7' and a[i]!='8' and a[i]!='9':
                    Error=True
                if b[i]!='0' and b[i]!='1' and b[i]!='2' and b[i]!='3' and b[i]!='4' and b[i]!='5' and b[i]!='6' and b[i]!='7' and b[i]!='8' and b[i]!='9':
                    Error=True
        else:
            Error=True
    return(Error)

def VerifDate1(jour,mois):
    error=False
    if mois == 1 or mois == 3 or mois == 5 or mois ==  7 or mois == 8 or mois == 10 or mois == 12:
        if jour > 31 :
            error=True
    elif mois == 4 or mois == 6 or mois ==9 or mois ==11 :
        if jour > 30 :
            error=True
    elif mois == 2 :
        if jour > 29 :
            error=True
    else:
        error=True
    return(error)

def VerifDate2(jour,mois,annee):
    error=False
    if mois == 1 or mois == 3 or mois == 5 or mois ==  7 or mois == 8 or mois == 10 or mois == 12:
        if jour > 31 :
            error=True
    elif mois == 4 or mois == 6 or mois ==9 or mois ==11 :
        if jour > 30 :
            error=True
    elif mois == 2 :
        if jour > 29 :
            error=True
        elif jour==29 and annee%4!=0:
            error=True
    else:
        error=True
    return(error)

#variable
nmbr1=int()
nmbr2=int()
DayInMonth=['',31,28,31,30,31,30,31,31,30,31,30,31]
final=int()

#code
a=list(input("Quelle est la premiere date ? : "))
b=list(input("Quelle est la seconde date ? : "))
error=VerifFormat(a,b)
if error==True:
    print("Erreur : la date que vous avez entrez n'est pas au bon format, merci de l'entrer au format dd-mm ou dd-mm-yyyy")
else:
    a.reverse()
    b.reverse()
    for i in range(len(a)):
        if a[i]!='-':
            a[i]=int(a[i])
        if b[i]!='-':
            b[i]=int(b[i])
    if len(a)==4:
        mois1=int(a[0]+(a[1]*10))
        jour1=int(a[2]+(a[3]*10))
        mois2=int(b[0]+(b[1]*10))
        jour2=int(b[2]+(b[3]*10))
        error1=VerifDate1(jour1,mois1)
        error2=VerifDate1(jour2,mois2)
        if error1==False and error2==False:
            nmbr1+=jour1
            nmbr2+=jour2
            for i in range(1,mois1):
                nmbr1+=DayInMonth[i]
            for i in range(1,mois2):
                nmbr2+=DayInMonth[i]
            if nmbr1>nmbr2:
                final=nmbr1-nmbr2
            else:
                final=nmbr2-nmbr1
            print("Entre les 2 dates, il y a ",final," jours d'équart'")


    else:
        annee1=(a[0]*1)+(a[1]*10)+(a[2]*100)+(a[3]*1000)
        mois1=(a[4]*1)+(a[5]*10)
        jour1=(a[6]*1)+(a[7]*10)
        annee2=(b[0]*1)+(a[1]*10)+(b[2]*100)+(b[3]*1000)
        mois2=(b[4]*1)+(b[5]*10)
        jour2=(b[6]*1)+(b[7]*10)
        error1=VerifDate2(jour1,mois1,annee1)
        error2=VerifDate2(jour2,mois2,annee2)
        if error1==False and error2==False:
            nmbr1+=jour1
            nmbr2+=jour2
            for i in range(1,mois1):
                if i!=2:
                    nmbr1+=DayInMonth[i]
                else:
                    if annee1%4==0:
                        nmbr1+=29
                    else:
                        nmbr1+=28
            for i in range(1,mois2):
                if i!=2:
                    nmbr2+=DayInMonth[i]
                else:
                    if annee2%4==0:
                        nmbr2+=29
                    else:
                        nmbr2+=28
            for i in range(1,annee1):
                if i%4==0:
                    nmbr1+=366
                else:
                    nmbr1+=365
            for i in range(1,annee2):
                if i%4==0:
                    nmbr2+=366
                else:
                    nmbr2+=365
            if nmbr1>nmbr2:
                final=nmbr1-nmbr2
            else:
                final=nmbr2-nmbr1
            print("Entre les 2 dates, il y a ",final," jours d'équart'")
        else:
            print("La date donnée n'existe pas, merci de la vérifier")






