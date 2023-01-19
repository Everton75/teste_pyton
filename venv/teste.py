print("\x1b[2J\x1b[1;1H") # este codigo limpa a tela

convidados = []
convidados.append('amanda')
convidados.append('ana amélia')
convidados.append('amanda')



print(convidados[0].title() + '\tvenha na festa')
print(convidados[1].title() + ' venha na festa')
print(convidados[2].title() + '\tvenha na festa')
print(convidados[1].title() + ' não vai comparecer afesta')
del convidados[2]
print(convidados)
