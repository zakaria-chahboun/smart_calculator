
import re # regex : regular expressions

# main
def main():

	print('Enter your mathematical operations: ')
	# Example : 88 + 10 -15 * 20 * 3 / 10 / 2 - 45
	# = 8

	Input = raw_input() # String

	#---- validate mathematical expressions ----
	if re.search('^\s*([-+])?([0-9]+)(?:\s*([-+*/])\s*((?:\s[-+])?[0-9]+)\s*)+$',Input):

		# return a list of operations, for example : ['10','+','4','/','8']
		All = re.findall("[-*/+]+|[0-9]+", Input)

		# signed numbers like : -10 + 12 or +10 + 12
		if All[0] == '+' or All[0] == '-':
			All.insert(0,0) # Insert '0' in the begin of list operations

		#---- Division ----
		while '/' in All:
			i = All.index('/')

			# convert String to float and calculat the division
			div = float(All[i-1])/float(All[i+1])
			# delete the operation for example : ['10','/','2']
			del All[i-1] # delete : ['10']
			del All[i-1] # delete : ['/']
			del All[i-1] # delete : ['2']
			All.insert(i-1,div) # replace [ 10 / 2 ] with 5

		#---- Multiplication ----
		while '*' in All:
			i = All.index('*')
			mult = float(All[i-1])*float(All[i+1])
			del All[i-1]
			del All[i-1]
			del All[i-1]
			All.insert(i-1,mult)

		#---- Addition or Substraction ----
		while '+' in All or '-' in All:
			i = 1 # number 2, for example : ['1','+','2'] so : All[1] == '+'

			if All[i] == '+':
				add = float(All[i-1])+float(All[i+1])
				del All[i-1]
				del All[i-1]
				del All[i-1]
				All.insert(i-1,add)

			elif All[i] == '-':
				sub = float(All[i-1])-float(All[i+1])
				del All[i-1]
				del All[i-1]
				del All[i-1]
				All.insert(i-1,sub)


		#---- The Result ----
		print('------')
		print(All[0])
		print('------')

	#---- Errors! ----
	else:
		print('OPPS !! wrong expressions!')

	
	
# Start here	
if __name__ == '__main__': main()


#-----------------
# python 2.7

# Smart Calculator by zakaria chahboun | 27/06/2017

# twitter : @zaki_chahboun
# facebook : /zakaria.chahboun.2018
#-----------------
