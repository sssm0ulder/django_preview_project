import faker
import random
import logging

from django.db import transaction

from .models import Person


def add_fake_data_to_database(n=50):
    logging.info("Добавление фейковых данных в базу данных...")

    fake = faker.Faker("ru_RU")["ru_RU"]

    with transaction.atomic():
        for _ in range(n):
            Person.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=random.randint(20, 55),
                company=fake.company()
            )

    logging.info("Данные добавлены.")
