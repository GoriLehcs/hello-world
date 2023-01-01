# Este programa calcula e mostra quantos anagramas são possíveis formar com um nome.
n1 = -1
def fac(n:int):
    prod = 1
    for x in range(1, n+1):
        prod *= x
    return prod

nome = input("Insira o nome: ")
n = fac(len(nome))
# for _ in range(n):
for l in range(len(nome)):
    n1 += 1
    for x in nome:
        n2 = -1
        print(n1 + n2)
        for letra in nome:
            n2 += 1
            print(nome[n2], end='')
    print('')