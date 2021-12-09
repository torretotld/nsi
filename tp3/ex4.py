# Fonction
def VerifBaseDix(c):
    error=False
    point=False
    for i in range(len(c)):
        if c[i]!= '1' and c[i]!= '2' and c[i]!= '3' and c[i]!= '4' and c[i]!= '5' and c[i]!= '6' and c[i]!= '7' and c[i]!= '8' and c[i]!= '9' and c[i]!= '0' :
            error=True
    return(error)

#Dictionnaire
quatre_vingt_dix=list()
quatre_vingt_dix=['quatre-vingts dix', 'quatre-vingt onze','quatre-vingt douze','quatre-vingt treize','quatre-vingt quatorze','quatre-vingt quinze','quatre-vingt seize','quatre-vingt dix-sept','quatre-vingt dix huit','quatre-vingt dix neuf']
dix=['dix','onze','douze','treize','quatorze','quinze','seize','dix-sept','dix-huit','dix-neuf']
unite=['','un','deux','trois','quatre','cinq','six','sept','huit','neuf']
dizaine=['','dix','vingt','trente','quarante','cinquante','soixante','soixante-dix','quatre-vingt','quatre-vingt-dix']

#variable
d=int()
final=list()
final2=str()

#code
a=list(input("Entrez votre valeur : "))
error=VerifBaseDix(a)
if error == True :
    print("Merci d'entrer un nombre en base 10")
else:
    p=1 #puissance
    a.reverse()
    for z in range(len(a)): # conversion liste en int()
        a[z]=int(a[z])
        d=d+(a[z]*p)    # d = chiffre
        p*=10
    if d > 10000000000000:
        print("Le programme ne supporte pas des chiffres aussi grand")
    elif d == 0 :
        print(d,": zéro")
    else:
        while len(a)<12:
            a.append(0)
        #traitement  3 premiers chiffres
        if a[0]!=0 or a[1]!=0 or a[2]!=0:
            if a[1]==1 :
                final.append(dix[a[0]])
            elif a[1]==9:
                final.append(quatre_vingt_dix[a[0]])
            else:
                if a[0]==1 and a[1]!=8 and a[1]!=0:
                    final.append('et un')
                    final.append(dizaine[a[1]])

                else:
                    final.append(unite[a[0]])
                    final.append(dizaine[a[1]])
            if a[2]!=0:
                if a[2]==1:
                    final.append('cent')
                else:
                    final.append('cents')
                    final.append(unite[a[2]])
        print(final)
        if a[3]!=0 or a[4]!=0 or a[5]!=0:
            if a[3] == 1 and a[4]== 0 and a[5]==5:
                final.append('mille')
            else:
                final.append('milles')
                if a[4]==1 :
                    final.append(dix[a[3]])
                elif a[4]==9:
                    final.append(quatre_vingt_dix[a[3]])
                else:
                    if a[3]==1 and a[4]!=8 and a[4]!=0:
                        final.append('et un')
                        final.append(dizaine[a[4]])

                    else:
                        final.append(unite[a[3]])
                        final.append(dizaine[a[4]])
                if a[5]!=0:
                    if a[5]==1:
                        final.append('cent')
                    else:
                        final.append('cents')
                        final.append(unite[a[5]])
        if a[6]!=0 or a[7]!=0 or a[8]!=0:
            if a[6] == 1 and a[7]== 0 and a[8]==0:
                final.append('un million')
            else:
                final.append('millions')
                if a[7]==1 :
                    final.append(dix[a[6]])
                elif a[7]==9:
                    final.append(quatre_vingt_dix[a[6]])
                else:
                    if a[6]==1 and a[7]!=8 and a[7]!=0:
                        final.append('et un')
                        final.append(dizaine[a[7]])

                    else:
                        final.append(unite[a[6]])
                        final.append(dizaine[a[7]])
                if a[8]!=0:
                    if a[8]==1:
                        final.append('cent')
                    else:
                        final.append('cents')
                        final.append(unite[a[8]])
        if a[9]!=0 or a[10]!=0 or a[11]!=0:
            if a[9] == 1 and a[10]== 0 and a[11]==0:
                final.append('un milliard')
            else:
                final.append('milliards')
                if a[10]==1 :
                    final.append(dix[a[9]])
                elif a[10]==9:
                    final.append(quatre_vingt_dix[a[9]])
                else:
                    if a[9]==1 and a[10]!=8 and a[10]!=0:
                        final.append('et un')
                        final.append(dizaine[a[10]])

                    else:
                        final.append(unite[a[9]])
                        final.append(dizaine[a[10]])
                if a[11]!=0:
                    if a[11]==1:
                        final.append('cent')
                    else:
                        final.append('cents')
                        final.append(unite[a[11]])
        final.reverse()
        if '' in final :
            final.remove('')
        for i in range(len(final)):
            final2+=str(final[i])
            final2+=' '




        print(final2)
