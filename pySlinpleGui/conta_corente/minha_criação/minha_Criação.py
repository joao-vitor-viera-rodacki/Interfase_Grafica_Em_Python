import PySimpleGUI as sg

class Conta_corente :
    def __init__(self):
        #layout
        sg.change_look_and_feel('Black')
        layout = [

            [sg.Text('Nome'),sg.Input(size=(20,0),key='nome')],
            [sg.Text('saldo'),sg.Input(size=(20,0),key='saldo'),sg.Checkbox('saldo 0','saldozero',key='saldo_zero')],
            [sg.Text('Depositar'),sg.Input(size=(20,0),key='depositar_valor'),sg.Checkbox('depositar 0','depositarzero',key='depositar_zero')],
            [sg.Text('Sacar'),sg.Input(size=(20,0),key='sacado'),sg.Checkbox('sacar 0','sacarzero',key='sacar_zero')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(50,30),font=12)]
        ]

        #janela
        self.janela = sg.Window('Dados Bancarios').layout(layout)
        
    


    def list_dados(self):
        while True:
            #extraindo dos da tela
            self.button,self.values = self.janela.Read()
                

            if self.values == sg.WIN_CLOSED:
                break

            if self.values['saldo_zero'] :
                self.values['saldo'] = 0

            if self.values['depositar_zero'] :
                self.values['depositar_valor'] = 0

            if self.values['sacar_zero'] :
                self.values['sacado'] = 0
            
            sacado = float(self.values['sacado'])
            saldo = float(self.values['saldo'])
            deposito = float(self.values['depositar_valor'])
            nome = self.values['nome']
            
            
            total = saldo + deposito - sacado

            print('Dados do Usuário')
            print('-'*20)
            print(f'Nome : {nome}')
            print(f'Saldo : R${total}')
            print(f'Dinheiro Depositado R${deposito}')
            print(f'Dinheiro sacado R${sacado}')
            print('-'*20)
  


janela = Conta_corente()
janela.list_dados()
