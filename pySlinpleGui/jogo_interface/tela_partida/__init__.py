import  PySimpleGUI as sg
from random import randint
from time import sleep

def animação():
    for i in range(0,8):
        print('_ _ _',end='')
        sleep(0.10)


class Tela_partida:
    def __init__(self ,player1 ,player2):
        
        sg.theme('DarkBrown2')

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
                self.partida(self.player1.nome)
         
                
    def partida(self,player_atacante):
        
        self.player_atacante = player_atacante

        layout = [
            [sg.T(f'O player {self.player_atacante} começa a partida')],
            [sg.Radio('Ataque Ariscado','ataque',key='ataque_ariscado')],
            [sg.Radio('Ataque Magico De Gelo','ataque',key='ataque_magico_de_gelo')],
            [sg.Radio('Ataque Especial','ataque',key='ataque_especial')],
            [sg.Button('>>confirmar')],
            [sg.T(f'player {self.player1.nome} HP: {self.player1.hp}')],
            [sg.T(f'player {self.player2.nome} HP: {self.player2.hp}')],
            [sg.Output(size=(40,10))]
            ]
         
        self.janela_partida = sg.Window('Partida em andamento').layout(layout)

        self._atualiza_partida()


    def _atualiza_partida(self):
        
        while True:
            buttons , values = self.janela_partida.Read()
            
            if values == sg.WINDOW_CLOSED:
                break
            if buttons:
                if self.player_atacante == self.player1.nome:
                    
                    
                    dano = self.player1.ataque_player(self.player2,values)
                    
                    print(f'{self.player1.nome} infligiu {dano} de dano em {self.player2.nome}'), animação()
                    sleep(2)
                    layout = [
                        [sg.T(f'O player {self.player_atacante} começa a partida')],
                        [sg.Radio('Ataque Ariscado','ataque',key='ataque_ariscado')],
                        [sg.Radio('Ataque Magico De Gelo','ataque',key='ataque_magico_de_gelo')],
                        [sg.Radio('Ataque Especial','ataque',key='ataque_especial')],
                        [sg.Button('>>confirmar')],
                        [sg.T(f'player {self.player1.nome} HP: {self.player1.hp}')],
                        [sg.T(f'player {self.player2.nome} HP: {self.player2.hp}')],
                        [sg.Output(size=(40,10))],
                        ]
                    
                    self.janela_partida.close()
                    

                    self.janela_partida = sg.Window('Partida em andamento').layout(layout)
                    
                    self.player_atacante = self.player2.nome

                    
                elif self.player_atacante == self.player2.nome:
                                         
                    
                    dano = self.player2.ataque_player(self.player1,values)
                    
                    print(f'{self.player2.nome} infligiu {dano} de dano em {self.player1.nome}'), animação()
                    sleep(2)
                    layout = [
                        [sg.T(f'O player {self.player_atacante} começa a partida')],
                        [sg.Radio('Ataque Ariscado','ataque',key='ataque_ariscado')],
                        [sg.Radio('Ataque Magico De Gelo','ataque',key='ataque_magico_de_gelo')],
                        [sg.Radio('Ataque Especial','ataque',key='ataque_especial')],
                        [sg.Button('>>confirmar')],
                        [sg.T(f'player {self.player1.nome} HP: {self.player1.hp}')],
                        [sg.T(f'player {self.player2.nome} HP: {self.player2.hp}')],
                        [sg.Output(size=(40,10))]
                        ]
                    
                    self.janela_partida.close()
                    

                    self.janela_partida = sg.Window('Partida em andamento').layout(layout)
                    
                    self.player_atacante = self.player1.nome
                    print(dano)
                
    