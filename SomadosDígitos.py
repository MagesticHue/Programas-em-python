a = int(eval(input("Digites os numeros:")))

soma = 0

mod = a % 10
div = a // 10
soma = soma + mod

while div > 0 :
        mod = div % 10
        soma = soma + mod
        div = div // 10
print(soma)

#Felipe José
#@MagesticHue
