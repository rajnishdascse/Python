import random
doors = [0]*3  #there will be 3 choice
goatdoors = [0]*2   
swap = 0
dont_swap  =0
j = 0

while (j<10):
    x = random.randint(0,2)
    doors[x] = 'BMW'
    for i in range(0,3):
        if i==x:
            continue
        else:
            doors[i] = 'Goat'
            goatdoors.append(i)
    choice = int(input('Enter your choice (0-2): '))
    door_open = random.choice(goatdoors)
    while (door_open==choice):
        door_open = random.choice(goatdoors)
    ch = input('Do you want to swap.. y/n?')
    if ch=='y':
        if doors[choice] == 'Goat':
            print('Player wins')
            swap = swap+1
        else:
            print('Player lost')
    else:
        if doors[choice]=='Goat':
            print('Player lost')
        else:
            print('Player wins')
            dont_swap +=1
    j+=1

print('No. of swap: ',swap)
print('No. of dont swap: ',dont_swap)