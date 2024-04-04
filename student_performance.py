from util import add_issue

def clean_student_performance_data(data: list, student_ids: list[int]):
    size = len(data)

    paper_lookup = {}
    exceptions = {}

    for i in range(size):
        if i == 0: continue
        perf_data = data[i]

        student_id = int(perf_data[0][3:])
        data[i][0] = student_id
        paper_id = perf_data[2]
        marks = perf_data[4]
        effort = perf_data[5]

        issues = []   

        if student_id == '':
            add_issue(issues, "Student_ID", "Missing")
        elif student_id not in student_ids:
            add_issue(issues, "Student_ID", "Non-Existent Student ID")
        
        if student_id in paper_lookup:
            if paper_id in paper_lookup[student_id]:
                add_issue(issues, "Student_ID and Paper_ID", "Mark for this paper already exists")
            else:
               paper_lookup[student_id].append(paper_id)
        else:
            paper_lookup[student_id] = [paper_id]
        
        if not marks:
            add_issue(issues, "Marks", "Missing")
        else:
            marks = int(marks)
            if marks > 100 or marks < 0:
                add_issue(issues, "Marks", f"Value out of range of 0-100: Value was {marks}")

        if not effort:
            add_issue(issues, "Effort_Hours", "Missing")
        else:
            effort = int(effort)
            if effort < 0 or effort > 100:
                add_issue(issues, "Effort_Hours", f"Invalid amount of hours: Value was {effort}")

        if issues:
            exceptions[i] = {
                "index": i,
                "issues": issues,
                "action": "Removed"
            }
    
    for i in range(size - 1, -1, -1):
        if i in exceptions:
            data.pop(i)
    return exceptions