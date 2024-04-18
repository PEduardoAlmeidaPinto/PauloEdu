menu = '''

=================

Bem vindo ao sistema básico de cálculo para veículos!
Abaixo escolha as opções que deseja!

[1] Custo por KM 
[2] Custo por Deslocamento (Ida e Volta)
[3] Sair


=================
'''

custo_por_km = 0

while True:
    show = int(input(menu))

    if show == 1:
        preco = float(input("Qual o preço atual da gasolina? "))
        consumo = float(input("Qual o consumo médio do veículo? "))
        custo_por_km = preco / consumo
        print(f"O consumo por KM do seu veículo é R${custo_por_km:.2f}")

    elif show == 2:
        if custo_por_km != 0:
            ida = float(input("Qual a Km de deslocamento da sua casa até o destino? "))
            volta = float(input("Qual a Km de deslocamento do destino até sua casa? "))
            total = ida + volta
            custo_dia = custo_por_km * total
            print(f"O seu custo de KM diário é de R$ {custo_dia:.2f}")
        else:
            print("Por favor, primeiro calcule o custo por KM.")

    elif show == 3:
        break



    












