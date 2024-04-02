def validate_dept_info(dept_info: list):
    # validate Department_ID
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

        reports = []

        validate_dept_id(ids, dept_id, reports)
        validate_dept_name(names, dept_name, reports)
        validate_doe(doe, reports)
        
        if reports:
            exceptions.append({
                "index": i,
                "reports": reports
            })

def validate_dept_name(names: list, dept_name: str, reports: list):
    if dept_name:
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
    pass

def add_report(reports: list, attribute: str, report: str):
    reports.append({
        "attribute": attribute,
        "report": report
    })