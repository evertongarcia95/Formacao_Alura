from Fila_Normal import FilaNormal
from Fila_Prioritaria import FilaPrioritaria
from Fabrica_Fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada


test_Fabrica = FabricaFila.pega_fila("normal")
test_Fabrica.atualiza_fila()
test_Fabrica.atualiza_fila()
test_Fabrica.atualiza_fila()
print(test_Fabrica.chama_cliente(5))
print(test_Fabrica.chama_cliente(6))
print(test_Fabrica.chama_cliente(7))
test_Fabrica = FabricaFila.pega_fila("prioritaria")
test_Fabrica.atualiza_fila()
test_Fabrica.atualiza_fila()
test_Fabrica.atualiza_fila()
print(test_Fabrica.chama_cliente(1))
print(test_Fabrica.chama_cliente(2))
print(test_Fabrica.chama_cliente(3))
