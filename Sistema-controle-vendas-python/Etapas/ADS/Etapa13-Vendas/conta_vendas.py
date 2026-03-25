import json
import os
from datetime import datetime


class ContaVendas:

    # ===========================
    # CARREGAMENTO E SALVAMENTO
    # ===========================

    def carregar_dados(self):
        if os.path.exists("dados.json"):
            with open("dados.json", "r") as arquivo:
                self._vendas = json.load(arquivo)
        else:
            self._vendas = []

    def salvar_dados(self):
        with open("dados.json", "w") as arquivo:
            json.dump(self._vendas, arquivo, indent=4)

    def excluir_dados(self):
        self._vendas = []
        self.salvar_dados()

    def __init__(self, meta=50000):
        self._vendas = []
        self.meta = meta
        self.carregar_dados()

    # =========================
    # DATA
    # =========================

    def obter_data(self):
        agora = datetime.now()
        return agora.strftime("%d/%m/%Y")

    # =========================
    # CÉREBRO
    # =========================

    def calcular_total(self):
        total = 0
        for item in self._vendas:
            total += item["valor"]
        return total

    # =========================
    # VENDA
    # =========================

    def adicionar_venda(self, valor):

        if valor <= 0:
            return False, "Valor inválido"

        self._vendas.append({
            "tipo": "venda",
            "valor": valor,
            "data": self.obter_data()
        })

        self.salvar_dados()

        if self.calcular_total() >= self.meta:
            return True, f"Meta de R$ {self.meta:.2f} atingida!"

        return True, "Venda registrada"

    # =========================
    # BAIXA
    # =========================

    def adicionar_baixa(self, valor, observacao):

        if valor <= 0:
            return False, "Baixa inválida"

        if not self.validar_baixa(valor):
            return False, "Saldo insuficiente"

        self._vendas.append({
            "tipo": "baixa",
            "valor": -abs(valor),
            "observacao": observacao,
            "data": self.obter_data()
        })

        self.salvar_dados()

        return True, "Baixa registrada"

    # =========================
    # VALIDAÇÃO
    # =========================

    def validar_baixa(self, valor):
        return self.calcular_total() - valor >= 0

    # =========================
    # EXTRATO
    # =========================

    def exibir_extrato(self):

        print("\n||| EXTRATO |||\n")

        for item in self._vendas:

            if item["tipo"] == "venda":
                print(f"{item['data']} | Venda: R$ {item['valor']:.2f}")

            if item["tipo"] == "baixa":
                print(f"{item['data']} | Baixa: -R$ {abs(item['valor']):.2f} | {item['observacao']}")

        print(f"\nTotal: R$ {self.calcular_total():.2f}")
        print("-" * 30)

    # =========================
    # SOBRA
    # =========================

    def conferir_sobra(self):
        total = self.calcular_total()

        if total >= self.meta:
            return total - self.meta

        return 0

    # =========================
    # COMISSÃO
    # =========================

    def calcular_comissao(self, percentual=0.30):

        total_comissao = 0

        for item in self._vendas:
            if item["tipo"] == "venda":
                total_comissao += item["valor"] * percentual

        return total_comissao

    # =========================
    # TOTAL POR MÊS
    # =========================

    def calcular_total_mes(self, mes):

        total = 0

        for item in self._vendas:

            if item["tipo"] == "venda":
                mes_venda = item["data"][3:5]

                if mes_venda == mes:
                    total += item["valor"]

        return total

    # =========================
    # META POR MÊS
    # =========================

    def meta_mes(self, mes):

        total_mes = self.calcular_total_mes(mes)
        return total_mes >= self.meta