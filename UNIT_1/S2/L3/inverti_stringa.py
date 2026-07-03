#Creato da me
frase=input("inserisci una frase: ")
inversa=[]
lista_inversa=list(frase)
for i in reversed(lista_inversa):
    inversa.append(i)
stringa="".join(inversa)
print(stringa)

#Metodo trovato su internet
frase=input("inserisci un frase: ")
print(frase[::-1])
