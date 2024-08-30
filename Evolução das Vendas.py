import matplotlib.pyplot as plt
x=['JAN', 'FEV','MAR', 'ABR','MAI','JUN']
y1=[200,210,180,220,230,240]
y2=[150,170,160,190,200,210]

plt.style.use('bmh')
plt.title('Evolução das Vendas de Dois Produtos')
plt.xlabel('MESES')
plt.ylabel('VENDAS MENSAIS (em unidades)')
plt.plot(x,y1, label='PRODUTO X')
plt.plot(x,y2, label='PRODUTO Y')
plt.legend(fontsize=13, frameon=True, framealpha=0.2, facecolor='red')
plt.show()