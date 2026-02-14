from datetime import datetime

def calcula_idade_exata(dia, mes, ano_nascimento):
    hoje = datetime.now()
    idade = hoje.year - ano_nascimento
    if (hoje.month < mes) or (hoje.month == mes and hoje.day < dia):
        idade -= 1 
        
    return idade

def main():
    try:
        print("--- Calculadora de Idade Precisa ---")
        dia = int(input("Digite o dia do seu nascimento: "))
        mes = int(input("Digite o mês do seu nascimento: "))
        ano = int(input("Digite o ano do seu nascimento: "))
        
        idade_real = calcula_idade_exata(dia, mes, ano)
        
        if idade_real >= 0:
            print(f"\nSua idade exata hoje é: {idade_real} anos.")
        else:
            print("\nData inválida (ano futuro).")
            
    except ValueError:
        print("\nPor favor, digite apenas números inteiros.")

if __name__ == "__main__":
    main()