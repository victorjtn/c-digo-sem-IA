# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]
        ]

    def tem_campeao(self):
        # Verifica linhas
        for linha in self.matriz:
            if linha[0] == linha[1] == linha[2] != Tabuleiro.DESCONHECIDO:
                return linha[0]

        # Verifica colunas
        for coluna in range(3):
            if (
                self.matriz[0][coluna] == self.matriz[1][coluna] == self.matriz[2][coluna]
                and self.matriz[0][coluna] != Tabuleiro.DESCONHECIDO
            ):
                return self.matriz[0][coluna] 

        # Verifica diagonais
        if (
            self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2]
            and self.matriz[0][0] != Tabuleiro.DESCONHECIDO
        ):
            return self.matriz[0][0]  

        if (
            self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0]
            and self.matriz[0][2] != Tabuleiro.DESCONHECIDO
        ):
            return self.matriz[0][2]  


        return Tabuleiro.DESCONHECIDO

    def jogo_empatado(self):
        # Verifica se todas as células estão preenchidas e não há vencedor
        if self.tem_campeao() != Tabuleiro.DESCONHECIDO:
            return False  

        for linha in self.matriz:
            if Tabuleiro.DESCONHECIDO in linha:
                return False 

        return True 