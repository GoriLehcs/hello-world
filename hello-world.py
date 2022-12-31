print("hello world!")

# Programinha básico para mostrar primos.

n = int(input("Voce quer receber primos de 0 a: "))
for x in range(0, n):
    c = 0
    for y in range(1, x+1):
        if x % y == 0:
            c += 1
    if c == 2:
        print(x)
