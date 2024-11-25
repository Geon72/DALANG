import os
import django
import random

# Django 설정 초기화
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dalang.settings')
django.setup()

# Django 모델 import
from django.contrib.auth import get_user_model
from articles.models import Article, Comment

User = get_user_model()

def create_dummy_data():
    # 테스트용 사용자 생성
    users = []
    for i in range(10):
        user_data = {
            'username': f'testuser{i}',
            'email': f'test{i}@example.com',
            'age': random.randint(20, 60),
            'gender': random.choice([1, 2]),
            'salary': random.randint(2000, 10000) * 10000,
            'wealth': random.randint(10000, 50000) * 10000,
            'tendency': random.choice([1, 2, 3, 4, 5]),
            'marital_status': random.choice([0, 1]),
            'num_of_dependents': random.randint(0, 3),
            'employment_status': random.choice([0, 1]),
            'credit_score': random.randint(300, 900),
            'monthly_expense': random.randint(100, 500) * 10000,
            'investment_experience': random.choice([0, 1])
        }
        
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            email=user_data['email'],
            defaults=user_data
        )
        
        if created:
            user.set_password('testpass123')
            for field, value in user_data.items():
                if field not in ['username', 'email']:
                    setattr(user, field, value)
            user.save()
        users.append(user)

    # 테스트용 게시글 생성
    topics = ['Vue.js', 'React', 'Angular', 'Svelte', 'Node.js']
    tags = ['Frontend', 'Backend', 'DevOps', 'UI/UX', 'Testing']
    articles = []

    for i in range(30):
        article = Article.objects.create(
            title=f"{topics[i % len(topics)]}로 웹 애플리케이션 만들기 {i + 1}",
            content=f"{topics[i % len(topics)]}를 사용하여 현대적인 웹 애플리케이션을 구축하는 방법을 상세히 알아봅니다.",
            author=random.choice(users),
            hashtag1=random.choice(tags),
            hashtag2=random.choice(tags),
            hashtag3=random.choice(tags),
        )
        articles.append(article)

    # 좋아요 생성
    for article in articles:
        like_count = random.randint(0, min(10, len(users)))
        likers = random.sample(users, like_count)
        for liker in likers:
            article.likes.add(liker)

            
    # 댓글 생성
    for article in articles:
        comment_count = random.randint(0, 8)
        for _ in range(comment_count):
            comment = Comment.objects.create(
                article=article,
                author=random.choice(users),
                content=f"이 게시글에 대한 의견입니다. #{random.randint(1, 100)}"
            )
            comment_like_count = random.randint(0, 5)
            comment_likers = random.sample(users, comment_like_count)
            for liker in comment_likers:
                comment.likes.add(liker)

    print('Successfully created dummy data!')

if __name__ == '__main__':
    create_dummy_data()