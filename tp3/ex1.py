a=int(input("Quelle est votre base de départ : "))
b=int(input("Quelle est votre base d'arrivé : "))
reel=False
error=False

def VerifBaseDix(c):
    error=False
    point=False
    for i in range(len(c)):
        if c[i]!= '.' and c[i]!= '-' and c[i]!= '1' and c[i]!= '2' and c[i]!= '3' and c[i]!= '4' and c[i]!= '5' and c[i]!= '6' and c[i]!= '7' and c[i]!= '8' and c[i]!= '9' and c[i]!= '0' :
            error=True
        if(c[i])=='.':
            if point==False:
                point=True
            else:
                error=True
        if c[i]=='-' and i!=0:
            error=True
    return(error)

def DeuxEnDix(a):
    final=int()
    a.reverse()
    for i in range(len(a)):
        a[i] = int(a[i])
    for i in range(len(a)):
        final=final+(a[i]*(2**i))
    final=str(final)
    return(final)


def DixEnDeux(c):
    d=int()
    nombre=str()
    p=1
    d=int()
    c.reverse()
    for z in range(len(c)):
        c[z]=int(c[z])
        d=d+(c[z]*p)
        p*=10
    liste=list()
    while d>0:
        liste.append(d%2)
        d=d//2

    liste.reverse()

    for i in range(0, len(liste)):
        nombre += str(liste[i])
    return(nombre)


def DixEnDeuxVirgule(l):
    g=int()
    nmbr=int()
    nmbr2=int()
    final=str()
    listebinaire=list()
    e=0
    for i in range(len(l)) :
        if l[i]=="." or l[i]==",":
            h=i
    l.reverse()
    for i in range(len(l)) :
        if l[i]=="." or l[i]==",":
            g=i
    l.remove('.')
    for i in range(len(l)):
        l[i]=int(l[i])
    p=1
    for i in range(g,len(l)):
        nmbr+=l[i]*p
        p=p*10
    l.reverse()
    q=0.1
    for i in range(h,len(l)):
        nmbr2+=l[i]*q
        q=q*0.1
    while nmbr>1 :
        reste=nmbr%2
        nmbr=nmbr//2
        listebinaire.append(reste)
    listebinaire.append(nmbr)
    listebinaire.reverse()
    listebinaire.append('.')
    while nmbr2!=0 and e<6:
        nmbr2=nmbr2*2
        if nmbr2>=1:
            listebinaire.append(1)
            nmbr2=nmbr2-1
        else:
            listebinaire.append(0)
        e+=1
    for i in range(0, len(listebinaire)):
        final+= str(listebinaire[i])
    return(final)

def DixEnDeuxNegatif(c):
    c.remove('-')
    c.reverse()
    p=1
    d=int()
    for i in range(len(c)):
        c[i]=int(c[i])
        d=d+(c[i]*p)
        p=p*10
    if d> -127:
        bits=8
    elif d> -32768:
        bits=16
    elif d> -2147483648:
        bits=32
    else :
        print("Le chiffre n'est pas codable en 32 bit, le maximum supporté pour les nombres négatif")
        breakpoint
    liste=list()
    d=d-d-d
    d+=2**bits
    print(d)
    while d>0:
        liste.append(d%2)
        d=d//2
    liste.reverse()
    return(liste)

def VerifBaseDeux(c):
    error=False
    for i in range(len(c)):
        if c[i]!='0' and c[i]!='1' and c[i]!='.' :
            error=True
    return(error)

def DeuxEnDixVirgule(l):
    g=int()
    nmbr=int()
    nmbr2=int()
    final=int()
    listebinaire=list()
    listebinaire2=list()
    e=0
    l.reverse()
    for i in range(len(l)) :
        if l[i]=="." or l[i]==",":
            g=i
    l.remove('.')
    for i in range(g):
        listebinaire.append(l[i])
    for i in range(g,len(c)):
        listebinaire2.append(l[i])
    print(listebinaire2)
    print(listebinaire)
    listebinaire.reverse()
    for i in range(len(listebinaire)):
        listebinaire[i] = int(listebinaire[i])
    for i in range(len(listebinaire2)):
        listebinaire2[i] = int(listebinaire2[i])
    p=int(-1)
    for i in range(len(listebinaire)):
        final=final+(listebinaire[i]*(2**p))
        p=p-1
    z=1
    final2=int()
    for i in range(len(listebinaire2)):
        final2=final2+(listebinaire2[i]*(2**i))
        z=z*102
    print(final)
    print(final2)
    return(final+final2)



def DeuxEnSeize(d):
    final=int()
    nombre=str()
    d.reverse()
    for i in range(len(d)):
        d[i] = int(d[i])
    for i in range(len(d)):
            final=final+(d[i]*(2**i))
    liste=list()
    while final>0:
        d=final%16
        if d == 10:
            d = 'A'
        elif d == 11:
            d = 'B'
        elif d == 12:
            d = 'C'
        elif d == 13:
            d = 'D'
        elif d == 14:
            d = 'E'
        elif d == 15:
            d = 'F'
        liste.append(d)
        final=final//16
    liste.reverse()
    for i in range(0, len(liste)):
            nombre += str(liste[i])
    return(nombre)

def DixEnSeize(c):
    liste=list()
    nombre=str()
    while c>0:
        d=c%16
        if d == 10:
            d = 'A'
        elif d == 11:
            d = 'B'
        elif d == 12:
            d = 'C'
        elif d == 13:
            d = 'D'
        elif d == 14:
            d = 'E'
        elif d == 15:
            d = 'F'
        liste.append(d)
        c=c//16
    liste.reverse()
    for i in range(len(liste)):
            nombre += str(liste[i])
    return(nombre)

def VerifBaseSeize(c):
    error=False
    for i in range(len(c)):
        if c[i]=='0' and c[i]=='1' and c[i]=='2' and c[i]=='3' and c[i]=='4' and c[i]=='5' and c[i]=='6' and c[i]=='7' and c[i]=='8' and c[i]=='8' and c[i]=='A' and c[i]=='B' and c[i]=='C' and c[i]=='D' and c[i]=='E' and c[i]=='F':
            error=True
    return(error)

def SeizeEnDix(d):
    f=len(d)
    d.reverse()
    final=int()
    for i in range(f):

        if d[i] == 'A':
            d[i] = 10
        elif d[i] == 'B':
            d[i] = 11
        elif d[i] == 'C':
            d[i] = 12
        elif d[i] == 'D':
            d[i] = '13'
        elif d[i] == 'E':
            d[i] = 14
        elif d[i] == 'F':
            d[i] = 15
        d[i] = int(d[i])

    for i in range(f):
        final=final+(d[i]*(16**i))
    return(final)

def SeizeEnDeux(d):
    final=int()
    liste=list()
    nombre=str()
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
            d[i] = '13'
        elif d[i] == 'E':
            d[i] = 14
        elif d[i] == 'F':
            d[i] = 15
        d[i] = int(d[i])

    for i in range(f):
        final=final+(d[i]*(16**i))

    while final>0:
        liste.append(final%2)
        final=final//2
    liste.reverse()
    for i in range(len(liste)):
        nombre += str(liste[i])
    return(nombre)


if a==2 and b==10:
    c=list(input("Quelle est le nombre ?"))
    error=VerifBaseDeux(c)
    for i in range(len(c)):
        if c[i]=='.':
            reel=True
    if error==False:
        if reel==True:
            f=DeuxEnDixVirgule(c)
            print(f)
        else:
            f=DeuxEnDix(c)
            print(f)
    else:
        print("Erreur : votre chaine de caracteres n'est pas en base 2")

elif a==10 and b==2:
    c=list(input("Quelle est le nombre ?"))
    error=VerifBaseDix(c)
    if error==False:
        if(c[0])=='-':
            Negatif=True
        else:
            Negatif=False
        for i in range(len(c)):
            if c[i]=='.':
                reel=True
        if reel==True and Negatif==False:
            f=DixEnDeuxVirgule(c)
            print(f)
        elif reel == False and Negatif==False:
            f=DixEnDeux(c)
            print(f)
        elif reel == False and Negatif == True:
            f=DixEnDeuxNegatif(c)
            print(f)
        else:
            print('Le programme ne supporte pas les reels négatif')
    else:
        print('Erreur : certains carractere ne sont pas valide, merci de vérifier votre chiffre')

elif a==16 and b==10:
    c=list(input("Quelle est le nombre ?"))
    error=VerifBaseSeize(c)
    if error==False:
        f=SeizeEnDix(c)
        print(f)
    else:
        print('Erreur : certains carractere ne sont pas valide, merci de vérifier votre chiffre')


elif a==10 and b==16:
     c=int(input("Quelle est le nombre ?"))
     f=DixEnSeize(c)
     print(f)
elif a==2 and b==16:
    c=list(input("Quelle est le nombre ?"))
    error=VerifBaseDeux(c)
    for i in range(len(c)):
        if c[i]=='.':
            reel=True
    if error==False:
        if reel==True:
            print("Les reel ne sont pas supportés pour cette conversion")
        else:
            f=DeuxEnSeize(c)
            print(f)
    else:
        print('Erreur : certains carractere ne sont pas valide, merci de vérifier votre chiffre')
elif a==16 and b==2:
    c=list(input("Quelle est le nombre ?"))
    error=VerifBaseSeize(c)
    if error==False:
        f=SeizeEnDeux(c)
        print(f)
    else:
        print('Erreur : certains carractere ne sont pas valide, merci de vérifier votre chiffre')
else :
    print("Choisissez des bases valide")