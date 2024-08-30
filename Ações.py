import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10] #dia
y1=[100,102,101,103,105,106,108,107,109,110]
y2=[95,96,97,98,99,100,101,102,103,104]
plt.style.use('bmh')


plt.figure(figsize=(10, 6)) # primeiro valor =largura

plt.title('Evolução de Preços de Ações')
plt.xlabel('Dias')
plt.ylabel('Preço de fechamento (em R$)')
plt.plot(x,y1,label='AÇÃO X')
plt.plot(x,y2,label='AÇÃO Y')
plt.legend(fontsize=13, frameon=True, framealpha=0.2, facecolor='blue')

plt.xticks(x) #força a aparecer todos os valores de X

plt.show()
#figsize para diminuir ou aumentar o tamanho do grafico e caber todos os numeros