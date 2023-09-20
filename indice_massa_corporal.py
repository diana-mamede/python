"""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo coma a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 ate 40: Obesidade
- Acima de 40: Obesidade morbida"""

altura = float(input('Digite, em metros, sua altura: '))
peso = float(input('Digite, em kg, seu peso: '))
imc = peso / (altura**2)
print('=' * 20)
print('Calculando seu IMC...')
print('=' * 20)
if imc < 18.5:
    print(f'Seu indice de massa corporal é {imc :.1f}: Abaixo do peso. ')
elif 18.5 <= imc < 25:
    print(f'Seu indice de massa corporal é {imc :.1f}: Peso ideal. ')
elif 25 <= imc < 30:
    print(f'Seu indice de massa corporal é {imc :.1f}: Sobrepeso. ')
elif 30 <= imc < 40:
    print(f'Seu indice de massa corporal é {imc :.1f}: Obesidade. ')
elif imc >= 40:
    print(f'Seu indice de massa corporal é {imc :.1f}: Obesidade morbida. ')
