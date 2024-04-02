from util import add_report

def validate_student_counceling(student_counceling: list, department_ids: list):

    student_ids = []
    exceptions = []

    size = len(student_counceling)
    for i in range(size):
        if i == 0: continue

        stu = student_counceling[i]
        student_id = stu[0]
        dept_choice = stu[3]
        dept_admission = stu[4]
        
        issues = []

        validate_student_id(student_ids, student_id, issues)
        validate_dept_choice(department_ids, dept_choice, issues)
        validate_dept_admission(department_ids, dept_admission, issues)

        if issues:
            exceptions.append({
                "index": i,
                "issues": issues
            })

    return exceptions

def validate_dept_admission(department_ids, dept_admission, issues):
    if not dept_admission:
        add_report(issues, "Department_Admission", "Missing")
    elif dept_admission not in department_ids:
        add_report(issues, "Department_Admission", "Non-Existent Department")

def validate_dept_choice(department_ids, dept_choice, issues):
    if not dept_choice:
        add_report(issues, "Department_Choices", "Missing")
    elif dept_choice not in department_ids:
        add_report(issues, "Department_Choice", "Non-Existent Department")

def validate_student_id(student_ids, student_id, issues):
    if not student_id:
        add_report(issues, "Student_ID", "Missing")
    elif student_id in student_ids:
        add_report(issues, "Student_ID", "Not Unique")
