import json


def data_extract(content):
    company_array = []
    json_obj = json.loads(content)
    companies = json_obj["content"]["positionResult"]["result"]
    for company in companies:
        company_array.append(company['companyFullName'])
    return company_array
