#Peça para o usuário digitar um número:

#faça um programa que conte todos os números pares de 1 até o número digitado pelo usuário, assim como, os números impares.

numero = float(input("Digite um número:"))

contador_par=0
contador_impar=0

while(True):
    if numero % 2 == 0:
        print(f"De 1 até {numero} temos {contador_par + 1} números pares.")
    else:
        print(f"De 1 até {numero} temos {numero}")
