from random import randint

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

        self.habilidades = DEFAULT_ATK
       
        self.botões_habilidades = { '1' : 'ataque_ariscado',
                                   '2' : 'ataque_magico_de_gelo',
                                   '3' : 'ataque_especial'}

        self.hp = (self.level // 2) * 500
        self.nome = nome
        self.contagem_de_atake_especial = 2

    def ataque_player(self,player_inimigo ,tipo_ataque):
        if tipo_ataque['ataque_ariscado'] == True:
            dano = randint(0 ,self.dano)
            player_inimigo.hp -= dano
            return dano
        
        if tipo_ataque['ataque_magico_de_gelo'] == True:
            dano = randint(10,self.dano)
            player_inimigo.hp -= dano
            return dano

        if tipo_ataque['ataque_especial'] == True:
            if self.contagem_de_atake_especial == 0 :
                return False    
            self.contagem_de_atake_especial -= 1 
            dano = randint(100,200)
            player_inimigo.hp -= dano
            return dano

