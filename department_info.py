from util import add_report

def validate_dept_info(dept_info: list) -> list:
    # Keep track of IDs and names to keep uniqueness
    ids = []
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
        dept_id_unique = dept_id_missing or dept_id not in ids
        dept_name_unique = dept_name_missing or dept_name not in names
        is_duplicate = not dept_id_unique and not dept_name_unique

        if is_duplicate:
            add_report(issues, "Department_ID and Department_Name", "Duplicate Entry")
        else:
            if not dept_id_unique:
                add_report(issues, "Department_ID", "Not Unique")
            if not dept_name_unique:
                add_report(issues, "Department_Name", "Not Unique")

    
        if dept_id_missing:
            add_report(issues, "Department_ID", "Missing")
        if dept_name_missing:
            add_report(issues, "Department_Name", "Missing")
        
        if not doe:
            add_report(issues, "DOE", "Missing")
        else:
            year = int(doe.split('/')[2])
            if (year < 1900):
                add_report(issues, "DOE", f"Invalid Date: {year}")
            
        if issues:
            # exceptions.append({
            #     i: {
            #         "issues": issues,
            #         "action taken": "Removed"
            #     }
            # })
            exceptions[i] = {
                "index": i,
                "issues": issues,
                "action": "Removed"
            }
        
        ids.append(dept_id)
        names.append(dept_name)

    # Remove the problem data.
    for i in range(size - 1, -1, -1):
        if i in exceptions:
            dept_info.pop(i)
    return exceptions