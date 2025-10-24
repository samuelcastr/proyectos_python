# Algoritmo: Verificar si un número es primo

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Probar la función con varios valores
for numero in range(1, 21):
    if es_primo(numero):
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")
