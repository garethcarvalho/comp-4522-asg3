import csv
import department_info as dept

def myreader(filename: str) -> list:
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        return your_list

def mywriter(filename: str, mylist: list):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write multiple rows
        writer.writerows(mylist)

def main():
    # # read PERFORMANCE data
    # mydata = myreader('Student_Performance_Data.csv')
    # print("STUDENT_PERFORMANCE_DATA")
    # for i in range(0,29):
    #     print(mydata[i])
    # print("=============================================================================================")
    # # read DEPT data
    mydata = myreader('data/Department_Information.csv')
    exceptions = dept.validate_dept_info(mydata)
    for i in range(len(exceptions)):
        print(exceptions[i])
    # print("DEPARTMENT_DATA")
    # for i in range(0,29):
    #     print(mydata[i])
    # print("=============================================================================================")
    # # read COUNCIL data
    # mydata = myreader('data/Student_Counceling_Information.csv')
    # print("STUDENT_COUNCELING_DATA")
    # for i in range(0,29):
    #     print(mydata[i])
    # print("=============================================================================================")
    # # read EMPLOYEE data
    # mydata = myreader('data/Employee_Information.csv')
    # print("EMPLOYEE_INFORMATION")
    # for i in range(0,29):
    #     print(mydata[i])

        
main()
