Descrição: Este projeto foi desenvolvido como parte de um trabalho escolar com o objetivo de simular os movimentos das principais peças do jogo de xadrez. Cada peça possui regras específicas de movimentação, e o código implementa essas regras utilizando conceitos de orientação a objetos em Python.
Objetivo: Demonstrar o funcionamento das regras de movimentação das peças de xadrez por meio de classes e métodos em Python, reforçando o aprendizado sobre herança, polimorfismo e lógica condicional.
Técnicas usadas: Python 3 e Programação Orientada a Objetos (POO).
Funcionalidades
Classes para cada peça do xadrez:
Rei
Rainha
Torre
Bispo
Cavalo
Peão

Método movimento_valido(origem, destino) para verificar se o movimento é permitido conforme as regras oficiais do xadrez.
Suporte para peças brancas e pretas (no caso do peão, que tem movimentação diferente).

Como vai executar: Certifique-se de ter o Python instalado.
Salve o código em um arquivo chamado xadrez.py.
Importe as classes e teste os movimentos com coordenadas no formato (linha, coluna):

Pythonfrom xadrez import Rei, Rainha, Torre, Bispo, Cavalo, Peaorei = Rei('branco')print(rei.movimento_valido((4, 4), (5, 5)))  # True

Créditos: Trabalho escolar de Arquitetura de Computadores / Lógica de Programação
Desenvolvido por Wesley Vieira

