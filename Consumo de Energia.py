import matplotlib.pyplot as plt
x= ["00:00", "06:00", "12:00", "18:00", "21:00", "23:59"]
y=[0.5, 1.2, 2.0, 2.5, 1.8, 1.0]

plt.style.use('bmh')

plt.title('Consumo de Energia ao Longo do Dia')
plt.xlabel('Horário')
plt.ylabel('Consumo(kWh)')
plt.plot(x,y, marker='o', linewidth=2, color='blue')
#plt.yticks(y) ->grafico não ficou bom com esse comando
plt.show()