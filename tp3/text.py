a=list(input())
final=list()
final2=str()
for i in range(len(a)):
    if a[i]=='u':
        final.append(1)
    elif a[i]=='w':
        final.append(0)
    else:
        final.append(a[i])
for i in range(len(final)):
    final2+=str(final[i])
print(final2)
