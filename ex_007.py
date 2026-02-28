# O tipo float permite números com vírgula
n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite outro nota: "))

# O python prioriza a operação que está dentro dos parênteses
média = (n1+n2)/2

# ':.1f' significa que só vai aparecer uma casa depois da vírgula
print("A média entre {:.1f} e {:.1f} é igual a {:.1f}".format(n1,n2,média))
