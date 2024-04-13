import random
caverna = ["Zubat", "Geodude", "Aaron", "Onix"]
mato = ["Weedle", "Caterpie", "Metapod", "Bellsprout"]
pokedex=[]
print("Oi, olá!\nÉ um prazer conhecê-lo!\nBem-vindo ao fabuloso mundo POKéMON!\nMeu nome é CARVALHO!\nMas todos aqui me chamam de PROFESSOR OAK.\nEste mundo...,\n...é habitado por várias criaturas chamadas de POKéMON.\nMas primeiro, me fale um pouco sobre você!\nAgora diga-me.")
while True:
    try:
        genero = int(input("Digite 1 para garoto \nDigite 2 para garota\nVocê é um garoto ou uma garota?: "))

        if genero == 1:
            print("Olá garoto!")
            break

        elif genero == 2:
            print("Olá garota!")
            break

        if genero < 1 or genero > 2:
            print("Escolha entre 1 ou 2! Tente novamente!")

    except ValueError:
        print("Escolha entre 1 ou 2! Tente novamente!")

print("Começaremos com o nome...")

while True:
    nome = input("Como se chama? ")

    if not nome or not nome.isalpha():
        print("Por favor, insira um nome válido.")

    else:
        print(f"Certo, {nome}!\nA sua própria lenda POKéMON está prestes a começar!\nUm mundo de sonhos e aventuras o aguarda! Então, vamos lá!")
        break

print("Caminhos que podem ser percorridos!")
print('''[1] Caverna
[2] Mato
[3] Mostrar Pokedex
[4] Sair      ''')
while True:
    escolha = int(input("Escolha um caminho: "))
    if escolha==4:
        print("Encerrando...")
        break
    if escolha <=0 or escolha >3:
        print("Caminho incorreto, tente novamente!")
        continue
    if escolha ==1:
        while True:
            pokemon_aleatorio=random.choice(caverna)
            print(f"Você entrou no caverna e encontrou um {pokemon_aleatorio}!")
            resposta=input("Deseja capturar esse pokémon (S/N)")
            if resposta=="S" or resposta=="s":
                pokedex.append(pokemon_aleatorio)
                print(f"Você capturou o {pokemon_aleatorio}")
                break
            elif resposta=="N" or resposta=="n":
                break
            else:
                continue
    elif escolha ==2:
        while True:
            print("Você está adentrando o mato...")
            pokemon_aleatorio=random.choice(mato)
            print(f"Você entrou no mato e encontrou um {pokemon_aleatorio}!")
            resposta=input("Deseja capturar esse pokémon (S/N)")
            if resposta=="S" or resposta=="s":
                pokedex.append(pokemon_aleatorio)
                print(f"Você capturou o {pokemon_aleatorio}")
                break
            elif resposta=="N" or resposta=="n":
                break
            else:
                continue
    elif escolha==3:
        print("Você decidiu listar seus pokémons na Pokédex...")
        print(f"Esses são os seus pokémons no momento: {pokedex}")
        continue


