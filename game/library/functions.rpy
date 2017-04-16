init python:

    studentIndex = []
    studentStats = []
    studentImages = []

    def generateSudentIndex(number=0, sex='random'):
        # GenerateStudentIndex appends array[sex, firstName, lastName] to studentIndex
        for numbers in range(number):
            # We need a tmp array to store all data
            newStudent = []
            if sex == 'random':
                newStudent.append(renpy.random.choice(["male", "female"]))
            else:
                newStudent.append(sex)
            # When we have gender, we can generate a name.
            studentName = generateStudentName(sex)
            newStudent.append(studentName[0])
            newStudent.append(studentName[1])

            studentIndex.append(newStudent)
        return


    def generateSudentStats(number=0, student=''):
        # GenerateStudentStats appends a array with all student data to studentStats.
        # We need a temp array to store all data
        newStudent = []
        counter = 0
        while len(studentIndex) > len(studentStats):
            newStudent.append(studentIndex[counter][0]) #Sex
            newStudent.append(studentIndex[counter][1]) #First name
            newStudent.append(studentIndex[counter][2]) #last name
            newStudent.append(morale)                   #morale
            newStudent.append(behavior)                 #behavior
            newStudent.append(academics)                #academics
            newStudent.append(artistery)                #artistery
            newStudent.append(athletics)                #athletics
            newStudent.append(deviance)                 #deviance
            newStudent.append(inhibition)               #inhibition
            newStudent.append(10)                       #respect
            newStudent.append(0)                        #affection
            studentStats.append(newStudent)             #add to storage!
            counter += 1                                #...and next student!

        #for numbers in range(number):
        return


    def generateSudentIntegrity(test='simple'):
        # Will verify that studentIndex and studentStats is in sync.
        if test == 'simple':
            return len(studentIndex) == len(studentStats)
        elif test == 'normal' or 'full':
            v = 0
            for students in range(len(studentIndex)):
                # We need a tmp array to store all data
                v += 1
            if test == 'full':
                pass
        return


    def removeStudent(firstName='firstName', lastName='lastName', id=0):
        if id != 0:
            #remove student with that id
            pass
        elif firstName != 'firstName' and lastName != 'lastName':
            #remove student with that name
            pass
        else:
            #Randomly remove a student
            pass


