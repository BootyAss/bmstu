s = 0
cycle = True

while cycle:
    try:
        lst = input()
        if (lst == ''):
            continue
        else:
            i = 0
            num = ''
            while i < len(lst):
                if ('0' <= lst[i] <= '9'):
                    num += lst[i]
                else:
                    if (num == '-'):
                        num = ''
                    if (num != ''):
                        s += int(num)
                        num = ''

                if (lst[i] == '-' and num == ''):
                    num += '-'

                i += 1
            if (num == '-'):
                num = ''
            if (num != ''):
                s += int(num)

    except Exception:
        cycle = False

print(str(s))
