import random

notes_list = ['1G','1A','1B','C','D','E','F','G','A','B','C1','D1','E1','F1','G1','A1','B1','C2','D2']

#normal 3->14(+1)
#complete 0->18(+1)
#if note less or equal to index 3, make 1 suplementary line bellow, if its less or igual to 1, make another one
#if its more or equal to index 15 create 1 suplementary line above, if its more or iqual no index 17, make another one

for c in range (0,5):
    rand = random.randrange(0, 19)
    print(notes_list[rand])
    if rand <= 3:
        print('First bellow line')
        if rand <=1:
            print('Seconde bellow line')

    if rand >= 15:
        print('First above line')
        if rand >= 17:
            print('Seconde above line')
