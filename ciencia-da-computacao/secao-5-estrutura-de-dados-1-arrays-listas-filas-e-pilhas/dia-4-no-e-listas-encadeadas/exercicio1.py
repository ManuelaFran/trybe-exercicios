# Aprimorando a classe Lista: nossa classe Lista atende as principais
# operações que essa TAD nos oferece, mas que tal melhorarmos? Para isso, você
# deve adicionar os seguintes métodos:
# a. A operação clear nos permite remover todos os Nodes da lista;
# b. A operação __get_node_at nos permite acessar o Node em qualquer posição
# da lista.

"""1 - a. clear(self) - Para este desafio existem 2 possibilidades de
respostas a serem implementadas. A opção #1 só funciona, sem que ocorra
vazamento de memória, graças ao garbage collector do python, porém, o mais
indicado é a opção #2, pois utilizam a própria estrutura para atribuir um novo
comportamento."""


# 1
def clear(self):
    self.head_value = None
    self.__length = 0


# 2
def clea(self):
    while not self.is_empty():
        self.remove_first()


"""1 - b. __get_node_at(self, position) - Para este desafio foi realizado a
extração do trecho de código mais repetitivo, que estava sendo utilizado nos
demais métodos. Vale salientar que nos casos que precisamos do anterior ao
ultimo, precisamos fazer a operação len(self) - 2."""


def get_node_at(self, position):
    value_to_be_returned = self.head_value
    if value_to_be_returned:
        while position > 0 and value_to_be_returned.next:
            value_to_be_returned = value_to_be_returned.next
            position -= 1
    return value_to_be_returned
