#PROGRAMMA CHE CALCOLA IL FATTORIALE DI UN NUMERO
numero=int(input("inserisci il numero di cui vuoi calcolare il fattoriale: "))
fattoriale=numero
for i in range(numero-1,0,-1):
    fattoriale=fattoriale*i
print(f"Il fattoriale è: {fattoriale}")