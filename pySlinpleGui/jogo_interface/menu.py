from random import randint
import PySimpleGUI as sg

import tela_partida
import jogador



class Tela  : 
 
    def __init__(self,player1,player2):


        layout = [
            [sg.T(f'Seja bem vindo ao meu jogo ')],
            [sg.Radio('Enter the match','entrar',key='entrar_1')],
            [sg.Radio('Enter the player status','entrar',key='entrar_2')],
            [sg.Radio('Enter the evolution tree','entrar',key='entrar_3')],
            [sg.Button('Next >>')]
        ]
    
        self.janela_menu = sg.Window('MY GAME').layout(layout)
        
        self._atualiza_menu()

    def tela_habilidades(self):
       pass
        
    def tela_partida(self):
        
        sg.Window.close(self.janela_menu)
        
        janela_partida = tela_partida.Tela_partida(player1 ,player2)
        
    def tela_statusJogador(self):
        pass
    


    def _atualiza_menu (self):
        while True:
            buttons , values = self.janela_menu.Read()
          

            if values == sg.WIN_CLOSED:
                break

            if values['entrar_1'] :
                self.tela_partida()
            
            if values['entrar_2']:
                self.tela_statusJogador()
 
            if values['entrar_3']:
                self.tela_habilidades()
            
player1 = jogador.Jogador('joão')
player2 = jogador.Jogador('lucas')

tela = Tela(player1 ,player2)
            





