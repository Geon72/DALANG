import random
from django.core.management.base import BaseCommand
from accounts.models import User

class Command(BaseCommand):
    help = 'Create 10,000 dummy users for testing'

    def handle(self, *args, **kwargs):
        users = []
        for i in range(10000):
            username = f'user_{i}'
            age = random.randint(18, 80)
            gender = random.choice([1, 2])
            salary = random.randint(30000, 100000)
            wealth = random.randint(10000, 500000)
            tendency = random.choice([1, 2, 3, 4, 5])

            user = User(
                username=username,
                age=age,
                gender=gender,
                salary=salary,
                wealth=wealth,
                tendency=tendency
            )
            users.append(user)

        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('Successfully created 10,000 dummy users'))
