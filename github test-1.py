import time
print ('Bem vindo a calculadora!')
time.sleep(2)
print ('Digite a equação desejada (ex: 2+3 ou 10/2)')
time.sleep(1)
equacao = input(">>>")
try:
    resultado = eval(equacao) #avalia a expressão digitada
    print("Resultado:", resultado)
except:
    print("equação inválida!")
