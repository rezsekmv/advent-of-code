import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from copy import deepcopy
import multiprocessing

def parse_input(text):
    bricks = []
    lines = text.split('\n')

    for i, line in enumerate(lines):
        start, end = line.split('~')
        x1, y1, z1 = start.split(',')
        x2, y2, z2 = end.split(',')
        x1, x2, y1, y2, z1, z2 = int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)

        bricks.append([])
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    bricks[-1].append((x, y, z))
        bricks[-1].append(i)
    return bricks

def falling(bricks, do):
    uniqe = set()
    while True:
        fell = 0
        for i in range(len(bricks)):
            can_fall = True
            for ii in range(len(bricks)):
                if bricks[i] == bricks[ii]:
                    continue
                for j, coords in enumerate(bricks[i][:-1]):
                    x, y, z = coords
                    if  (x, y, z-1) in bricks[ii] or z <= 1:
                        can_fall = False
                        break
                if not can_fall:
                    break
            if can_fall:
                for j, coords in enumerate(bricks[i][:-1]):
                    if do:
                        x, y, z = coords
                        bricks[i][j] = (x, y, z-1)
                        uniqe.add(bricks[i][-1])
                fell += 1
               
        if not do:
            return fell

        if fell < 1:
            break

    return len(uniqe)

def process_brick(bricks, brick):
    tmp_bricks = deepcopy(bricks)
    tmp_bricks.remove(brick)
    return falling(tmp_bricks, False), falling(tmp_bricks, True)

if __name__ == "__main__":
    import time

    start_time = time.time()
    text = get_data(22, 2023)
    bricks = parse_input(text)
    num_processes = multiprocessing.cpu_count()
    print("Full calculation on {} cores, it takes approximately {} minutes".format(num_processes, 2+130//num_processes))

    print("Falling simulation started (approx 2 minutes)")
    falling(bricks, True)
    end_time = time.time()
    print("Falling simulation finished. Time: {:.2f} sec".format(end_time - start_time))

    print("Calculation started (approx {} minutes)".format(130//num_processes))
    with multiprocessing.Pool(processes=num_processes) as pool:
        tasks = [pool.apply_async(process_brick, (bricks,brick)) for brick in bricks]

        results = [task.get() for task in tasks]
        p1 = sum(1 for result in results if result[0] == 0)
        p2 = sum(result[1] for result in results)

    end_time = time.time()
    print('Calculation finished. Time: {:.2f} sec'.format(end_time - start_time))
    print(p1)
    print(p2)
