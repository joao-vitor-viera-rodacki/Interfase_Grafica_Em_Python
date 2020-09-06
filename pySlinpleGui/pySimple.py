import PySimpleGUI as sg

class Telapython :
    def __init__(self):
        #sg.theme_previewer()
        sg.change_look_and_feel('darkbrown2')
        #layout
        
        layout = [
            
            [sg.Text('Nome',size=(5,0)), sg.Input(size=(10,0),key='Nome')],
            [sg.Text('Idade',size=(5,0)), sg.Input(size=(10,0),key='Idade')],
            
            [sg.Text('Quais provedores de e-mail são aceitos ?')],
            [sg.Checkbox('Gmai',key='Gmail'), sg.Checkbox('Outlook',key='Outlook'), sg.Checkbox('Yahoo',key='Yahoo')],
            
            [sg.Text('Você aceita cartão ?')],
            [sg.Radio('Aceito','cartão',key='cartao_sim'),sg.Radio('Não aceito','cartão',key='cartao_nao')],
            [sg.Button('Enviar Dados',size=(20,0))],
            [sg.Text('Velocidade de Script')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(30,20),key='velocidade_slider')],    
            [sg.Output(size=(30,20))]
        ]

        #janela
        self.janela = sg.Window('Dados do Usuário').layout(layout)
    
       

    def iniciar(self):
        while True:
        
            #extrair os dados da tela
            self.Button_dados , self.values = self.janela.Read()

            nome = self.values['Nome']
            idade = self.values['Idade']
            aceita_gmail = self.values['Gmail']
            aceita_outlook = self.values['Outlook']
            aceita_yahoo = self.values['Yahoo']
            cartao_sim = self.values['cartao_sim']
            cartao_nao = self.values['cartao_nao']
            velocidade_script = self.values['velocidade_slider']

            print(f'Dados do Usuário')
            print('-'*16)
            print(f'nome : {nome}')
            print(f'idade : {idade}')
            print(f'Gmail : {aceita_gmail}')
            print(f'Outlook : {aceita_outlook}')
            print(f'Yahoo : {aceita_yahoo}')
            
            if cartao_sim:
                print(f'cartão_sim : {cartao_sim}')

            else:
                print(f'cartão_não : {cartao_nao}')    
            print(f'velocidade script : {velocidade_script}')
            
            print('-'*16)

tela = Telapython()
tela.iniciar()
