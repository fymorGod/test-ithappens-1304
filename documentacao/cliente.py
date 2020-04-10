class Cliente:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
    def __str__(self):
        return "Nome do Cliente: "+self.nome+"\nCPF Cadastrado: "+str(self.cpf)+"."