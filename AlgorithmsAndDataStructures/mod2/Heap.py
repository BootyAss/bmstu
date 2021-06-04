class Heap:
    def __init__(self):
        self.items = dict()     # key - (value, index)
        self.indexes = []       # index  - key // to know indexes 


    # Usefull functions
    def swap(self, i, j):
        x = self.indexes[i]     # key of 1 item
        y = self.indexes[j]     # key of 2 item

        # swap keys in index array
        self.indexes[i] = y
        self.indexes[j] = x

        temp = self.items[x][1]     # index of 1 item

        # swap indexes in dictionary
        self.items.update({x: (self.items[x][0], self.items[y][1])})
        self.items.update({y: (self.items[y][0], temp)})

    def bigger(self, i, j):
        if self.indexes[i] <= self.indexes[j]:
            return False
        else:
            return True


    # Check family UwU
    def hasParent(self, i):
        if (i - 1)/2 >= 0:
            return True
        return False
    def parentIndex(self, i):
        return int((i - 1)/2)

    def hasLeft(self, i):
        if i*2 + 1 < len(self.indexes):
            return True
        return False
    def leftIndex(self, i):
        return int(i*2 + 1)

    def hasRight(self, i):
        if i*2 + 2 < len(self.indexes):
            return True
        return False
    def rightIndex(self, i):
        return int(i*2 + 2)


    # heapifys
    def heapifyUp(self, i=None):
        if i:
            index = i
        else:
            index = len(self.indexes) - 1

        while self.hasParent(index) and self.bigger(self.parentIndex(index), index):
            self.swap(self.parentIndex(index), index)
            index = self.parentIndex(index)

    def heapifyDown(self, i=0):
        index = i
        while self.hasLeft(index):
            smaller = self.leftIndex(index)
            if self.hasRight(index) and self.bigger(self.leftIndex(index), self.rightIndex(index)):
                smaller = self.rightIndex(index)

            if self.bigger(smaller, index):
                break
            else:
                self.swap(index, smaller)

            index = smaller


    # all needed methods
    def add(self, key, data):
        if self.items.get(key, None):
            raise(Exception)

        self.items[key] = (data, int(len(self.indexes)))
        self.indexes.append(key)
        self.heapifyUp()

    def set(self, key, data):
        temp = self.items.get(key, None)
        if not temp:
            raise(Exception)

        self.items[key] = (data, temp[1])

    def delete(self, key):
        temp = self.items.get(key, None)
        if not temp:
            raise(Exception)

        if len(self.indexes) > 1:
            lastKey = self.indexes[-1]
            last = self.items.get(lastKey, None)

            # set last item index of deleted
            self.items.update({lastKey: (last[0], temp[1])})

            # set key of last item to deleted index
            self.indexes[temp[1]] = lastKey

        self.indexes.pop()
        del self.items[key]

        if temp[1] < len(self.indexes):   # dont heapify if deleted last element
            self.heapifyDown(i=temp[1])
            self.heapifyUp(i=temp[1])

    def search(self, key):
        temp = self.items.get(key, None)
        if temp:
            print('1', temp[1], temp[0])
        else:
            print('0')

    def min(self):
        if len(self.indexes) == 0:
            raise(Exception)

        key = self.indexes[0]
        print(key, '0', self.items[key][0])

    def max(self):
        if len(self.indexes) == 0:
            raise(Exception)

        i = int(len(self.indexes)/2)
        maxKey = self.indexes[i]

        index = i
        while i < len(self.indexes):
            if maxKey < self.indexes[i]:
                maxKey = self.indexes[i]
                index = i
            i += 1
        print(maxKey, index, self.items[maxKey][0])

    def extract(self):
        if len(self.indexes) == 0:
            raise(Exception)

        rootKey = self.indexes[0]
        rootData = self.items[rootKey][0]
        del self.items[rootKey]

        if len(self.indexes) > 1:
            self.indexes[0] = self.indexes.pop()

            # set top item index to 0
            self.items.update({self.indexes[0] : (self.items[self.indexes[0]][0], 0)})
            
            self.heapifyDown()
        else:
            self.indexes.pop()

        print(rootKey, rootData)

    def print(self):
        height = 0
        index = 0
        out = ''

        i = 0
        if len(self.indexes) == 0:
            out += '_\n'
            print('_')
            return

        while i < len(self.indexes):
            lineLen = 1 << height
            index += 1
            key = self.indexes[i]
            out += '[' + str(key) + ' ' + self.items[key][0]
            if height != 0:
                out += ' ' + str(self.indexes[self.parentIndex(i)])

            out += ']'

            if index == lineLen:
                out += '\n'
                index = 0
                height += 1
            else:
                out += ' '
            i += 1

        if index != 0 and index < lineLen:
            out += '_ ' * (lineLen - index)
            print(out[0:-1])
        else:
            print(out, end='')


cycle = True
heap = Heap()

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
                heap.add(int(cmd[1]), cmd[2])

            elif cmd[0] == 'set':
                heap.set(int(cmd[1]), cmd[2])

            elif cmd[0] == 'delete':
                heap.delete(int(cmd[1]))

            elif cmd[0] == 'search':
                heap.search(int(cmd[1]))

            elif cmd[0] == 'min':
                heap.min()

            elif cmd[0] == 'max':
                heap.max()

            elif cmd[0] == 'extract':
                heap.extract()

            elif cmd[0] == 'print':
                heap.print()

            else:
                raise(Exception)

        except Exception:
                print('error')
                continue

    except Exception:
        cycle = False
