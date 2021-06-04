def printf(arr):
	out = ''
	for i in range(len(arr) - 1, -1, -1):
		out += arr[i] + '\n'

	print(out, end='')


def Dappa(amount):
	actions = []

	while amount > 0:
		amount = int(amount)
		if not amount % 2:
			actions.append('dbl')
			amount /= 2
			continue

		dec = bin(amount + 1)
		inc = bin(amount - 1)

		dec_ones = dec.count('1')
		inc_ones = inc.count('1')

		if dec_ones < inc_ones:
			actions.append('dec')
			amount += 1
		elif dec_ones > inc_ones:
			actions.append('inc')
			amount -= 1
		elif len(dec) > len(inc):
			actions.append('inc')
			amount -= 1
		else:
			actions.append('dec')
			amount += 1

	return actions


amount = int(input())
printf(Dappa(amount))
