from util import add_report

def validate_dept_info(dept_info: list) -> list:
    # Keep track of IDs and names to keep uniqueness
    ids = []
    names = []
    exceptions = []

    size = len(dept_info)
    for i in range(size):
        # ignore the schema
        if i == 0: continue

        dept = dept_info[i]
        dept_id = dept[0]
        dept_name = dept[1]
        doe = dept[2]

        issues = []

        validate_dept_id(ids, dept_id, issues)
        validate_dept_name(names, dept_name, issues)
        validate_doe(doe, issues)
        
        if issues:
            exceptions.append({
                "index": i,
                "issues": issues
            })
        
        ids.append(dept_id)
        names.append(dept_name)
    
    return exceptions

def validate_dept_name(names: list, dept_name: str, reports: list):
    if not dept_name:
            # Department_Name is missing
        add_report(reports, "Department_Name", "Missing")

    elif dept_name in names:
            # Department_Name is not unique
        add_report(reports, "Department_Name", "Not Unique")


def validate_dept_id(ids: list, dept_id: str, reports: list):
    if not dept_id:
            # Department_ID is missing
        add_report(reports, "Department_ID", "Missing")
    elif dept_id in ids:
            # Department_ID is not unique
        add_report(reports, "Department_ID", "Not Unique")

def validate_doe(doe: str, reports: list):
    if not doe:
        add_report(reports, "DOE", "Missing")
        return
    
    year = int(doe.split('/')[2])
    if (year < 1900):
        add_report(reports, "DOE", f"Invalid Date: {year}")

