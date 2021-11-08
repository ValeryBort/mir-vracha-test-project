from faker import Faker
import requests

BASE_URL = 'https://test.mirvracha.ru/'
ROLE_STUDENT = 4
URL_PATIENT = 'patient'
CITY = 'Волгоград'
COUNTRY = 'Российская Федерация'
FINISH_DATE = '2021'
FIRST_NAME = 'Сальвадор'
LAST_NAME = 'Дали'
MIDDLE_NAME = 'Сальвадорович'
REGION = 'Волгоградская область'
TEST_RESULT = 'false'
UNIVERSITY = 'Алтайский гос. мед. университет'

def test_registration(faker):
    email = faker.ascii_company_email()

    continue_registration = requests.post(BASE_URL + 'front/auth/continueRegistration', data={
        'email': email,
        'url': URL_PATIENT,
        'roleId': ROLE_STUDENT
    })

    continue_registration.raise_for_status()

    student_id = {'file': open('student_id.pdf', 'rb')}

    save = requests.post(BASE_URL + 'front/picture/save', files=student_id)
    save.raise_for_status()

    diploma_id = save.json()['id']

    complete_registration = requests.post(BASE_URL + 'auth/continueRegistration/student', data={
        'city': CITY,
        'country': COUNTRY,
        'diplomaId': diploma_id,
        'email': email,
        'finishDate': FINISH_DATE,
        'firstName': FIRST_NAME,
        'lastName': LAST_NAME,
        'middleName': MIDDLE_NAME,
        'region': REGION,
        'role': ROLE_STUDENT,
        'testResult': TEST_RESULT,
        'university': UNIVERSITY
    })

    assert complete_registration.status_code == 200
