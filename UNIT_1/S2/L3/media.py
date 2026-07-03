numeri=input("inserisci una lista di numeri separati da uno spazio: ")
lista_numeri=list(map(int, numeri.split()))
t=len(lista_numeri)
num_ordinati=sorted(lista_numeri)
somma=0
moda=[]
a=0
n=0
c=0
for i in lista_numeri:
    for num in lista_numeri:
        if(num==i):
            a=a+1
            
        
    
    if(a>n): 
        moda.clear()
        moda.append(i)
        n=a
    elif(a==n):
        if i not in moda:
            moda.append(i)

    a=0
    somma=somma+i
media=somma/t
if(t%2==1):
    mediana=num_ordinati[(t+1)//2]
else:
    mediana=(num_ordinati[t/2]+num_ordinati[t//2+1])/2
print(f"La media è {media} ")
print(f"La moda è {moda}")
print(f"La mediana è {mediana}")