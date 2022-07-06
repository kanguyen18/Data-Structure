import os
import argparse

parser = argparse.ArgumentParser("Do things with file")
parser.add_argument("-i","--inputfile", help="input file", type = str)
parser.add_argument("-p","--percent", help="input file", type = float)
args=parser.parse_args()

class Student:
    def __init__(self,ID,firstName,lastName,email,year,gpa):
        self.ID=ID
        self.firstName=firstName
        self.lastName=lastName
        self.email=email
        self.year=year
        if float(gpa) > 4.0:
            print("Error! GPA can not exceed 4.0!")
            self.gpa = "4.0"
        else:
            self.gpa = gpa
    
    def get_ID(self):
        return self.ID
    
    def get_firstName(self):
        return self.firstName
    
    def get_lastName(self):
        return self.lastName
    
    def get_email(self):
        return self.email
    
    def get_year(self):
        return self.year
    
    def get_gpa(self):
        return self.gpa
        
    def set_ID(self,ID):
        self.ID = ID
    
    def set_firstName(self,firstName):
        self.firstName = firstName
        
    def set_lastName(self,lastName):
        self.lastName = lastName
        
    def set_email(self,email):
        self.email = email
        
    def set_year(self,year):
        self.year = year
        
    def set_gpa(self,gpa):
        if float(gpa) > 4.0:
            print("Error! GPA can not exceed 4.0!")
            self.gpa = "4.0"
        else:
            self.gpa = gpa

def loadStudent(file_name):
    if os.path.isfile(file_name):
        input_file = open(file_name,'r')
    else:
        raise ValueError("Wrong input! The file doesn't exist!")
    students_array = []
    for i in input_file:
        i = i.strip('\n')
        a = i.split(',')
        if float(a[5]) > 4.0:
            a[5] = "4.0"
            print("Error! GPA can not exceed 4.0!")
            students_array.append(Student(a[0],a[1],a[2],a[3],a[4],a[5]))
        else:
            students_array.append(Student(a[0],a[1],a[2],a[3],a[4],a[5]))
    return students_array

def displayStudents(students_array):
    print('ID, firstName, lastName, email, year, gpa')
    for i in students_array:
        a=[]
        a.append(i.get_ID())
        a.append(i.get_firstName())
        a.append(i.get_lastName())
        a.append(i.get_email())
        a.append(i.get_year())
        a.append(i.get_gpa())
        c = ','.join(a)
        print(c)
        
def averageGPA(students_array):
    gpa_list=[]
    for i in students_array:
        gpa_list.append(float(i.get_gpa()))
    averageGPA = sum(gpa_list)/len(gpa_list)
    print(round(averageGPA,2))
    
def improveGPA(students_array,percentImprovement = 1.0):
    percent_adj=percentImprovement/100
    for i in range(len(students_array)):
        new_gpa = round(float(students_array[i].get_gpa())*(1+percent_adj),2)
        if new_gpa <= 4.0:
            students_array[i].set_gpa(str(new_gpa))
        else:
            students_array[i].set_gpa("4.0")
    return (students_array)
   
        
if __name__ == '__main__':
    loadStudent(args.inputfile)
    students_array = loadStudent(args.inputfile)
    displayStudents(students_array)
    averageGPA(students_array)
    improveGPA(students_array)
    averageGPA(students_array)
    
        
 