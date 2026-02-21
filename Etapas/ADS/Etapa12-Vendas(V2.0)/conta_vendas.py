"""
Módulo: conta_vendas
Responsabilidade: Regra de negócio do sistema de controle de vendas.
Contém a classe principal responsável por:
- Registrar vendas
- Registrar baixas
- Validar saldo
- Calcular total
- Conferir meta
- Exibir extrato

Atualização recente:
- Separação da interface (input/print) da regra de negócio.
- Método adicionar_baixa agora recebe a observação como parâmetro.
- Atributo _vendas protegido para evitar manipulação externa direta.
"""

class ContaVendas:

    def __init__(self, meta=50000):
        self._vendas = []   # Armazena entradas e saídas (lista de dicionários)
        self.meta = meta    # Meta financeira

    # =========================
    # CÉREBRO DO SISTEMA
    # =========================
    def calcular_total(self):
        """Calcula o total atual somando vendas e baixas."""
        total = 0
        for item in self._vendas:
            total += item["valor"]
        return total

    # =========================
    # REGISTRO DE VENDA
    # =========================
    def adicionar_venda(self, valor):
        """Registra uma nova venda validando valor positivo."""
        if valor <= 0:
            return False, "Valor de venda inválido"

        self._vendas.append({
            "tipo": "venda",
            "valor": valor
        })

        if self.calcular_total() >= self.meta:
            return True, f"Meta de R$ {self.meta:.2f} atingida!"

        return True, "Venda registrada"

    # =========================
    # REGISTRO DE BAIXA
    # =========================
    def adicionar_baixa(self, valor, observacao):
        """
        Registra uma baixa no sistema.
        A observação deve ser fornecida pela interface.
        """
        if valor <= 0:
            return False, "Baixa inválida"

        if not self.validar_baixa(valor):
            return False, "Baixa não registrada: total insuficiente"

        self._vendas.append({
            "tipo": "baixa",
            "valor": -abs(valor),
            "observacao": observacao
        })

        return True, "Baixa registrada!"

    # =========================
    # VALIDAÇÃO DE BAIXA
    # =========================
    def validar_baixa(self, valor):
        """Impede que o total fique negativo."""
        return self.calcular_total() - valor >= 0

    # =========================
    # CONFERÊNCIA DE META
    # =========================
    def conferir_sobra(self):
        """Retorna valor excedente acima da meta."""
        total = self.calcular_total()
        if total >= self.meta:
            return total - self.meta
        return 0

    # =========================
    # EXTRATO
    # =========================
    def exibir_extrato(self):
        """Exibe histórico detalhado de vendas e baixas."""
        print("||| Extrato de Vendas e Baixas |||")

        for item in self._vendas:

            if item["tipo"] == "venda":
                print(f"Venda de: R$ {item['valor']:.2f}")

            if item["tipo"] == "baixa":
                print(f"Baixa de: -R$ {abs(item['valor']):.2f} | Motivo: {item['observacao']}")

        print(f"Total atual: R$ {self.calcular_total():.2f}")

        sobra = self.conferir_sobra()
        if sobra > 0:
            print(f"Valor excedente à meta: R$ {sobra:.2f}")

        print("-" * 30)