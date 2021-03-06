from Fila_Base import FilaBase
from Constantes import CODIGO_NORMAL


class FilaNormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f"${CODIGO_NORMAL}{self.codigo}"

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f"cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}")
