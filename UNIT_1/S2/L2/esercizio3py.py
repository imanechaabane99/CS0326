a=int(input("inserisci un valore"))
b=int(input("inserisci un valore"))
c=int(input("inserisci un valore"))
if a%2==0:
    print("il primo valore è pari:")
else:
    print("il primo valore è dispari:")
print("la media è: ",(a+b+c)/3)
i=1
tabellina=[]
for i in range(11):
    tabellina.append(a*i)
    i=i+1
  print(tabellina)
a=int(input("quanti numeri vuoi scrivere"))
max=0
i=0
lista=[]
for i in range(a):
    lista.append(int(input("inserisci un numero")))
    if lista[i]>max:
        max=lista[i]
print("il massimo della lista è :",max)
s=input(str("inserisci una frase "))
print(s[::-1])
i=0
t=0
vocali="aeiouAEIOU"
for i in range(len(s)):
    if s[i] in vocali:
        t=t+1
i=i+1
print("le vocali nella frase sono: ", t)
