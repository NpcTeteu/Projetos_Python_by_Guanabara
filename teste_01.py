import math
num = int(input("Digite um número "))
# módulo que faz a raiz quadrada ao ínves de fazer uma potência de 0,5 do número
raiz = math.sqrt(num)

print("A raiz de {:.0f} é igual a {:.0f}".format(num,math.floor(raiz)))
