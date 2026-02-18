cal = float(input('Digite [1] para soma e [2] para subtração: '))
def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

def main():
    a = float(input('Digite um valor: '))
    b = float(input('Digite outro valor: '))
    s = soma(a,b)
    su = sub(a,b)
    if cal==1:
        print(s)
    elif cal==2:
        print(su)
    else:
        print("Opreação inválida!")
main()
