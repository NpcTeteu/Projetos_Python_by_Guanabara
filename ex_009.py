real = float(input('Digite quantos reais tem em sua carteira R$'))
# A cada 1 real equivale o valor em dolar, euro e iene
dolar = real / 5.27
euro = real / 6.25
iene = real / 29.37

print('Com {:.2f}R$ você pode comprar US{:.2f}, {:.2f}€, {:.2f}¥'.format(real,dolar,euro,iene))
