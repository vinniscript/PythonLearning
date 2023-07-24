class Vetor:
    def __init__(self,n1):  # Defininfo uma classe __init__ é como definir um método construtor em uma classe java / Self define que o parâmetro da classe se refere a ela mesma.
        self.n1 = n1  # Aqui definimos o valor padrão dos atributos de nossa classe e quais métodos são chamados em seu instanciamento.
        self.vetor = [1, 2, -3, -4]  # Array
        self.pessoa = {'Nome': 'Caio'}  # Dicionário

        # ===== Métodos matemáticos ===== #

    def __add__(self, n):  # __add__ é chamado automaticamente pelo Python ao somar um objeto a um número.
        return self.n1 + n

    def __sub__(self, n):  # __sub__ faz a subtração, porém com a mesma regra de objeto para/com números
        if not isinstance(n, int):  # Verifica se n não é uma instância da classe de um número inteiro.
            n = int(n)  # Se realmente não for, aqui rola a conversão (casting).

        return self.n1 - n

    def __mul__(self, n):  # Multiplicação
        if not isinstance(n, int):
            n = int(n)

        return self.n1 * n

    def __mod__(self, n):  # Resto da divisão
        if not isinstance(n, int):
            n = int(n)

        return self.n1 % n

    def __pow__(self, n):  # Exponenciação
        if not isinstance(n, int):
            n = int(n)
        return self.n1 ** n

    # ===== Métodos condicionais ===== #

    def __eq__(self, n):
        return True if self.n1 == n else False  # Valida se a comparação é válida ou não

    def __neg__(self):  # Não é necessário parâmetros, ele trabalha apenas com os atributos de seu próprio objeto.
        return list(
            map(lambda x: -x if x > 0 else x, self.vetor))  # Converter todos os números de uma lista para negativo.

    def __pos__(self):
        return list(map(lambda x: x * -1 if x < 0 else x, self.vetor))  # Converter para positivo.

    def __getitem__(self, key):
        if not key in self.pessoa.keys():  # Para evitar erros, criamos essa condicional caso o programa tente buscar uma chave inexistente.
            self.pessoa[
                key] = None  # Retorna None quando é chamado uma chave não definida, porém agora essa chave existe dentro de self.pessoa, porém seu valor agora atual é None.
        return self.pessoa[key]

    def __setitem__(self, key, value):
        self.pessoa[key] = value

    def __delitem__(self, key):
        del self.pessoa[key]

    def __call__(self, *args, **kwargs):
        print('Fui chamado', args)


x = Vetor(2)  # Instância da class / o valor '2' equivale ao segundo parâmetro n1.

# Outputs (Matemáticos)
print(x + 3)  # 5
print(x - '3')  # -1
print(x * 3)  # 6
print(x ** 3)  # 8

# Outputs (comparativos)
print(x == 2)  # true
print(-x)  # [-1, -2, -3, -4]
print(+x)  # [1, 2, 3, 4]
print(x['Nome'])  # Caio
print(x['Idade'])  # None
x['Altura'] = 173  # Chama o método mágico __setitem__ e adiciona a chave "Altura" e seu valoe "173" ao dicionária "pessoa"
print(x.pessoa)  # {'Nome': 'Caio', 'Idade': None, 'Altura': 173}
del x['Nome']  # Chama o __delitem__ apaga a chave passada
print(x.pessoa)  # {'Idade': None, 'Altura': 173}

# Se você chamar sua classe como um a função, o método mágico __call__ será chamado
x('alooo', 123)  # Fui chamado ('alooo', 123)

# Em python tudo é um objeto. Um número inteiro é um objeto do tipo inteiro, um float é um objeto do tipo float e assim por diante...

# 1 + 1 Uma operação de soma entre 2 objetos de tipo inteiro.

# print(dir(int)) retorna todos os métodos implementados dentro de um método inteiro.

# __init__ se lê "dunder init".

# Métodos que iniciam e terminam com "__" são conhecidos como métodos dunder, ou métodos mágicos.
