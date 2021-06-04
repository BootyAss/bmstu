class Stack:
    def __init__(self):
        self.items = None
        self.init = False
        self.count = 0      # Amount of not None items

    def set_size(self, size):
        if not self.init:
            self.init = True
            self.items = [None] * size      # Allocate memory for size elemets
        else:
            print('error')

    def push(self, item):
        if self.count < self.size():
            self.items[self.count] = item
            self.count += 1
        else:
            print('overflow')

    def pop(self):
        if self.count > 0:
            print(self.items[self.count - 1])
            self.items[self.count - 1] = None
            self.count -= 1
        else:
            print('underflow')

    def print(self):
        i = 0
        if self.count == 0:
            print('empty')
        else:
            while i < self.count:
                if i == self.count - 1:
                    print(self.items[i])
                else:
                    print(self.items[i], end=' ')
                i += 1

    # Max size of stack
    def size(self):
        return len(self.items)


cycle = True
stack = Stack()

while cycle:
    try:
        line = input()

    except Exception:
        cycle = False

    else:
        cmd = line.split(' ', 2)
        length = len(cmd)

        if length > 2:
            print('error')
            continue
        else:
            if not stack.init and cmd[0] != 'set_size':
                if cmd[0] == '' and length == 1:
                    continue
                elif cmd[0] == '' and cmd[1] == '' and length == 2:
                    continue
                else:
                    print('error')
                    continue

            elif length == 1:
                if cmd[0] == '':
                    continue
                elif cmd[0] == 'pop':
                    stack.pop()
                elif cmd[0] == 'print':
                    stack.print()
                else:
                    print('error')
                    continue

            elif length == 2:
                arg = cmd[1]
                if cmd[0] == 'set_size':
                    try:
                        arg = int(arg)
                    except Exception:
                        print('error')
                        continue
                    else:
                        stack.set_size(arg)

                elif cmd[0] == 'push':
                    stack.push(arg)
                else:
                    print('error')
                    continue

            else:
                print('error')
                continue





if 'set_size':
    arg = 0
    try:
        arg = int(cmd[1])
    except Exception:
        print('error')
    else:
        s.set_size(arg)
