# Sorting hat code, Control Flow - Ex 16

print('=======================')
print('SORTING HAT')
print('=======================')

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print(' \n Q1. Do you like Dawn or Dusk? \n 1) Dawn \n 2) Dusk \n')
q1 = int(input('Enter your selection (1-2): '))

if q1 == 1:
  gryffindor =+ 1
  ravenclaw =+ 1
  print('Gryffindor and Ravenclaw both get a +1')
elif q1 == 2:
  hufflepuff = 1
  slytherin = 1
  print('Hufflepuff and Slytherin both get a +1')
else:
  print('Wrong input')


print ('\n Q2. When I’m dead, I want people to remember me as: \n 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold')
q2 = int(input('Enter your selection (1-4): '))

if q2 == 1:
  hufflepuff =+ 2
  print('Hufflepuff +2')
elif q2 == 2:
  slytherin =+ 2
  print('Slytherin +2')
elif q2 == 3:
  ravenclaw =+ 2
  print('Ravenclaw +2')
elif q2 == 4:
  gryffindor =+ 2
  print('Gryffindor +2')
else:
  print('Wrong input')


print ('\n Q3) Which kind of instrument most pleases your ear?: \n 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum')
q3 = int(input('Enter your selection (1-4): '))

if q3 == 1:
  slytherin =+ 4
  print('Slytherin +4')
elif q3 == 2:
  hufflepuff =+ 4
  print('Hufflepuff +4')
elif q3 == 3:
  ravenclaw =+ 4
  print('Ravenclaw +4')
elif q3 == 4:
  gryffindor =+ 4
  print('Gryffindor +4')
else:
  print('Wrong input')

print('Slytherin:', slytherin)
print('Hufflepuff:', hufflepuff)
print('Ravenclaw:', ravenclaw)
print('Gryffindor:', gryffindor)