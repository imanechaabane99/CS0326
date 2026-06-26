from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import base64

#carica la chiave privata
with open("private_key.pem","rb") as key_file:
    privete_key= serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

#carica la chiave pubblica
with open("public_key.pem","rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

messaggio="sono 3 settimane che studio" 

#criptazione con la chiave pubblica
encypted=public_key.encrypt(messaggio.encode(), padding.PKCS1v15())

#decriptazione della chiave privata
decrypted=privete_key.decrypt(encypted, padding.PKCS1v15())

print("messaggio originale: ", messaggio)
print("messaggio cripatato: ", base64.b64encode(encypted).decode("utf-8"))
print("messaggio decriptato: ", decrypted.decode("utf-8"))
