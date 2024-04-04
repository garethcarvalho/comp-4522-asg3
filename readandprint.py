import csv
from department import clean_department_info
from student_counceling import clean_student_counceling_info
from student_performance import clean_student_performance_data
from employee import clean_employee_info

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
    dept_ids, exceptions = clean_department_info(dept_info)
    print("DEPARTMENT_DATA")
    for d in dept_info:
        print(d)
    return
    for e in exceptions:
        print(exceptions[e])
    # for i in range(0,29):
    #     print(mydata[i])
    # print("=============================================================================================")
    # # read COUNCIL data
    stu_coun_info = myreader('data/Student_Counceling_Information.csv')
    print("STUDENT_COUNCELING_DATA")
    print(len(stu_coun_info))
    student_ids, exceptions = clean_student_counceling_info(stu_coun_info, dept_ids)
    print(len(stu_coun_info))
    i = 0
    for e in exceptions:
        print(exceptions[e])
        i += 1
        if i > 29: break

    stu_perf_data = myreader('data/Student_Performance_Data.csv')
    exceptions = clean_student_performance_data(stu_perf_data, student_ids)
    print("STUDENT_PERFORMANCE_DATA")

    for e in exceptions:
        print(exceptions[e])

    # print("=============================================================================================")
    # # read EMPLOYEE data
    emp_info = myreader('data/Employee_Information.csv')
    print("EMPLOYEE_INFORMATION")
    exceptions = clean_employee_info(emp_info, dept_ids)
    for e in exceptions:
        print(exceptions[e])
    # for i in range(0,29):
    #     print(mydata[i])

        
main()
