roster = []
def addStudent(student , grade):
    roster.append([student,grade])
    roster.sort() 
    

def grade(rank):
    liste = []
    for i in roster:
        if i[1] == rank:
           liste.append(i[0])
    print(f"this is students in roster of grade {rank} : {liste}") 

def rankList():
    for i in range(1,4):
        grade(i)

addStudent('doddy',3)
addStudent('nicolas',3)
addStudent('tiffany',1)
addStudent('tania',2)
addStudent('paul',1)
addStudent('djo',2) 
#grade(3) 
#grade(2)
#grade(1)
rankList()        