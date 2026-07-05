#PROGRAMMA CHE CALCOLA LE OCCORRENZE DELLE PAROLE
stringa=input("Inserisci frase: ")
lista_parole=stringa.split()
lista_fatte=[]
a=0
for parola in lista_parole:
    a=0
    for t in lista_parole:
        if(t==parola):
            a=a+1
                  
    if parola not in lista_fatte:
        print(f"La parola {parola} compare {a} volte")                    
        lista_fatte.append(parola)      

