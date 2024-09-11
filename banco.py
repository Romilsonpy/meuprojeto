class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if self.saques_diarios < 3 and valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R${valor:.2f}")
            self.saques_diarios += 1
            print("Saque realizado com sucesso!")
        else:
            print("Saque não permitido.")

    def ver_extrato(self):
        print("\nExtrato Bancário\n")
        for transacao in self.extrato:
            print(transacao)
        print(f"\nSaldo: R${self.saldo:.2f}")

    def reiniciar_saques_diarios(self):
        self.saques_diarios = 0

# Criando uma instância da classe Banco
banco = Banco()

# Menu de opções
while True:
    print("\nBem-vindo ao seu banco!")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        valor = float(input("Digite o valor a ser depositado: "))
        banco.depositar(valor)
    elif opcao == 2:
        valor = float(input("Digite o valor a ser sacado: "))
        banco.sacar(valor)
    elif opcao == 3:
        banco.ver_extrato()
    elif opcao == 4:
        print("Obrigado por usar nosso banco!")
        break
    else:
        print("Opção inválida.")

# Reiniciando os saques diários a cada dia (simplificado para demonstração)
banco.reiniciar_saques_diarios()