
from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='course/', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    user = models.ForeignKey(User, verbose_name='владелец', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='lesson/', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    url = models.URLField(max_length=250, verbose_name='ссылка на видео урок', **NULLABLE)
    course = models.ForeignKey(Course, verbose_name='курс', on_delete=models.CASCADE, related_name="lessons", **NULLABLE)
    user = models.ForeignKey(User, verbose_name='владелец', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    CHOICES = (
        ("Card", "карта"),
        ("CASH", "наличка"),
    )
    user = models.ForeignKey(User, verbose_name='владелец', on_delete=models.CASCADE, **NULLABLE)
    date_of_pay = models.DateTimeField(auto_now_add=True, **NULLABLE)
    item = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE)
    lesson_name = models.ForeignKey(Lesson, on_delete=models.SET_NULL, **NULLABLE)
    cash = models.PositiveIntegerField()
    payment_method = models.CharField(choices=CHOICES, verbose_name="тип оплаты")

    def str(self):
        return f"{self.user} {self.item}"

    class Meta:
        verbose_name = "оплата"
        verbose_name_plural = "оплаты"