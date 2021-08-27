def simple(string):
	leet_str = string.replace('e','3').replace('o','0')
	return leet_str

def good(string):
	leet_str = string.replace('l','1').replace('e','3').replace('o','0').replace('a','4')
	return leet_str

def hard(string):
	leet_str = string.replace('l','1').replace('e','3').replace('o','0').replace('t','7').replace('a','4').replace('g','6')
	return leet_str
def usage():
	print("usage: leet.simple(string) or leet.good(string) or leet.hard(string)")
if __name__ == '__main__':
	print("Y0u sh0u1d imp0rt it 4s m0du13!")