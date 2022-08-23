#calculadora

mensagem = "por favor insira a operação matemática que deseja: "
mensagem += "\n+ para adição"
mensagem += "\n- para subtração"
mensagem += "\n* para multiplicação"
mensagem += "\n/ para divisão"

operacao = input(mensagem)

numero1 = int(input("insira o primeiro num"))
numero2 = int(input("insira o segundo num"))

if operacao == '+':
    print(f"operacao: {numero1} {operacao} {numero2} = {numero1 + numero2} " )

elif operacao == '-':
    print(f"operacao: {numero1} {operacao} {numero2} = {numero1 - numero2} " )

elif operacao == '*':
    print(f"operacao: {numero1} {operacao} {numero2} = {numero1 * numero2} " )

elif operacao == '/':
    print(f"operacao: {numero1} {operacao} {numero2} = {numero1 / numero2} " )

else: 
    print("0")

sair = str(input("Digite 'sair' para sair do programa"))


