from util import add_issue

def clean_employee_info(data: list, dept_ids: list[str]):
    exceptions = {}
    emp_ids = []

    size = len(data)
    for i in range(size):
        # ignore the schema
        if i == 0: continue

        emp = data[i]
        emp_id = emp[0]
        dept_id = emp[3]

        issues = []

        emp_id_missing = emp_id == ''
        emp_id_unique = emp_id_missing or emp_id not in emp_ids

        if emp_id_missing:
            add_issue(issues, "Employee ID", "Missing")
        elif not emp_id_unique:
            add_issue(issues, "Employee ID", "Not Unique")
        
        if dept_id == '':
            add_issue(issues, "Department_ID", "Missing")
        elif dept_id not in dept_ids:
            add_issue(issues, "Department_ID", "Non-Existent Department")
        
        if not emp_id_missing and emp_id_unique:
            emp_ids.append(emp_id)
        
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