num = int(input("Digite um numero inteiro:"))
adjacente = 0
resto = num % 10
num = num // 10
aux = num % 10

while num > 0:
        if aux == resto:
                adjacente = adjacente + 1
        resto = num % 10
        num = num // 10
        aux = num % 10

if adjacente > 0:
        print("sim")
else :
        print("nao")
        
#Felipe José
#@MagesticHue
        
