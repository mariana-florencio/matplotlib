import matplotlib.pyplot as plt
x=['JAN','FEV', 'MAR', 'ABR', 'MAI', 'JUN', ]
y=[120,85, 95,70,50,40]
plt.style.use('bmh')
plt.plot(x,y, marker='*', linewidth=2, color='red')
plt.title('Variação de Precipitação ao Longo do Ano')
plt.xlabel('MESES')
plt.ylabel('precipitação mensal (em mm)')
plt.show()