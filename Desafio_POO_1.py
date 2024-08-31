class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#TODO: Crie um método para retornar as informações formatas com Nome e Idade:
    def nome_idade(self):
        return f"Nome: {nome}, Idade: {idade}"    
    

# Entrada do usuário
nome = input()
idade = int(input())

resultado = nome.nome_idade and idade.nome_idade
print(resultado)
