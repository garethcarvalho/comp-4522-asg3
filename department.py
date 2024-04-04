from util import add_issue

def clean_department_info(dept_info: list):
    # Keep track of IDs and names to keep uniqueness
    dept_ids = []
    names = []
    exceptions = {}

    size = len(dept_info)
    for i in range(size):
        # ignore the schema
        if i == 0: continue

        dept = dept_info[i]
        dept_id = dept[0]
        dept_name = dept[1]
        doe = dept[2]

        issues = []

        # bunch of bools to keep track of attributes
        dept_id_missing = dept_id == ''
        dept_name_missing = dept_name == ''
        dept_id_unique = dept_id_missing or dept_id not in dept_ids
        dept_name_unique = dept_name_missing or dept_name not in names
        is_duplicate = not dept_id_unique and not dept_name_unique

        if is_duplicate:
            add_issue(issues, "Department_ID and Department_Name", "Duplicate Entry")
        else:
            if not dept_id_unique:
                add_issue(issues, "Department_ID", "Not Unique")
            if not dept_name_unique:
                add_issue(issues, "Department_Name", "Not Unique")

    
        if dept_id_missing:
            add_issue(issues, "Department_ID", "Missing")
        if dept_name_missing:
            add_issue(issues, "Department_Name", "Missing")
        
        if not doe:
            add_issue(issues, "DOE", "Missing")
        else:
            year = int(doe.split('/')[2])
            if (year < 1900):
                add_issue(issues, "DOE", f"Invalid Date: {year}")
            
        if issues:
            exceptions[i] = {
                "index": i,
                "issues": issues,
                "action": "Removed"
            }
        
        if dept_id_unique and not dept_id_missing:
            dept_ids.append(dept_id)
        if dept_name_unique and not dept_name_missing:
            names.append(dept_name)

    # Remove the problem data.
    for i in range(size - 1, -1, -1):
        if i in exceptions:
            dept_info.pop(i)
    
    return dept_ids, exceptions