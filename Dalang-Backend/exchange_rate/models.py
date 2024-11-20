from django.db import models

class ExchangeRate(models.Model):
    currency_unit = models.CharField(max_length=10)  # 통화 코드
    exchange_rate = models.FloatField()              # 환율
    date = models.DateField()                        # 날짜

    def __str__(self):
        return f"{self.currency_unit} - {self.date}"