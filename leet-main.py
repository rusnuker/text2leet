from argparse import ArgumentParser
def main():
	parser = ArgumentParser()
	parser.add_argument("-o", "--output",
		dest="filename", help="write translated string to FILE", metavar="FILE")
	parser.add_argument("-t","--type", type=str,help="type for translation. can be \"simple\", \"good\" or \"hard\"", default="good")
	parser.add_argument("string", type=str,help="string to translate.", nargs="?", )
	args = parser.parse_args()
	if args.string==None:
		print("\n [FKDUP] \n")
		raise Exception("check ur arguments, ur missing string!")
	if args.filename:
		with open(args.filename,"w") as f:
			if args.type=="simple":
				f.write(simple(args.string))
			elif args.type=="good":
				f.write(good(args.string))
			elif args.type=="hard":
				f.write(hard(args.string))
			else:
				raise Exception("check ur arguments, ur fucked up with type of translation!")
		f.close()
	else:
		if args.type=="simple":
			print(simple(args.string))
		elif args.type=="good":
			print(good(args.string))
		elif args.type=="hard":
			print(hard(args.string))
		else:
			raise Exception("check ur arguments, ur fucked up with type of translation!")
if __name__=="__main__":
	def simple(string):
		leet_str = string.replace('e','3').replace('o','0')
		return leet_str

	def good(string):
		leet_str = string.replace('l','1').replace('e','3').replace('o','0').replace('a','4')
		return leet_str

	def hard(string):
		leet_str = string.replace('l','1').replace('e','3').replace('o','0').replace('t','7').replace('a','4').replace('g','6')
		return leet_str
	main()
