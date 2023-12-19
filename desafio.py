from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

>>> """

saldo  = 0
limite = 0 
extrato = f""" """
numero_saques = 0
LIMITES_SAQUES = 3

def horas():
    data_hora = datetime.now()
    dt_hr_format = "%d-%m-%Y %H:%M:%S"
    dt_hr_formatada = data_hora.strftime(dt_hr_format)
    return dt_hr_formatada


while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        
        valor = float(input("Digite o valor a ser depositada: "))
        if valor > 0 :
            saldo += valor
            dt_hr_formatada =horas()
            print(f"Deposito Realizado com sucesso, as {dt_hr_formatada}")
            
            extrato+=(f""" 
Saldo de: R${saldo:.2f}
{dt_hr_formatada} - Realizado Deposito no valor de: R$ {valor:.2f}""")
        else:
            print("Somente valores superiores a zero")
        
    elif opcao == "s":
        valor_saq = float(input("Digite o valor a ser sacado: "))
        if (LIMITES_SAQUES <= 3 and LIMITES_SAQUES > 0) and (valor_saq <=500 and valor_saq > 0):
            saldo -= valor_saq
            LIMITES_SAQUES -= 1
            print("Saque realizado com sucesse!")
            
            dt_hr_formatada =horas()
            extrato+=(f"""
Saldo de: R${saldo:.2f}
{dt_hr_formatada} - Realizado Saque no valor de: R$ {valor_saq:.2f}""")
        else:
            if (valor_saq > saldo):
                print("Saldo insuficiente")
            elif LIMITES_SAQUES == 0:
                print("Limite diario de saque diario excedido") 
            elif valor_saq > 500:
                print("Limite de saque é de R$ 500.00 por saque")
        
    elif opcao == "e":
        print(extrato)
    elif opcao == 'q':
        break