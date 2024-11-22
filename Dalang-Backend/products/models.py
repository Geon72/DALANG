from django.db import models
from django.conf import settings
# Create your models here.

class DepositProduct(models.Model):
    interest_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='interest_deposit')
    dcls_month = models.TextField()
    fin_prdt_cd = models.TextField()
    fin_co_no = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    join_way = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.IntegerField(default=0)
    join_member = models.TextField()
    etc_note = models.TextField()
    max_limit = models.IntegerField(blank=True, null=True)

class SavingProduct(models.Model):
    interest_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='interest_saving')
    dcls_month = models.TextField()
    fin_prdt_cd = models.TextField()
    fin_co_no = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    join_way = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.IntegerField(default=0)
    join_member = models.TextField()
    etc_note = models.TextField()
    max_limit = models.IntegerField(blank=True, null=True)

class DepositOption(models.Model):
    # fin_prdt_cd = models.IntegerField()
    deposit_product = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
    intr_rate_type = models.CharField(max_length=100)
    intr_rate_type_nm = models.CharField(max_length=100)    
    save_trm = models.IntegerField(default=0)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)

class SavingOption(models.Model):
    # fin_prdt_cd = models.IntegerField()
    saving_product = models.ForeignKey(SavingProduct, on_delete=models.CASCADE)
    intr_rate_type = models.CharField(max_length=100)
    intr_rate_type_nm = models.CharField(max_length=100)
    rsrv_type = models.TextField()
    rsrv_type_nm = models.TextField()
    save_trm = models.IntegerField()
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)