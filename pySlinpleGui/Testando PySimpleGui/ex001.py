import PySimpleGUI as sg



class Window :
    def __init__(self,nome):
        self.nome = nome
        layout = [
            [sg.T('Testando'),sg.In(size=(20,0),key='IN')],
            
        ]

        self.janela = sg.Window(self.nome).layout(layout)

    def list_dados(self):
        while True:
          
                
                botton , values = self.janela.Read()

                if values != None :
                    sg.popup(f'você  digitou {values["IN"]}')
                if values ==  sg.WIN_CLOSED:
                    break

janela = Window('joão')
janela.list_dados()