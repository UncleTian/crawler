import json


# extract company name from return json data
def extract_company_name(content):
    company_array = []
    json_obj = json.loads(content)
    companies = json_obj["content"]["positionResult"]["result"]
    for company in companies:
        company_array.append(company['companyFullName'])
    return company_array
