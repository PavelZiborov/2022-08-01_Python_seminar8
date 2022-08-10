import json

person_data = 'person.json'
company_data = 'company.json'
department_data = 'department.json'
job_data = 'job.json'
summary = 'summary.json'


def PrintData(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        BD = json.load(file)
        for i in BD:
            for key, value in i.items():
                print("{}: {}".format(key, value))
            print('\n')


def PrintSummary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        BD = json.load(file)

        with open(person_data, 'r', encoding='utf-8') as file:
            PD = json.load(file)
        with open(company_data, 'r', encoding='utf-8') as file:
            CD = json.load(file)
        with open(department_data, 'r', encoding='utf-8') as file:
            DD = json.load(file)
        with open(job_data, 'r', encoding='utf-8') as file:
            JD = json.load(file)

        for i in BD:

            for key, value in i.items():
                if key == 'id':
                    print("{}: {}".format(key, value))

            for key, value in i.items():
                if key == 'id_person':
                    for j in PD:
                        if j['id'] == value:
                            value = j['name']
                    print("{}: {}".format(key, value))

                elif key == 'id_company':
                    for j in CD:
                        if j['id'] == value:
                            value = j['name']
                    print("{}: {}".format(key, value))

                elif key == 'id_department':
                    for j in DD:
                        if j['id'] == value:
                            value = j['name']
                    print("{}: {}".format(key, value))

                elif key == 'id_job':
                    for j in JD:
                        if j['id'] == value:
                            value = j['name']
                    print("{}: {}".format(key, value))
            print('\n')