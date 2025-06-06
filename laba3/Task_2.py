import csv
from Task_1 import Person

def modifier(filename):
    persons = []

    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        p = Person(
            surname=row['surname'],
            first_name=row['name'],
            birth_date_str=row['birth_date'],
            nickname=row.get('nickname', None)
        )
        row['fullname'] = p.get_fullname()
        row['age'] = p.get_age()
        persons.append(row)

    fieldnames = list(rows[0].keys())
    if 'fullname' not in fieldnames:
        fieldnames.insert(fieldnames.index('name') + 1, 'fullname')
    if 'age' not in fieldnames:
        fieldnames.append('age')

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(persons)
    
modifier("data.csv")
print("Файл успішно змінено.")
