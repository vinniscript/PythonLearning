# PARADIGMAS DA PROGRAMAÇÃO

'''

O que é um paradigma de programação?

Definição: É um estilo de programação, a forma como você descreve a solução computacional de um problema.

Paradigmas mais populares:

    ° Imperativo: Um programa que é uma sequência de comandos que alteram o estado atual do sistema até atingir um estado final.

    ° Estruturado: Programas com uma estrutura de fluxo de controle e uso de procedimentos e funções. Uma melhoria do paradigma imperativo, com código mais organizados.

    º Orientado a objeto: Organização através de objetos que contém dados, estados próprios e métodos que alteram ou recuperam os dados/estados. Os objetos comunicam entre si para compor a lógica do programa.

Em oposição a esses paradigmas descritos acima, temos outros que focam mais no QUE o programador quer do que em como ele quer programar. São alguns deles:

    ° Declarativo: Especifica o que quer, porém sem detalhar como fazer.

    ° Funcional: Programas são avaliações de funções matemáticas sem alterar estados e com dados imutáveis.

    ° Lógico: especifica-se um conjunto de fatos e regras, o interpretador infere respostas para perguntas sobre o programa.

Não é tudo preto no branco assim, pois muitas linguagens de programação são, na verdade, multi-paradigmas, ou seja, possuem características de diversos paradigmas.
Contudo, na prática, elas acabam favorecendo um paradigma específico o que acaba lhes conferindo o título de linguagem "funcional" ou "imperativa" por exemplo.

Isso faz hoje muito difícil você ver uma linguagem e definir qual seu paradigma, por conta de suas diversas características de diferentes paradigmas imbutidas dentro de suas funcionalidades.

Por exemplo o Python que é visto de forma consistente a basicamente todos como uma linguagem orientada a objetos, porém a linguagem contém muitos outros conceitos e paradigmas compondo-a.

'''

# Aprofundando ao conceito de cada paradigma individualmente:

'''

º Paradigma Imperativo:

Descreve passo a passo o que deve ser feito.

O infame goto. "Pule para tal linha" (que é basicamente como funciona um hardware).

evoluiu para o procedutal e estruturado com o if, while, for...


'''

# Exemplo de paradigma imperativo em Python


alunos = {
    'joão': 5.5,
    'Ana Julia': 8.75,
    'Carlos': 4,
    'Roberto': 3.75,
    'Jesueola': 10
}


def verif_aprovacao(alunos):
    aprovados = []
    reprovados = []

    for nome, nota in alunos.items():  # o método .items() busca as chaves juntas de seus respectivos valores.
        if nota > 6:
            aprovados.append(nome)  # Se a nota for maior que 6, adicione (append) à lista de aprovados
        else:  # Se não
            reprovados.append(nome) # Adicione à lista de reprovados

    return aprovados, reprovados  # Toda função tem que ter um retorno, nesse caso, essa função irá retornar 2 listas.


aprovados, reprovados = verif_aprovacao(
    alunos)  # Essa função retorna 2 tuplas, o seu primeiro index [0] são os aprovados, o segundo [1] são os reprovados. Estamos apenas armazenando os index às variáveis "Aprovados" e "reprovados".

print("Alunos aprovados:")
for aluno in aprovados:
    print(aluno)

print("\nAlunos reprovados:")
for aluno in reprovados:
    print(aluno)
