from django.db import models


class Person(models.Model):
    SHIRT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE)
    # age1 관리자 페이지에서 빈값을 허용하지만 DB에서 빈 값을 허용하지 않음
    age1 = models.IntegerField(blank=True)
    # age2 는 DB에는 빈값을 허용하지만 관리자 페이지에서 빈 값을 허용하지 않음
    age2 = models.IntegerField(null=True)
    # 둘다 허용, 빈 값을 넣어도 이상없이 작동한다
    age3 = models.IntegerField(blank=True, null=True)
