#PROGRAMMA CHE CALCOLA LA SEQUENZA DI FIBONACCI DEI PRIMI N NUMERI RICHIESTI DALL'UTENTE
n=int(input("Di quanti numeri vuoi la sequenza di Fibonacci: "))
lista_fibonacci=[]
t=-1 
m=-2
for n in range(n,-1,-1):
    if(n==1):
        m=0
    if(n==0):
        m=0
        t=0
       
    f=2*n+t+m
    lista_fibonacci.append(f)
print(lista_fibonacci)    