from random import sample

print("\x1b[2J\x1b[1;1H") # este codigo limpa a tela

population = []
sample_size = 6
tam_lista=0
prompt = "\nDigite os números que você quer jogar"
prompt += "\n"
while True:
    city = input(prompt)
    if city == 'quit':
        if tam_lista >= 6:
            sample_elements = sample(population, sample_size)
            sample_elements.sort() #ordena a lista
            print(sample_elements)
            break
        else:
            print("\x1b[2J\x1b[1;1H") # este codigo limpa a tela
            print("\nA lista precisa de mais de 6 números")
            print("  para realizar o sorteio\n")
            break

    else:
        population.append(int(city)) #problema aqui se digitar algo diferente  de inteiro
        tam_lista=len(population)
        print(population)
