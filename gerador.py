import random

import string

tamanho = (int(input("De quantos caracteres sua senha precisa?: ")))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = "".join(random.choices(caracteres, k=tamanho))

print("Aqui está a sua senha: " +senha+ "")