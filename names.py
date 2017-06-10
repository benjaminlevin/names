#Part One

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def part_one():
    i = 0
    while i < len(students):
        print students[i]['first_name'], students[i]['last_name']
        i += 1
part_one()

#Part Two

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def part_two():
    print "Students"
    i = 0
    while i < len(users['Students']):
        print i+1, '-', users['Students'][i]['first_name'], users['Students'][i]['last_name'], '-', len(users['Students'][i]['first_name']) + len(users['Students'][i]['last_name'])
        i += 1
    print "Instructors"
    i = 0
    while i < len(users['Instructors']):
        print i+1, '-', users['Instructors'][i]['first_name'], users['Instructors'][i]['last_name'], '-', len(users['Instructors'][i]['first_name']) + len(users['Instructors'][i]['last_name'])
        i += 1
part_two()
