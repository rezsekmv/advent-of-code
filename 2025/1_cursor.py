def solve():
    with open('input_1.in', 'r') as f:
        data = f.read()
    lines = data.strip().split('\n')
    
    # Part 1: Count times dial points at 0 after any rotation
    position = 50
    part1 = 0
    
    for line in lines:
        if not line.strip():
            continue
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        else:  # R
            position = (position + distance) % 100
        
        if position == 0:
            part1 += 1
    
    # Part 2: Count times dial points at 0 during any rotation (including intermediate positions)
    position = 50
    part2 = 0
    
    for line in lines:
        if not line.strip():
            continue
        direction = line[0]
        distance = int(line[1:])
        
        start_pos = position
        
        if direction == 'L':
            end_pos = (position - distance) % 100
            # Check all intermediate positions (excluding start, including end)
            for step in range(1, distance + 1):
                check_pos = (start_pos - step) % 100
                if check_pos == 0:
                    part2 += 1
        else:  # R
            end_pos = (position + distance) % 100
            # Check all intermediate positions (excluding start, including end)
            for step in range(1, distance + 1):
                check_pos = (start_pos + step) % 100
                if check_pos == 0:
                    part2 += 1
        
        position = end_pos
    
    print(part1)
    print(part2)

if __name__ == '__main__':
    solve()

