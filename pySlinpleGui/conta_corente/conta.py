import pygame as game
from PySimpleGUI import PySimpleGUI as sg
game.init()

game.mixer.music.load('./musica.mp3')
game.mixer.music.play(-1)

class Janela_login:
    def __init__(self):
        sg.change_look_and_feel('Black')
        layout = [
            [sg.Text('Nome'),sg.Input(key='nome',size=(20,0))],
            [sg.Text('Senha'),sg.Input(key='senha',size=(20,0),password_char='*')],
            [sg.Button('Entrar')],
          
        ]

        self.window = sg.Window('Login').layout(layout)

    def update(self):
        while True:
            self.button , self.values = self.window.Read()
            self.nome = self.values['nome']

            if self.values == sg.WINDOW_CLOSED:
                break
            if self.button == 'Entrar': 
                break
        self.window.close()
        conta = Conta_corente(self.values['nome'])
        conta.update()
                

class Conta_corente:
    def __init__(self, nome):
        self.money_current = 0
        self.nome = nome
        
        self.layout = [
            #[sg.Output(size=(30,10))],
            [sg.Text(f'your account : {window.nome}')],
            [sg.Text(f'your money current {self.money_current}')],
            [sg.Text('Depositar'),sg.Input(key='depositado',size=(20,0))],
            [sg.Text('Sacar : '),sg.Input(key='sacar',size=(20,1))],
            [sg.Button('Validar')]
        ]

        self.window = sg.Window('Conta_Conrente').layout(self.layout)
    
    def update(self):
        
        while True:
            #fechando janela
            self.window.close()

            #colocando uma janela atualizada 
            self.layout = [
            #[sg.Output(size=(30,10))],
            [sg.Text(f'your account : {window.nome}')],
            [sg.Text(f'your money current {self.money_current}')],
            [sg.Text('Depositar'),sg.Input(key='depositado',size=(20,0))],
            [sg.Text('Sacar : '),sg.Input(key='sacar',size=(20,1))],
            [sg.Button('Validar')]
            ]
            self.window = sg.Window('Conta_Conrente').layout(self.layout)
            self.button , self.values = self.window.Read()

            print(self.money_current)
            if self.button == sg.WINDOW_CLOSED:
                break
            self.validar()
                

    def validar(self):
        if self.button == 'Validar':
            print(self.values)
                
            if self.values['depositado'] == '':
                self.values['depositado'] = 0

            else:
                depositado = float(self.values['depositado'])
                
                self.depositar(depositado)


            if self.values['sacar'] == '':
                self.values['sacar'] = 0

            else:
                sacado = float(self.values['sacar'])
                self.sacar(sacado)

            self.layout[1][0] = sg.Text(f'your money current {self.money_current}') 

    def sacar(self, valor):
        self.money_current -= valor
        return

    def depositar(self, valor):
        self.money_current += valor
        return 






window = Janela_login()
window.update()