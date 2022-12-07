FILENAME = '7.txt'
lines = []

with open(FILENAME) as f:
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

#====================================================

result = ''
treshold = 100000
total = 70000000
need  = 30000000

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.dirs = []

    def addFile(self, file):
        self.files.append(file)

    def addDir(self, dir):
        self.dirs.append(dir)

    def findDirByName(self, name):
        for d in self.dirs:
            if d.name == name:
                return d
        return None
        
    def getFilesSize(self):
        summ = 0
        for f in self.files:
            summ += f
        return summ

    def getDirSize(self):
        summ = self.getFilesSize()
        for d in self.dirs:
            summ += d.getDirSize()
        return summ

    def getDirSizeTreshold(self):
        summ = self.getFilesSize()
        for d in self.dirs:
            summ += d.getDirSize()
        
        if summ <= treshold:
            return summ
        else:
            return 0

    def __str__(self) -> str:
        return self.name

root = None
currentDir = None

for line in lines:
    if line.startswith('$'):
        if line[2:4] == 'cd':
            inp = line.split(' ')
            if inp[2] == '..':
                currentDir = currentDir.parent
            else:
                if inp[2] == '/':
                    currentDir = Dir('/', None)
                    root = currentDir
                else:
                    currentDir = currentDir.findDirByName(inp[2])
            
        elif line[2:4] == 'ls':
            pass
        else:
            print('HIBA')

    else:
        inp = line.split(' ')
        if inp[0] == 'dir':
            currentDir.addDir(Dir(inp[1], currentDir))
        else:
            currentDir.addFile(int(inp[0]))

al = []
def getSize(directory, summm):
    for d in directory.dirs:
        summm += d.getDirSize()
        summm += getSize(d, 0)
    return summm

def getSmallestSize(arr):
    s = total
    for a in arr:
        if a < s:
            s = a
    return s

now = total - root.getDirSize()

def getSizes(dir):
    al.append(dir.getDirSize())
    for a in dir.dirs:
        getSizes(a)

getSizes(root)

filtered = [x for x in al if now+x > need]

print(getSmallestSize(filtered))