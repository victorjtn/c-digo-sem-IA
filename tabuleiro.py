# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):

        # Verifica as colunas
        for c in range(0,3):
            soma = self.matriz[0][c] + self.matriz[1][c] + self.matriz[2][c]
            if soma == 3:
                return Tabuleiro.JOGADOR_0
            elif soma == 12:
                return Tabuleiro.JOGADOR_X
        # Verifica as linhas
        for l in range(0,3):
            soma = self.matriz[l][0] + self.matriz[l][1] + self.matriz[l][2]
            if soma == 3:
                return Tabuleiro.JOGADOR_0
            elif soma == 12:
                return Tabuleiro.JOGADOR_X
        # Verifica as diagonais
        soma = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]
        if soma == 3:
            return Tabuleiro.JOGADOR_0
        elif soma == 12:
            return Tabuleiro.JOGADOR_X
        soma = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]
        if soma == 3:
            return Tabuleiro.JOGADOR_0
        elif soma == 12:
            return Tabuleiro.JOGADOR_X
        return Tabuleiro.DESCONHECIDO