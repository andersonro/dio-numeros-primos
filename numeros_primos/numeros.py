def numero(numero):
    result = False
    sum = 0
    for j in range(1, (numero+1)):
        if numero % j == 0:
            sum += 1
    if sum != (2):
        result = False
    else:
        result = True

    return result
