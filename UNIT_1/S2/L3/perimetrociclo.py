#programma che misura il perimetro di cerchio rettangolo e quadrato
a="SI"
while a=="SI" or a=="si":
    import math
    figura=int(input("inserisci una figura geometrica 1=per quadrato 2=per rettangolo 3=per cerchio: "))
    if figura==1:
        lato=float(input("inserisci il valore del lato del quadrato: "))
        p=lato*4
        print(f"il perimetro del quadrato è {p}")
    elif figura==3:
        raggio=float(input("inserisci il raggio: "))
        p=raggio*math.pi *2
        print(f"il perimetro della cerchio è {p}")
    elif figura==2:
        base1=float(input("inserisci la prima base: "))
        base2=float(input("inserisci la seconda base: "))
        p=(base1+base2)*2
        print(f"il perimetro del rettangolo è {p}")
    else:
        print("la figura non è disponibile")
    a=input("vuoi continuare SI o NO")
