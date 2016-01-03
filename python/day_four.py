import hashlib
m = hashlib.md5()
secret = input("Secret key: ")
code = 0
advent5Found = False

while True:
	code += 1
	test = secret + str(code)
	m = hashlib.md5()
	m.update(test.encode('utf-8'))
	result = str(m.hexdigest())
	if result.startswith("00000") and not advent5Found:
		advent5 = str(code)
		advent5Found = True
	if result.startswith("000000"):
		advent6 = str(code)
		break
print("AdventCoin 5 zero: " + advent5)
print("AdventCoin 6 zero: " + advent6)