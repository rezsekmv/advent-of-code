from my_input import lines

cycle = 0
X = 1
su = 0

isAddx = False
for i in range(len(lines)):
    while True:
        command = lines[i].split(' ')
        cycle += 1


        if X-1 <= cycle%40-1 <= X+1:
            print('#', end='')
        else: 
            print('.', end='')

        if cycle == 40 or cycle == 80 or cycle == 120 or cycle == 160 or cycle == 200 or cycle == 240:
            print()


        if command[0] == 'addx':
            if isAddx:
                X += int(command[1])
                isAddx = False
                break
            else:
                isAddx = True
                continue

        break
