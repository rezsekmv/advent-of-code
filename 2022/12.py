from my_input import lines
import util
import math
import heapq

maze = lines
elevation = 'a'

for m in maze:
    m = m.lower()

class Node():
    def __init__(self, letter, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.letter = letter
        self.steps = 0

    def __eq__(self, other):
        return self.position == other.position



def find_path(maze, start, end):

    start_node = Node('z', None, start)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node.letter == 'a':
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            node_letter = maze[node_position[0]][node_position[1]]
            if node_letter == 'S':
                node_letter = 'a'

            if ord(current_node.letter) - ord(node_letter) > 1:
                continue

            if current_node.parent is not None and node_position == current_node.parent.position:
                continue

            for open_child in open_list:
                if node_position == open_child.position:
                    continue

            new_node = Node(maze[node_position[0]][node_position[1]], current_node, node_position)         
            children.append(new_node)

        for child in children:
            append = True
            for closed_child in closed_list:
                if child == closed_child:
                    append = False
                    break

            child.steps = current_node.steps + 1

            for open_node in open_list:
                if child == open_node:
                    append = False
                    break
            
            if append:
                open_list.append(child)

    print('end')

for i, row in enumerate(maze):
    s2 = row.find('S')
    if (s2 >= 0):
        s1 = i
        break;

start = (s1, s2)

for i, row in enumerate(maze):
    c = row.find('E')
    if (c >= 0):
        r = i
        break;

end = (r, c)

path = find_path(maze, end, start)

print(len(path)-1)