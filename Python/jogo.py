
pino1 = ['CCC','BBB','AAA']
pino2 = []
pino3 = []
print('Pino 1', pino1)
print('Pino 2', pino2)
print('Pino 3', pino3)
for pinos in range(12):
     
    spino = int(input('Qual pino deseja movimentar ?'))
    item = input('Qual item deseja movimentar ?')
    epino = int(input('Para qual pino deseja movimentar o item ' + item '?'))
    if spino == 1:
        pino1.remove(item)
    elif spino == 2:
        pino2.remove(item)
    elif spino == 3:
        pino3.remove(item)
    if epino == 1: 
        pino1 = pino1 + [item]
    elif epino == 2:
        pino2 = pino2 + [item]
    elif epino == 3:
        pino3 = pino3 + [item]
    print('Pino 1', pino1)
    print('Pino 2', pino2)
    print('Pino 3', pino3)
    print('\n_______________________________________________________')
    print('\nPasso número: ', pinos,'\n_______________________________________________________')
   

