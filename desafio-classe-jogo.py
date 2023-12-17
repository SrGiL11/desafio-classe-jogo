class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = ""
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"

        print(f"O {self.tipo} atacou usando {ataque}")

# Exemplo de uso da classe Heroi
heroi_1 = Heroi("Gandalf", 200, "mago")
heroi_2 = Heroi("Thor", 35, "guerreiro")

heroi_1.atacar()
heroi_2.atacar()
