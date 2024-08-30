import matplotlib.pyplot as plt
x=['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB', 'DOM']
y=[32,34,33,31,30,29,28]
plt.title('Variação da Temperatura Diária ao Longo de Uma Semana')
plt.xlabel('DIAS DA SEMANA')
plt.ylabel('TEMPERATURA(ºC)')
plt.plot(x,y, marker='o', linewidth=2, color='blue')
plt.show()