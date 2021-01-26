from random import randint
import PySimpleGUI as sg

import tela_partida


DEFAULT_ATK =  {
    'Ataque Especial': 300,
    'Ataque Ariscado': 200,
    'Ataque Magico De Gelo': 100
}


class Jogador :
    def __init__(self , nome):
        
        self.level = 6
        self.xp = 0
        self.dano  = (self.level // 2) * 10
        self.usu_dano_max = self.dano + 10
        self.usu_dano_min = self.dano

        self.habilidades = DEFAULT_ATK
       
        self.botões_habilidades = { '1' : 'Ataque Ariscado',
                                   '2' : 'Ataque Magico De Gelo',
                                   '3' : 'Ataque Especial'}

        self.pontos_de_habilidades = 10
        self.hp = (self.level // 2) * 500
        self.nome = nome
        self.contagem_de_atake_especial = 2


class Tela  :

    
    def __init__(self):
        layout = [
            [sg.T(f'Seja bem vindo ao meu jogo -- {self.nome} --')],
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
        
        janela_partida = tela_partida.Tela_partida()
        janela_partida.atualiza_partida()

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
            
            

jogo = Tela()
jogo.tela_menu()




