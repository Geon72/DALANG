from django.db import models

class DepositProduct(models.Model):
    kor_co_nm = models.CharField(max_length=100)  # 은행명
    fin_prdt_nm = models.CharField(max_length=200)  # 상품명
    intr_rate_type = models.CharField(max_length=50)  # 저축 금리 유형 / 이자 계산방식
    save_trm = models.CharField(max_length=50) # 저축 기간 [단위: 개월]
    intr_rate = models.FloatField()  # 일반 금리
    intr_rate2 = models.FloatField()  # 우대 금리
    join_way = models.CharField(max_length=200)  # 가입 방법
    spcl_cnd = models.CharField(max_length=200)  # 특별 조건
    join_deny = models.CharField(max_length=200)  # 가입 제한 가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    join_member = models.CharField(max_length=200)  # 가입 대상
    etc_note = models.CharField(max_length=200)  # 기타 사항
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜

    def __str__(self):
        return f"{self.kor_co_nm} - {self.fin_prdt_nm}"
