import  PySimpleGUI as sg
from random import randint


class Tela_partida:
    def __init__(self ,player1 ,player2):

        self.player1 = player1
        self.player2 = player2

        layout = [ 
            [sg.T(f'Começar partida de {player1.nome} contra {player2.nome}')],
            [sg.Button('>>Começar')],
            [sg.Button('>>sair')]
        ]

        self.janela_partida = sg.Window('Dando inicio a partida').layout(layout)
        self._atualiza()


    def _atualiza(self):
        while True:
            buttons , values = self.janela_partida.Read()

            if values == sg.WIN_CLOSED:
                break 
            
            if buttons == '>>sair' :
                break
            
            if buttons == '>>Começar':
                self.janela_partida.close()
                self.partida()
         
                
    def partida(self):
                
        layout = [
            [sg.T(f'O player {self.player1.nome} começa a partida')],
            [sg.Radio('Ataque Ariscado','ataque',key='ataque_ariscado')],
            [sg.Radio('Ataque Magico De Gelo','ataque',key='ataque_magico_de_gelo')],
            [sg.Radio('Ataque Especial','ataque',key='ataque_especial')],
            [sg.Button('>>confirmar')]
            ]
         
        self.janela_partida = sg.Window('Partida em andamento').layout(layout)

    def _atualiza_partida(self):
        
        while True:
            buttons , values = self.janela_partida.Read()
            
            if values == sg.WINDOW_CLOSED:
                break
                
                
                
    