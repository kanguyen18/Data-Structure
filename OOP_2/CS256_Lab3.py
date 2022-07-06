import os
import argparse

parser = argparse.ArgumentParser("We need a bigger class")
parser.add_argument("-s","--input_file", help="input file", type = str)
parser.add_argument("-e","--course_enrollment", help="input file", type = str)
parser.add_argument("-d","--dropID_file", help="input file", type = str)
args=parser.parse_args()

class genericUniversity:
    def __init__(self,studentType,ID,firstName,lastName,email):
        self._studentType = studentType
        self._firstName = firstName
        self._lastname = lastName
        self._ID = ID
        self._email = email
        
    def get_studentType(self):
        return self._studentType
    def get_firstName(self):
        return self._firstName
    def get_lastName(self):
        return self._lastName
    def get_ID(self):
        return self._ID
    def get_email(self):
        return self._email
    
    def set_studentType(self,studentType):
        self._studentType = studentType
    def set_firstName(self,firstName):
        self._firstName = firstName
    def set_lastName(self,lastName):
        self._lastName = lastName
    def set_ID(self,ID):
        self._ID = ID
    def set_email(self,email):
        self._email = email
        
class undergraduate(genericUniversity):
    def __init__(self,studentType,ID,firstName,lastName,email,dormRoom):
        super().__init__(studentType,ID,firstName,lastName,email)
        self._dormRoom = dormRoom
        
    def get_dormRoom(self):
        return self._dormRoom 
        
    def set_dormRoom(self,dormRoom):
        self._dormRoom = dormRoom
        
class graduate(genericUniversity):
    def __init__(self,studentType,ID,firstName,lastName,email,office):
        super().__init__(studentType,ID,firstName,lastName,email)
        self._office = office
        
    def get_office(self):
        return self._office
    
    def set_dormRoom(self,dormRoom):
        self._dormRoom = dormRoom
        
class course:
    def __init__(self,department,number,enrolledIDList):
        self._department = department
        self._number = number
        self._enrolledIDList = enrolledIDList
        
    def get_department(self):
        return self._department
    def get_number(self):
        return self._number
    def get_enrolledIDList(self):
        return self._enrolledIDList
    
    def set_department(self,department):
        self._department = department
    def set_number(self,number):
        self._number = number
    def set_enrolledIDList(self,enrolledIDList):
        self._enrolledIDList = enrolledIDList
        
    def enrollStudent(self,studentID):
        self._enrolledIDList.append(studentID)
        
    def countStudent(self):
        return len(self._enrolledIDList)
    
    def dropStudent(self,studentID):
        self._enrolledIDList.remove(studentID)

def loadStudent(file_name):
    if os.path.isfile(file_name):
        input_file = open(file_name,'r')
    else:
        raise ValueError("Wrong input! The file doesn't exist!")
    students_array = []
    for i in input_file:
        i = i.strip('\n')
        a = i.split(',')
        if a[0] == "grad":
            students_array.append(graduate(a[0],a[1],a[2],a[3],a[4],a[5]))
        else:
            students_array.append(undergraduate(a[0],a[1],a[2],a[3],a[4],a[5]))
    return students_array       
    
def enrolling(course_file_name, studentArray):
    enrolledIDList = []
    course_cs256 = course("CS","256",enrolledIDList)
    valid_ID_list = []
    for i in studentArray:
        valid_ID_list.append(i.get_ID())
    if os.path.isfile(course_file_name):
        input_file = open(course_file_name,'r')
    else:
        raise ValueError("Wrong input! The file doesn't exist!")
    for i in input_file:
        i = i.strip('\n')
        if i in valid_ID_list:
            course_cs256.enrollStudent(i)
    return course_cs256

def dropStudents(dropID_file,course_cs256):
    if os.path.isfile(dropID_file):
        input_file = open(dropID_file,'r')
    else:
        raise ValueError("Wrong input! The file doesn't exist!")
    enrolledIDList = course_cs256.get_enrolledIDList()
    for i in input_file:
        if i in enrolledIDList:
            course_cs256.dropStudent(i)
    return course_cs256

if __name__ == '__main__':
    studentArray = loadStudent(args.input_file)
    cs256CourseObject = enrolling(args.course_enrollment, studentArray)
    count = cs256CourseObject.countStudent()
    print(count)
    
    
    