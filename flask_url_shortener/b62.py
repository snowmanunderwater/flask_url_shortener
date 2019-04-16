ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(ALPHABET)


def encode(num):
    digits = []

    while num > 0:
        remainder = ALPHABET[num % BASE]
        digits.append(remainder)
        num //= BASE
    
    return("".join(reversed(digits)))


def decode(string):
	strlen = len(string)
	num = 0
	idx = 0

	for char in string:
		power = (strlen - (idx + 1))
		num += ALPHABET.index(char) * (BASE ** power)
		idx += 1
	  
	return num
