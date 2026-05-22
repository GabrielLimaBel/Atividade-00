peso = float(input('digite o peso em quilos: '))
altura = float(input('digite a altura em metros: '))
idade = int(input('digite a idade em anos: '))

BMR = ((10*peso) + (6.25*altura) - (5*idade) + 5)
print(f"Sua taxa metabólica basal é de: {BMR}" "para calcular novamente feche o programa e forneça novamente os dados!")