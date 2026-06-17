#programma che misura il perimetro di cerchio rettangolo e quadrato
import math
figura=int(input("inserisci una figura geometrica 1=per quadrato 2=per rettangolo 3=per cerchio: "))
if figura==1:
    lato=float(input("inserisci il valore del lato del quadrato: "))
    p=lato*4
    print(f"il perimetro della figura è {p}")
elif figura==3:
    raggio=float(input("inserisci il raggio: "))
    p=raggio*math.pi *2
    print(f"il perimetro della figura è {p}")
elif figura==2:
    base1=float(input("inserisci la prima base: "))
    base2=float(input("inserisci la seconda base: "))
    p=(base1+base2)*2
    print(f"il perimetro della figura è {p}")
else:
    print("la figura non è disponibile")
