import PySimpleGUI as sg

class Interfase :
    def __init__(self):
        self.produtos = {'bolacha' : 'bolacha',
                        'leite' : 'leite' 
                        }
        layuot = [
            [sg.Text('testando'),sg.Input(size=(20,0))],
            [self.filtraItens()]
        ]

        #janela
        self.janela_usuario = sg.Window('Dados Bancarios').layout(layuot)
    
    def update_usuario(self):
        while True:
            #extraindo dados em tempo real do layout
            self.botton, self.values = self.janela_usuario.read()
            if self.values == sg.WIN_CLOSED:
                break


    def filtraItens (self):
        for item in self.produtos.keys():
            print(item)

'''
    def list_produtos (self):
        layout = [
            [sg.T('Lista de produtos')],
           ]
'''
        self.janela_produtos = sg.Window('Lista').layout(layout)

    def update_listaPrecos (self):
        while True: 
            button , values = self.janela_produtos.Read()

            if values == sg.WINDOW_CLOSED:
                break
janela = Interfase()
janela.list_produtos()
janela.update_listaPrecos()

janela.update_usuario()
#---------------------

