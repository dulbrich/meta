
def to_base(number, base): # up to 64
	digits = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"
	digitlist = []
	currval = number
	while currval >= base:
		quotient = currval//base
		remainder = currval % base
		digitlist.append(digits[remainder])
		currval = quotient
	if currval > 0:
		digitlist.append(digits[currval])
	digitlist.reverse()
	return "".join(digitlist)

print(to_base(25, 11))