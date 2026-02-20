cal = float(input('Digite [1] para soma, [2] para subtração, [3] para multiplicação e [4] para divisão: '))
def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

def main():
    a = float(input('Digite um valor: '))
    b = float(input('Digite outro valor: '))
    res_soma = soma(a, b)
    res_sub = sub(a, b)
    res_mult = mult(a, b)
    res_div = div(a, b)

    if cal == 1:
        print(res_soma)
    elif cal == 2:
        print(res_sub)
    elif cal == 3:
        print(res_mult)
    elif cal == 4:
        print(res_div)
    else:
        print("Opreação inválida!")
main()
