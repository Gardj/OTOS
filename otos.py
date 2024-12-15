



alphabet = {'zero': '\ufeff', 'one': '\u2060', 'two': '\u200b', 'three': '\u200d', 'four': '\u200c'}

def convert_base(num, to_base, from_base):
    n = int(num, from_base) if isinstance(num, str) else num

    alphabet = "0123456789ABCDEF"
    res = ""
    while n > 0:
        n,m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]

def read(path: str):
	file = open(path, "rb")
	data = file.read()

	fivenary = ""

	for i in data:
		fivenary += convert_base(data[i], 5, 16)
	file.close()

	return fivenary

def write(name: str, data: str):
	file = open(name, "wb")
	file.write(data)

	file.close()

def encode(fivenary: str):
	code = ""

	for sym in fivenary:
		if sym == '0':
			code += alphabet['zero']
		elif sym == '1':
			code += alphabet['one']
		elif sym == '2':
			code += alphabet['two']
		elif sym == '3':
			code += alphabet['three']
		elif sym == '4':
			code += alphabet['four']

	return code

def decode(code: str):
	fivenary = ""

	for sym in code:
		if sym == alphabet['zero']:
			fivenary += '0'
		elif sym == alphabet['one']:
			fivenary += '1'
		elif sym == alphabet['two']:
			fivenary += '2'
		elif sym == alphabet['three']:
			fivenary += '3'
		elif sym == alphabet['four']:
			fivenary += '4'

	return fivenary



# msg = open("msg.txt", "wb")

# img  = encode(read("art.png"))

# msg.write(bytes(img, encoding = "UTF-8"))


msg = open("msg.txt", "rb")

img = open("tra.png", "wb")

data = msg.read().decode("UTF-8")

decode = ""
st = ""
for i in data:
	st += convert_base(data[i])
	
	if i % 4 == 0:
	st += convert_base(data[i])
	st = ""
print(convert_base(decode(data), 16, 5))
img.write(decode(data))

