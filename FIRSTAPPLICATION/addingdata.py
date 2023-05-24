from faker import Faker
import random

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FIRSTPROJECT/FIRSTPROJECT.settings')
django.setup()
fake = Faker()
from models import Name, ID, Contact, Address

for _ in range(30):
    Name.objects.create(name=fake.name())
    ID.objects.create(unique_id=random.randint(1000, 9999))
    Contact.objects.create(contact=fake.phone_number())
    Address.objects.create(address=fake.address())

