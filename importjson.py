import json
from administrator.models import Student

with open('students-gr1.json') as f:
    students_json = json.load(f)

for student in students_json:
    student = Student(first_name=student['first_name'].upper(), middle_name=student['middle_name'].upper(), last_name=student['last_name'].upper(), lrn=student['lrn'], sex=student['sex'], birthdate=student['birthdate'], section_id=student['section_id'], guardian_name=student['guardian_name'], contact_number=student['contact_number'], remarks=student['remarks'])
    try:
        student.save()
    except:
        continue
