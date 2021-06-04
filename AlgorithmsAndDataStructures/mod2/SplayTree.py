class Node:
    def __init__(self, key, data, parent=None, left=None, right=None):
        self.key = key
        self.data = data

        self.parent = parent
        self.left = left
        self.right = right


class SplayTree:
    def __init__(self):
        self.root = None

    def zig(self, p):
        x = p.left
        
        p.left = x.right
        if x.right:
            x.right.parent = p

        x.parent = p.parent
        if not p.parent:
            self.root = x
        elif p == p.parent.right:
            p.parent.right = x
        else:
            p.parent.left = x

        x.right = p
        p.parent = x

    def zag(self, p):
        x = p.right

        p.right = x.left
        if x.left:
            x.left.parent = p

        x.parent = p.parent
        if not p.parent:
            self.root = x
        elif p == p.parent.right:
            p.parent.right = x
        else:
            p.parent.left = x

        x.left = p
        p.parent = x

    def splay(self, x):
        while x.parent:
            if not x.parent.parent:
                if x == x.parent.left:
                    self.zig(x.parent)
                else:
                    self.zag(x.parent)

            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self.zig(x.parent.parent)
                self.zig(x.parent)

            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self.zag(x.parent.parent)
                self.zag(x.parent)

            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self.zag(x.parent)
                self.zig(x.parent)

            else:
                self.zig(x.parent)
                self.zag(x.parent)


    def add(self, key, data):
        x = self.root
        parent = None
        while x:
            if key == x.key:
                self.splay(x)
                raise(Exception)

            parent = x

            if key < x.key:
                x = x.left
            else:
                x = x.right

        temp = Node(key, data, parent=parent)

        if not parent:
            self.root = temp
        elif key < parent.key:
            parent.left = temp
        else:
            parent.right = temp
        self.splay(temp)


    def set(self, key, data):
        if not self.root:
            print('error')
            return

        temp = self.root
        parent = None
        while temp:
            if key == temp.key:
                temp.data = data
                self.splay(temp)
                return

            parent = temp
            
            if key < temp.key:
                temp = temp.left
            else:
                temp = temp.right

        self.splay(parent)
        print('error')

        
    def delete(self, key):
        if not self.root:
            print('error')
            return

        x = self.root
        temp = parent = None
        while x:
            if key == x.key:
                temp = x

            parent = x

            if key < x.key:
                x = x.left
            else:
                x = x.right

        if not temp:
            self.splay(parent)
            print('error')
            return

        self.splay(temp)

        leftChild = None
        rightChild = None
        if temp.right:
            rightChild = temp.right
            rightChild.parent = None
        if temp.left:
            leftChild = temp.left
            leftChild.parent = None

        if not leftChild:
            self.root = rightChild
            return
        if not rightChild:
            self.root = leftChild
            return

        while leftChild.right:
            leftChild = leftChild.right

        self.splay(leftChild)
        leftChild.right = rightChild
        rightChild.parent = leftChild

        self.root = leftChild


    def min(self):
        if not self.root:
            print('error')
            return

        temp = self.root
        while temp.left:
            temp = temp.left

        print(temp.key, temp.data)
        self.splay(temp)


    def max(self):
        if not self.root:
            print('error')
            return

        temp = self.root
        while temp.right:
            temp = temp.right
        
        print(temp.key, temp.data)
        self.splay(temp)


    def search(self, key):
        if not self.root:
            print('0')
            return

        temp = self.root
        parent = None
        while temp:
            if temp.key == key:
                print('1', temp.data)
                self.splay(temp)
                return
            elif key < temp.key:
                parent = temp
                temp = temp.left
            else:
                parent = temp
                temp = temp.right

        self.splay(parent)
        print('0')


    def print(self):
        if not self.root:
            print('_')
            return

        queue = [self.root]
        index = 0
        height = 0
        out = ''

        while len(queue):
            print(queue)
            print()
            lineLen = 1 << height

            _cycle = False
            for q in queue:
                if isinstance(q, Node):
                    _cycle = True
            if not _cycle:
                if index != 0:
                    out += '_ ' * (lineLen - index)
                print(out[0:-1])
                return

            temp = queue.pop(0)

            if isinstance(temp, Node):
                if temp.left:
                    queue.append(temp.left)
                else:
                    queue.append(0)

                if temp.right:
                    queue.append(temp.right)
                else:
                    queue.append(0)

                index += 1
                out += '[' + str(temp.key) + ' ' + temp.data
                if not height:
                    out += ']\n'
                else:
                    if index != lineLen:
                        out += ' ' + str(temp.parent.key) + '] '
                    else:
                        out += ' ' + str(temp.parent.key) + ']\n'

            else:
                amount = 1 << temp
                out += '_ ' * amount
                index += amount
                queue.append(temp + 1)

                if index == lineLen:
                    out += '\n'

            if index == lineLen:
                index = 0
                height += 1



cycle = True
tree = SplayTree()

while cycle:
    try:
        line = input()
        cmd = line.split(' ', 2)
        
        try:
            if len(cmd) == 1 and cmd[0] == '':
                continue
            if len(cmd) == 2 and cmd[0] == '' and cmd[1] == '':
                continue
            
            if cmd[0] == 'add':
                tree.add(int(cmd[1]), cmd[2])

            elif cmd[0] == 'set':
                    tree.set(int(cmd[1]), cmd[2])

            elif cmd[0] == 'delete':
                tree.delete(int(cmd[1]))

            elif cmd[0] == 'search':
                tree.search(int(cmd[1]))

            elif cmd[0] == 'min':
                tree.min()

            elif cmd[0] == 'max':
                tree.max()

            elif cmd[0] == 'print':
                tree.print()

            else:
                raise(Exception)

        except Exception:
            print('error')
            continue

    except Exception:
        cycle = False