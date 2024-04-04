from pandas import DataFrame

def add_issue(issues: list, attribute: str, report: str):
    issues.append({
        "attribute": attribute,
        "issue": report
    })

def csv_to_dataframe(data: list) -> DataFrame:
    columns = data.pop(0)
    df = DataFrame(data, columns = columns)

    data.insert(0, columns)
    return df