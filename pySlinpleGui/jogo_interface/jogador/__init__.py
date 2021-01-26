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

joao = Jogador('joao')
gui = Jogador('gui')