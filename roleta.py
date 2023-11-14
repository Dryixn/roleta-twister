from random import randint

r = 'sim'

#              0              1             2               3
partes = ['pé esquerdo', 'pé direito', 'mão direita', 'mão esquerda']
cores = ['azul', 'vermelha', 'amarela', 'verde']
#           0         1         2           3

print('-' * 40)
while r == 'sim':
    p = randint(0, len(partes) - 1)
    c = randint(0, len(cores) - 1)  
    while True:
        r = str(input('Pode sortear? ')).lower().strip()
        if r in 'simnãonao':
            break
        else:
            print('Só aceita \033[1mSIM\033[m ou \033[1mNÃO\033[m. Tente novamente.')
    if r in 'sim':
        print('-' * 30)
        print(f'Coloque o(a) {partes[p]} na cor {cores[c]}')
        print('-' * 30)      
print('-' * 40)
