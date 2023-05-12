#takes input string
#prints 'You are bringing input.'
#   input can be a list separated by commas
#   a list of two will have elements separated by an 'and'
#   a list of three or more will have elements separated by ',' and an 'and' at the end of the list
#the user will be able to sort the output of items alphabetically and reverse alphabetically

stuff = ''
#get input
bringing = input('What are you bringing to the picnic?\n')
#get sort? ynr
sorting = input('Sort your items? (y/n/r)\n')
#split input list by commas
splitBringing = bringing.split(',')
#check length of input list
bringingLength = len(splitBringing)
#sort?
if sorting == 'y':
    splitBringing.sort()
elif sorting == 'r':
    splitBringing.reverse()
    
#if 1
if bringingLength == 1:
    stuff = splitBringing[0]
#if 2
elif  bringingLength == 2:
    stuff = ' and '.join(splitBringing)
#if 3+
else:
    splitBringing[-1] = 'and ' + splitBringing[-1]
    stuff = ', '.join(splitBringing)
    
#print 'You are bringing...'
print('You are bringing {}.'.format(stuff))