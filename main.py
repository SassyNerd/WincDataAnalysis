# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer_1 + ' ' + f'{goal_0}' + ', ' + scorer_2 + ' ' f'{goal_1}'
report = scorer_1 + ' scored in the ' + f'{goal_0}' + 'nd minute' '\n' + scorer_2 + ' scored in the ' + f'{goal_1}' + 'th minute'
print (report)
player = 'Ronald Koeman'
myIndex = player.find(' ')
print (myIndex)
first_name = player[0:myIndex]
print (first_name)
last_name_len = len(player) - (myIndex +1)
print (last_name_len)
print(player[myIndex:len(player)])
name_short = player[0] + '.' + player[myIndex:len(player)]
print (name_short)
chant = (first_name + '! ') * (len(first_name) - 1)  + first_name + '!'
print (chant)
good_chant = chant[len(chant)-1] != ' '