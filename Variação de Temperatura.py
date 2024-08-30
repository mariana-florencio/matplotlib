from matplotlib import pyplot as plt
x=['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN']
y=[25,27,30,28,24,22]
plt.style.use('bmh')

plt.plot(x,y, marker='o', linewidth=2, color='green')
plt.title('Variação de temperartura ao longo do ano')
plt.xlabel('MESES')
plt.ylabel('TEMPERATURA MÉDIAºC')
plt.show()