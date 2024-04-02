import csv
from department_info import validate_dept_info
from student_counceling import validate_student_counceling

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
    # mydata = myreader('data/Student_Performance_Data.csv')
    # print("STUDENT_PERFORMANCE_DATA")
    # for i in range(0,29):
    #     print(mydata[i])
    # print("=============================================================================================")
    # # read DEPT data
    dept_info = myreader('data/Department_Information.csv')
    report = validate_dept_info(dept_info)

    dept_ids = report[0]
    exceptions = report[1]
    for e in exceptions:
        print(exceptions[e])
    # print("DEPARTMENT_DATA")
    # for i in range(0,29):
    #     print(mydata[i])
    # print("=============================================================================================")
    # # read COUNCIL data
    stu_coun_info = myreader('data/Student_Counceling_Information.csv')
    print(len(stu_coun_info))
    stu_coun_exceptions = validate_student_counceling(stu_coun_info, dept_ids)
    print(len(stu_coun_info))

    # print("STUDENT_COUNCELING_DATA")
    i = 0
    for e in stu_coun_exceptions:
        print(stu_coun_exceptions[e])
        i += 1
        if i > 29: break

    # print("=============================================================================================")
    # # read EMPLOYEE data
    # mydata = myreader('data/Employee_Information.csv')
    # print("EMPLOYEE_INFORMATION")
    # for i in range(0,29):
    #     print(mydata[i])

        
main()
