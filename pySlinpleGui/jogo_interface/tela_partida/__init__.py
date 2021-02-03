import  PySimpleGUI as sg
from random import randint


class Tela_partida:
    def __init__(self,player):
       
    
        layout = [
            [sg.T(f'O player {player.nome} começa a partida')],
            [sg.Radio('Ataque Ariscado','ataque',key='ataque_ariscado')],
            [sg.Radio('Ataque Magico De Gelo','ataque',key='ataque_magico_de_gelo')],
            [sg.Radio('Ataque Especial','ataque',key='ataque_especial')],
            [sg.Button('>>>>confirmar')]
            ]

        self.janela_partida = sg.Window('Partida...').layout(layout)

    def atualiza_partida(self,player):
        while True:
            buttons , values = self.janela_partida.Read()

            if values == sg.WIN_CLOSED:
                break 

