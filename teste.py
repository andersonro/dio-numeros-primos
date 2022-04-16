from numeros_primos import numeros

num = 8
primo = numeros.numero(num)
if primo:
    print('Número {} é primo'.format(num))
else:
    print('Número {} não é primo'.format(num))
