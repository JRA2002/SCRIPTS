import os
import django
import random
from faker import Faker

#define setup from django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

#import models to fill data
from hospital.models import Patients, Province

#create a function
def populate(n=1000):
    #create an object
    fake = Faker()
    #fill every attribute
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        birth_date = fake.date_of_birth()
        gender = random.choice(['Male', 'Female', 'Other'])
        city = fake.city()
        province_name = random.choice(Province.objects.all())
        allergies = random.choice([
        'None',
        'Pollen',
        'Dust',
        'Cat scratch',
        'Dust',
        'Cat scratch',
        'Other',
    ])
        weight = random.randint(30, 200)
        height = random.randint(10, 200)

        #add to database
        Patients.objects.create(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            gender=gender,
            city=city,
            province_name=province_name,
            allergies=allergies,
            weight=weight,
            height=height
        )

if __name__ == '__main__':
    print("Populating the database with fake data...")
    populate()
    print("Done!")
