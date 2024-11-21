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
            marital_status = random.choice([0, 1])  # 0: 미혼, 1: 기혼
            num_of_dependents = random.randint(0, 5)  # 부양가족 수
            employment_status = random.choice([0, 1])  # 0: 실업, 1: 고용
            credit_score = random.randint(300, 850)  # 신용 점수
            monthly_expense = random.randint(1000, 10000)  # 월평균 지출
            investment_experience = random.choice([0, 1])  # 0: 경험 없음, 1: 경험 있음

            user = User(
                username=username,
                age=age,
                gender=gender,
                salary=salary,
                wealth=wealth,
                tendency=tendency,
                marital_status=marital_status,
                num_of_dependents=num_of_dependents,
                employment_status=employment_status,
                credit_score=credit_score,
                monthly_expense=monthly_expense,
                investment_experience=investment_experience
            )
            users.append(user)

        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('Successfully created 10,000 dummy users'))




# import random
# from django.core.management.base import BaseCommand
# from accounts.models import User

# class Command(BaseCommand):
#     help = 'Create 10,000 dummy users for testing'

#     def handle(self, *args, **kwargs):
#         users = []
#         for i in range(10000):
#             username = f'user_{i}'
#             age = random.randint(18, 80)
#             gender = random.choice([1, 2])
#             salary = random.randint(30000, 100000)
#             wealth = random.randint(10000, 500000)
#             tendency = random.choice([1, 2, 3, 4, 5])

#             user = User(
#                 username=username,
#                 age=age,
#                 gender=gender,
#                 salary=salary,
#                 wealth=wealth,
#                 tendency=tendency
#             )
#             users.append(user)

#         User.objects.bulk_create(users)
#         self.stdout.write(self.style.SUCCESS('Successfully created 10,000 dummy users'))
