class Campeao: 
    def __init__(self, nome, vida, defesa):
        self.nome = nome
        self.__vida = vida
        self.ataque = defesa

    def atacar(self):
        print(f"{self.nome} ataca causando {self.ataque} de dano.")

    def receber_dano(self, dano):
        self.__vida -= dano
        print(f"{self.nome} recebe {dano} de dano e agora tem {self.__vida} de vida.")

    def mostrar_vida(self):
        print(f"{self.nome} tem {self.__vida} de vida.")


class Ashe(Campeao):
    def __init__(self, nome, vida, ataque, flecha_congelante):
        super().__init__(nome, vida, ataque)
        self.flecha_congelante = flecha_congelante

    def usar_flecha_congelante(self):
        print(f"{self.nome} usa Flecha Congelante, causando {self.flecha_congelante} de dano e congelando o inimigo!")


class Garen(Campeao):
    def __init__(self, nome, vida, ataque, golpe_demaciano):
        super().__init__(nome, vida, ataque)
        self.golpe_demaciano = golpe_demaciano

    def usar_golpe_demaciano(self):
        print(f"{self.nome} usa Golpe Demaciano, causando {self.golpe_demaciano} de dano!")


# Função para escolher o ataque
def escolher_ataque(campeao):
    if isinstance(campeao, Ashe):
        ataque = input("Escolha o ataque: '1' para ataque básico ou '2' para Flecha Congelante: ")
        if ataque == '1':
            campeao.atacar()
        elif ataque == '2':
            campeao.usar_flecha_congelante()
        else:
            print("Opção inválida.")

    elif isinstance(campeao, Garen):
        ataque = input("Escolha o ataque: '1' para ataque básico ou '2' para Golpe Demaciano: ")
        if ataque == '1':
            campeao.atacar()
        elif ataque == '2':
            campeao.usar_golpe_demaciano()
        else:
            print("Opção inválida.")

# Criando campeões específicos com habilidades próprias
ashe = Ashe("Ashe", 500, 60, 120)
garen = Garen("Garen", 800, 70, 150)

# Exemplo de uso com o usuário escolhendo os ataques
print("Ataques para Ashe:")
escolher_ataque(ashe)
print("\nAtaques para Garen:")
escolher_ataque(garen)
