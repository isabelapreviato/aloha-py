# def  copa_do_mundo(pais, *anos):
#     print(f'País: {pais}')

#     for year in anos:
#         print(f'Ano: {year}')

# copa_do_mundo('Brasil', '58', '62', '70', '94', '02')


# 0

def soma(x, y):
    return x+y

num1 = float(input("Digite um número: "))
num2 = float(input('Digite outro número: '))

resultado = soma(x=num1, y=num2)
print(f'{num1} + {num2} = {resultado}')

# 1

num = int(input('Digite um número: '))

if num % 2 == 0:
    print("Número par.")
else:
    print("Número ímpar.")

#2

def intervalo(a, b):
    lista = (range(a, b))

numm1 = int(float(input('Digite o começo do intervalo: ')))
numm2 = int(float(input('Digite o fim do intervalo: ')))

print(lista)