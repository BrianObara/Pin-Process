# Pin-Process
A SIM PIN PROCESS SKULLTONE
def evaluation(event, a):
	while len(event) < a or not event.isdigit():
		print('Must be a number or is greater than', a)
		event = input()
	return event
def main():
	global PIN, PUK, a, b
	constant = 0
	while a>0:
		print('Remaining' , a)
		t = int(evaluation(input('Enter PIN: '), 4))
		a -= 1
		if a == 0:
			print('Your blocked from PIN')
			while b>0:
				p = int(evaluation(input('Enter PUK: '), 8))
				b -= 1
				if p == PUK:
					r = input('Enter New PIN: ')
					e = input('Confirm your new PIN: ')
					if r == e:
						print('Unlocking... ')
						constant += 1
						break
				elif b == 0:
					print('BLOCKED')
		elif t == PIN:
			print('Unlocking')
			constant += 1
			break
	return constant
	
PIN = 1234
PUK = 12345678
a = 3
b= 10
