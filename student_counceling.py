from util import add_report

def validate_student_counceling(student_counceling: list, department_ids: list):
    student_ids = []
    exceptions = {}

    size = len(student_counceling)
    for i in range(size):
        if i == 0: continue

        stu = student_counceling[i]
        student_id = stu[0]
        dept_choice = stu[3]
        dept_admission = stu[4]        
        
        issues = []

        student_id_unique = True

        if not student_id:
            add_report(issues, "Student_ID", "Missing")
        elif student_id in student_ids:
            student_id_unique = False
            add_report(issues, "Student_ID", "Not Unique")
        
        if not dept_choice:
            add_report(issues, "Department_Choices", "Missing")
        elif dept_choice not in department_ids:
            add_report(issues, "Department_Choice", "Non-Existent Department")

        if not dept_admission:
            add_report(issues, "Department_Admission", "Missing")
        elif dept_admission not in department_ids:
            add_report(issues, "Department_Admission", "Non-Existent Department")

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

    return exceptions
