VRB = float(input('Digite o valor que você tem em conta: R$'))
CD = float(input('Digite o valor da cotação atual do dólar: US$'))



CRD = (VRB/CD)

print(f'Com a cotação atual do dólar, vôce pode comprar este valor em dólares ==> US${CRD:.2f}')
