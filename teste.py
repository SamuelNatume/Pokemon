import random

# Listas de Pokémon por ambiente
caverna = ["Zubat", "Geodude", "Onix"]
mato = ["Weedle", "Caterpie", "Bellsprout"]

# Variáveis de probabilidade de captura
prob_capt_mato = 0.5
prob_capt_caverna = 0.0000000000000001

# Pokédex do jogador
pokedex = []

# Número máximo de tentativas extras de captura
max_tentativas_extras = 3
tentativas_extras = 0

print("-" * 60)
print("                            | MUNDO POKÉMON |")
print("-" * 60)
print("Olá!\nÉ um prazer conhecê-lo(a)!\nBem-vindo ao fabuloso mundo POKéMON!\nMeu nome é CARVALHO!\nMas todos aqui me chamam de PROFESSOR OAK.\nEste mundo é habitado por várias criaturas chamadas de POKéMON.\nMas primeiro, me fale um pouco sobre você!\nAgora diga-me.")

# Introdução do Professor Carvalho e nome do jogador
while True:
    try:
        genero = int(input("[1] Garoto\n[2] Garota\nVocê é um garoto ou uma garota? "))

        if genero == 1:
            print("Olá garoto!")
            break

        elif genero == 2:
            print("Olá garota!")
            break

        if genero < 1 or genero > 2:
            print("Escolha a opção 1 ou 2 ,Tente novamente!")

    except ValueError:
        print("Escolha a opção 1 ou 2 ,Tente novamente!")

while True:
    nome = input("Como se chama? ")

    if not nome or not nome.isalpha():
        print("Por favor, insira um nome válido.")

    else:
        print(f"Certo, {nome}!\nA sua própria lenda POKéMON está prestes a começar!\nUm mundo de sonhos e aventuras o aguarda! Então, vamos lá!")
        break

# Loop principal do jogo
while True:
    print("Essas são suas escolhas!")
    print('''
    [1] Caverna
    [2] Mato
    [3] Mostrar Pokédex
    [4] Sair      
    ''')
    escolha = int(input("Escolha uma opção: "))

    # Sair do jogo
    if escolha == 4:
        print(f"Até logo {nome}!\nEspero te reencontrar novamente.")
        break

    # Exploração da caverna
    elif escolha == 1:
        pokemon_aleatorio = random.choice(caverna)
        print(f"Você entrou na caverna e encontrou um {pokemon_aleatorio}!")
        if pokemon_aleatorio in pokedex:
            print(f"Você já capturou o {pokemon_aleatorio}!")
        else:
            resposta = input("Deseja tentar capturar esse pokémon (S/N)? ")
            if resposta.lower() == "s":
                if random.random() <= prob_capt_caverna:
                    pokedex.append(pokemon_aleatorio)
                    print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                else:
                    while tentativas_extras < max_tentativas_extras:
                        resposta2 = input("O Pokémon escapou! Quer tentar capturar novamente (S/N)? ")
                        if resposta2.lower() == "s":
                            tentativas_extras += 1
                            if random.random() <= prob_capt_caverna:
                                pokedex.append(pokemon_aleatorio)
                                print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                                break
                            else:
                                print(f"O {pokemon_aleatorio} escapou novamente!")
                        elif resposta2.lower() == "n":
                            break
                        else:
                            print("Opção inválida. Por favor, digite S para sim ou N para não.")
            elif resposta.lower() == "n":
                continue
            else:
                print("Opção inválida. Por favor, digite S para sim ou N para não.")

    # Exploração do mato
    elif escolha == 2:
        pokemon_aleatorio = random.choice(mato)
        print(f"Você está adentrando o mato e encontrou um {pokemon_aleatorio}!")
        if pokemon_aleatorio in pokedex:
            print(f"Você já capturou o {pokemon_aleatorio}!")
        else:
            resposta = input("Deseja tentar capturar esse pokémon (S/N)? ")
            if resposta.lower() == "s":
                if random.random() <= prob_capt_mato:
                    pokedex.append(pokemon_aleatorio)
                    print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                else:
                    while tentativas_extras < max_tentativas_extras:
                        resposta2 = input("O Pokémon escapou! Quer tentar capturar novamente (S/N)? ")
                        if resposta2.lower() == "s":
                            tentativas_extras += 1
                            if random.random() <= prob_capt_mato:
                                pokedex.append(pokemon_aleatorio)
                                print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                                break
                            else:
                                print(f"O {pokemon_aleatorio} escapou novamente!")
                        elif resposta2.lower() == "n":
                            break
                        else:
                            print("Opção inválida. Por favor, digite S para sim ou N para não.")
            elif resposta.lower() == "n":
                continue
            else:
                print("Opção inválida. Por favor, digite S para sim ou N para não.")

    # Mostrar Pokédex
    elif escolha == 3:
        print("===POKÉDEX===")
        if not pokedex:
            print("Sua Pokédex está vazia.")
        else:
            for pokemon_cap in pokedex:
                print(f"- {pokemon_cap}")

    else:
        print("Escolha incorreta, digite novamente!")
