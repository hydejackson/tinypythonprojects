# program that takes string argument 'x'
# returns 'Ahoy, Captain, a(n) x off the larboard bow!'

while True:
    SeaCreature = input('What do ya see?\n')
    if ' ' not in SeaCreature:
        break;
    print('Arrg, try again without ye spaces!')

article = 'a'
vowels = 'aeiouAEIOU'

#check the first letter of SeaCreature
if SeaCreature[0] in vowels:
    article = 'an'

print('Ahoy, Captain, {} {} off the larboard bow!'.format(article, SeaCreature))