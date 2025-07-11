# -*- coding: utf-8 -*-
from random import randint  # Usaremos randint no lugar de choice

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

        if tipo == Tabuleiro.JOGADOR_X:
            self.oponente = Tabuleiro.JOGADOR_0
        else:
            self.oponente = Tabuleiro.JOGADOR_X

    def getJogada(self) -> (int, int):

        vazias = []
        for i in range(3):
            for j in range(3):
                if self.matriz[i][j] == Tabuleiro.DESCONHECIDO:
                    vazias.append((i, j))

        # REGRA 1: Ganhar ou bloquear o oponente
        for i, j in vazias:
            self.matriz[i][j] = self.tipo
            if self.tabuleiro.tem_campeao() == self.tipo:
                self.matriz[i][j] = Tabuleiro.DESCONHECIDO
                return (i, j)
            self.matriz[i][j] = Tabuleiro.DESCONHECIDO

        # Verifica se o oponente pode ganhar
        for i, j in vazias:
            self.matriz[i][j] = self.oponente
            if self.tabuleiro.tem_campeao() == self.oponente:
                self.matriz[i][j] = Tabuleiro.DESCONHECIDO
                return (i, j)
            self.matriz[i][j] = Tabuleiro.DESCONHECIDO

        # REGRA 2: Criar duas chances de vitória
        for i, j in vazias:
            self.matriz[i][j] = self.tipo
            chances = 0
            
            if self.matriz[i].count(self.tipo) == 2:
                chances += 1
            
            coluna = [self.matriz[0][j], self.matriz[1][j], self.matriz[2][j]]
            if coluna.count(self.tipo) == 2:
                chances += 1
            
            if i == j:
                diagonal = [self.matriz[0][0], self.matriz[1][1], self.matriz[2][2]]
                if diagonal.count(self.tipo) == 2:
                    chances += 1
            
            if i + j == 2:
                diagonal = [self.matriz[0][2], self.matriz[1][1], self.matriz[2][0]]
                if diagonal.count(self.tipo) == 2:
                    chances += 1
            self.matriz[i][j] = Tabuleiro.DESCONHECIDO
            if chances >= 2:
                return (i, j)

        # REGRA 3: Ocupar o centro
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # REGRA 4: Canto oposto ao do oponente
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for i, j in cantos:
            if self.matriz[i][j] == self.oponente:
                canto_oposto = (2 - i, 2 - j)
                if self.matriz[canto_oposto[0]][canto_oposto[1]] == Tabuleiro.DESCONHECIDO:
                    return canto_oposto

        # REGRA 5: Ocupar um canto vazio 
        cantos_vazios = []
        for i, j in cantos:
            if self.matriz[i][j] == Tabuleiro.DESCONHECIDO:
                cantos_vazios.append((i, j))
        if cantos_vazios:
        
            indice = randint(0, len(cantos_vazios) - 1)
            return cantos_vazios[indice]

        # REGRA 6: Jogada aleatória em células vazias
        if vazias:
            indice = randint(0, len(vazias) - 1)
            return vazias[indice]

        return None  # Caso não haja jogadas