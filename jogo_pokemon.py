import random

caverna = ["Zubat", "Geodude", "Aaron", "Onix"]
mato = ["Weedle", "Caterpie", "Metapod", "Bellsprout"]
pokedex = []
prob_capt_mato = 0.5
prob_capt_caverna = 0.35
chances_captura_extra = 3

print(60 * "-")
print("                            |MUNDO POKÉMON|")
print(60 * "-")
print("Olá!\nÉ um prazer conhecê-lo(a)!\nBem-vindo ao fabuloso mundo POKéMON!\nMeu nome é CARVALHO!\nMas todos aqui me chamam de PROFESSOR OAK.\nEste mundo é habitado por várias criaturas chamadas de POKéMON.\nMas primeiro, me fale um pouco sobre você!\nAgora diga-me.")

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

while True:
    try:
        print("Essas são suas escolhas!")
        print('''
[1] Caverna
[2] Mato
[3] Mostrar Pokédex
[4] Sair      ''')
        escolha = int(input("Escolha uma opção: "))

        if escolha == 4:
            print(f"Até logo {nome}!\n Espero te reencontrar novamente.")
            break

        if escolha <= 0 or escolha > 4:
            print("Escolha incorreta, digite novamente!")
            continue

        if escolha == 1:
            while True:
                if chances_captura_extra == 0:
                    print("Você usou todas as suas chances extras de captura.")
                    break

                pokemon_aleatorio = random.choice(caverna)
                print(f"Você entrou na caverna e encontrou um {pokemon_aleatorio}!")
                resposta = input("Deseja tentar capturar esse pokémon? (S/N): ")

                if resposta.upper() == "S":
                    if random.random() <= prob_capt_mato:
                        pokedex.append(pokemon_aleatorio)
                        print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                        break
                    else:
                        chances_captura_extra -= 1
                        print(f"O {pokemon_aleatorio} escapou!")
                        if chances_captura_extra > 0:
                            print(f"Você ainda tem mais {chances_captura_extra} chances extras de captura.")
                        else:
                            print("Você usou todas as suas chances extras de captura.")

                elif resposta.upper() == "N":
                    break

                else:
                    continue

        elif escolha == 2:
            while True:
                if chances_captura_extra == 0:
                    print("Você usou todas as suas chances extras de captura.")
                    break

                print("Você está adentrando o mato...")
                pokemon_aleatorio = random.choice(mato)
                print(f"Você entrou no mato e encontrou um {pokemon_aleatorio}!")
                resposta = input("Deseja tentar capturar esse pokémon? (S/N): ")

                if resposta.upper() == "S":
                    if random.random() <= prob_capt_caverna:
                        pokedex.append(pokemon_aleatorio)
                        print(f"Parabéns!\nVocê capturou o {pokemon_aleatorio}!")
                        break
                    else:
                        chances_captura_extra -= 1
                        print(f"O {pokemon_aleatorio} escapou!")
                        if chances_captura_extra > 0:
                            print(f"Você ainda tem {chances_captura_extra} chances extras de captura.")
                        else:
                            print("Você usou todas as suas chances extras de captura.")

                elif resposta.upper() == "N":
                    break

                else:
                    continue

        elif escolha == 3:
            for pokemon_cap in pokedex:
                print(f"===POKÉDEX===\n -{pokemon_cap}\n======")
                continue

    except ValueError:
        print("Escolha inválida, tente novamente!")
