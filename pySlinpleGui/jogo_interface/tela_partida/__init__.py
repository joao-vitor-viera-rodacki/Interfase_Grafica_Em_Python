import  PySimpleGUI as sg
from random import randint

import jogador

class Tela_partida:
    def __init__(self,jogador1,jogador2):

    


        layout = [
            [sg.T(f'O player {jogador} começa a partida')]
            ]

        self.janela_partida = sg.Window('Partida...').layout(layout)

    def atualiza_partida(self):
        while True:
            buttons , values = self.janela_partida.Read()

            if values == sg.WIN_CLOSED:
                break 