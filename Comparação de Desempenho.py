import matplotlib.pyplot as plt

x=['P1', 'P2', 'P3', 'P4', 'P5']
y1=[7.5,8,7,8.5,9]
y2=[8,7.5,7.8,8.2,8.5]
plt.style.use('bmh')

plt.title('Comparação de Desempenho Acadêmico')
plt.xlabel('Provas')
plt.ylabel('Notas médias')
plt.plot(x,y1,label='Aluno A')
plt.plot(x,y2,label='Aluno B')
plt.legend(fontsize=13, frameon=True, framealpha=0.2, facecolor='red')
plt.show()