from collections import namedtuple


citizen = namedtuple("Citizen", "name age status")
Alex = citizen(name='Alex Mercer', age=27, status='show businessman')

print(Alex.age)