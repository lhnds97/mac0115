def main():
    a = input('Digite a: ')
    b = input('Digite b: ')

    a, b = int(a), int(b)

    resultado = mdc(a,b)

    print(f'MDC({a},{b}) = {resultado}')


def mdc(a, b):
    """
    :param a: inteiro
    :param b: interio
    :return: mdc(a,b)
    """

    resultado = 1
    divisor = 2  # começar a testar divisores com 2

    while divisor <= a:
        if a % divisor == 0 and b % divisor == 0:
            resultado = divisor
        divisor += 1

    return resultado


main()