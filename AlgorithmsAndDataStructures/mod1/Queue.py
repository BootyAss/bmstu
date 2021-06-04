import sys
class Queue:
    def __init__(self):
        self.items = None
        self.init = False
        self.count = 0      # Amount of not None items
        self.toPop = 0      # Index of item to pop
        self.toPush = 0     # Index of item to push

    def set_size(self, size):
        if not self.init:
            self.init = True
            self.items = [None] * size
        else:
            fileOut.write('error\n')

    def push(self, item):
        if self.count < self.size():
            if (self.toPush >= self.size()):
                self.toPush = 0
            self.items[self.toPush] = item
            self.toPush += 1
            self.count += 1
        else:
            fileOut.write('overflow\n')

    def pop(self):
        if self.count > 0:
            if (self.toPop >= self.size()):
                self.toPop = 0
            fileOut.write(self.items[self.toPop] + '\n')
            self.items[self.toPop] = None
            self.count -= 1
            self.toPop += 1
        else:
            fileOut.write('underflow\n')

    def print(self):
        if self.count == 0:
            fileOut.write('empty\n')
        else:
            toPrint = self.toPop
            i = 0
            while i < self.count:
                if toPrint == self.size():
                    toPrint = 0
                if not (self.items[toPrint] is None):
                    if i == self.count - 1:
                        fileOut.write(self.items[toPrint] + '\n')
                    else:
                        fileOut.write(self.items[toPrint] + ' ')
                    i += 1
                toPrint += 1

    def size(self):
        return len(self.items)


queue = Queue()

try:
    fileIn = open(sys.argv[1])
    fileOut = open(sys.argv[2], 'w')

except Exception:
    print('error')

else:
    for line in fileIn:
        line = line[0:-1]   # remove /n
        cmd = line.split(" ", 2)
        length = len(cmd)

        if length > 2:
            fileOut.write('error\n')
            continue
        else:
            if not queue.init and cmd[0] != 'set_size':
                if cmd[0] == '' and length == 1:
                    continue
                elif cmd[0] == '' and cmd[1] == '' and length == 2:
                    continue
                else:
                    fileOut.write('error\n')
                    continue

            elif length == 1:
                if cmd[0] == '':
                    continue
                elif cmd[0] == 'pop':
                    queue.pop()
                elif cmd[0] == 'print':
                    queue.print()
                else:
                    fileOut.write('error\n')
                    continue

            elif length == 2:
                arg = cmd[1]
                if cmd[0] == 'set_size':
                    try:
                        arg = int(arg)
                    except Exception:
                        fileOut.write('error\n')
                        continue
                    else:
                        queue.set_size(arg)

                elif cmd[0] == 'push':
                    queue.push(arg)
                else:
                    fileOut.write('error\n')
                    continue

            else:
                fileOut.write('error\n')
                continue

    fileIn.close()
    fileOut.close()
    print('done')
