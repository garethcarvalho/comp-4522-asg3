from util import add_issue

def clean_student_counceling_info(student_counceling: list, department_ids: list):
    student_ids = [int]
    exceptions = {}

    size = len(student_counceling)
    for i in range(size):
        if i == 0: continue

        stu = student_counceling[i]

        student_id = int(stu[0][3:])
        student_counceling[i][0] = student_id

        dept_choice = stu[3]
        dept_admission = stu[4]        
        
        issues = []

        student_id_unique = True

        if not student_id:
            add_issue(issues, "Student_ID", "Missing")
        elif student_id in student_ids:
            student_id_unique = False
            add_issue(issues, "Student_ID", "Not Unique")
        
        if not dept_choice:
            add_issue(issues, "Department_Choices", "Missing")
        elif dept_choice not in department_ids:
            add_issue(issues, "Department_Choice", "Non-Existent Department")

        if not dept_admission:
            add_issue(issues, "Department_Admission", "Missing")
        elif dept_admission not in department_ids:
            add_issue(issues, "Department_Admission", "Non-Existent Department")

        if issues:
            exceptions[i] = {
                "index": i,
                "issues": issues,
                "action": "Removed"
            }

        if student_id != '' and student_id_unique:
            student_ids.append(student_id)

    for i in range(size - 1, -1, -1):
        if i in exceptions:
            student_counceling.pop(i)

    return student_ids, exceptions
