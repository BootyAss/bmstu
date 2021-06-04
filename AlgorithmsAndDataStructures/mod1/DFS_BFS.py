from queue import Queue

List = dict()       # adjacency list
visited = dict()    # dict contains all verticies
                    # to check if visited in const time 

def depth(start):
    stack = []
    stack.append(start)

    output = ''

    while len(stack):
        v = stack.pop()

        if visited[v]:
            continue
        else:
            visited[v] = True
            output += v + '\n'

            for neighbour in List[v]:
                if not visited[neighbour]:
                    stack.append(neighbour)

    print(output[0:-1],end='')


def width(start):
    queue = Queue()
    queue.put(start)

    output = ''

    while not queue.empty():
        v = queue.get()

        if visited[v]:
            continue
        else:
            visited[v] = True
            output += v + '\n'

            for neighbour in List[v]:
                if not visited[neighbour]:
                    queue.put(neighbour)

    print(output[0:-1],end='')


cycle = True
init = False

while cycle:
    try:
        line = input()
    except Exception:
        cycle = False
    else:
        cmd = line.split()

        if len(cmd) == 3 and not init:
            graph = cmd[0]
            start = cmd[1]
            search = cmd[2]
            init = True

        elif len(cmd) == 2 and init:
            if cmd[0] in List:
                if not cmd[1] in List[cmd[0]]:
                    List[cmd[0]].append(cmd[1])
            else:
                List[cmd[0]] = [cmd[1]]

            if graph == 'u':
                if cmd[1] in List:
                    if not cmd[0] in List[cmd[1]]:
                        List[cmd[1]].append(cmd[0])
                else:
                    List[cmd[1]] = [cmd[0]]
            else:
                if cmd[1] not in List:
                    List[cmd[1]] = []                

if init:
    if search == 'b':
        for k,i in List.items():
            visited[k] = None
            i.sort()
        width(start)    

    if search == 'd':
        for k,i in List.items():
            visited[k] = None
            i.sort(reverse=True)
        depth(start)
