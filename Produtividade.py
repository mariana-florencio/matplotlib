import matplotlib.pyplot as plt
x=['SEG', 'TER', 'QUA', 'QUI', 'SEX']
y1=[120,130,125,140,135]
y2=[110,115,120,130,125]
plt.style.use('bmh')

plt.title('Variação da Produtividade Semanal')
plt.xlabel('Dias da semana')
plt.ylabel('Produtividade (em unidades produzidas)')
plt.plot(x,y1,label='Semana 1')
plt.plot(x,y2, label='Semana 2')
plt.legend(fontsize=13, frameon=True, framealpha=0.2, facecolor='red')
plt.show()