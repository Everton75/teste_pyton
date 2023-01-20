from random import sample

print("\x1b[2J\x1b[1;1H") # este codigo limpa a tela

population = []
sample_size = 6
tam_lista=0
prompt = "Digite os números que você quer jogar"
prompt += "\n"
while True:
    city = input(prompt)
    if city == 'quit':
        if tam_lista >= 6:
            sample_elements = sample(population, sample_size)
            sample_elements.sort() #ordena a lista
            print(sample_elements)
            print(len(sample_elements)) # é para saber o tamanho da lista
            
            break
        else:
            print("\x1b[2J\x1b[1;1H") # este codigo limpa a tela
            print("\nA lista precisa de mais de 6 números")
            print("  para realizar o sorteio\n")
            break

    else:
        if not city.isdigit():
            print("Digite apenas números inteiros")
        else:
            if (int(city)) in population:
                print("Você já digitou este número!")
            else:     
                population.append(int(city)) #problema aqui se digitar ponto, virgula, olhar metodo isdigit():
                tam_lista=len(population)
                print(population)


  
