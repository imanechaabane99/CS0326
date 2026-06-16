numeri=[1,2,3,4,5,6,7,8,9,10]
n=3
risultato=[]
i=0
for i in range(len(numeri)):
    t=i-(n-1)
    if t<0:
        t=0
    lista=numeri[t:i+1]
    risultato.append(sum(lista)/len(lista))
    i=i+1
print(risultato)     