import random
count = 0

for number in range(10):

    player = int(input('Сделайте ход - 1-камень, 2-ножницы, 3-бумага:'))
    if player == 1:
        print('ход игрока камень')
    elif player == 2:
        print('ход игрока ножницы')
    elif player == 3:
        print('ход игрока бумага')
    else:
        print("Я вас не понимаю...")
    comp = random.randint(1,3)
    if comp == 1:
        print('ход компьютера камень')
    elif comp == 2:
        print('ход компьютера ножницы')
    elif comp == 3:
        print('ход компьютера бумага')

    if comp == player:
        print('ничья!')
    elif comp ==1 and player == 2:
        print('победил компьютер!')
    elif comp ==2 and player == 3:
        print('победил компьютер')
    elif comp == 3 and player == 1:
        print('победил компьютер')
    elif player == 1 and comp == 2:
        print('победил игрок')
        count += 1
    elif player == 2 and comp == 3:
        print('победил игрок')
        count +=1
    elif player == 3 and comp == 1:
        print('победил игрок')
        count += 1
    print('мои победы:', count)

    if count == 3:
        break