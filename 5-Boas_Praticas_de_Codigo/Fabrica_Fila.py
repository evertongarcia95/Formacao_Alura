from typing import Union

from Constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from Fila_Normal import FilaNormal
from Fila_Prioritaria import FilaPrioritaria


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila) -> Union[TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo não cadastrado')
