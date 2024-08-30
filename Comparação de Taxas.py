import matplotlib.pyplot as plt
x=[2019,2020,2021,2022,2023]
y1=[2.5,1.8,2.0,2.2,2.4]
y2=[3.0,2.5,2.8,3.1,3.2]
plt.style.use('bmh')


plt.figure(figsize=(9, 6))
plt.title('Comparação de Taxas de Crescimento Anual')
plt.xlabel('Ano')
plt.ylabel('Taxas de crescimento anual (%)')
plt.plot(x,y1, label='ECONOMIA A')
plt.plot(x,y2, label='ECONOMIA B')
plt.legend(fontsize=13, frameon=True, framealpha=0.2, facecolor='blue')

plt.xticks(x)

plt.show()