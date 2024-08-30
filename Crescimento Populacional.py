import matplotlib.pyplot as plt
x=[2020,2021,2022,2023,2024]
y1=[500,520,540,560,580]
y2=[450,460,470,490,510]

plt.style.use('bmh')
plt.title('Crescimento Populacional em Duas Cidades')
plt.xlabel('Ano')
plt.ylabel('População (em milhares)')

plt.plot(x, y1, label='CIDADE A')
plt.plot(x, y2, label='CIDADE B')
plt.xticks(x)#para manter os elementos da lista X
plt.legend(fontsize=13, frameon=True,framealpha=0.2, facecolor='green')
plt.show()