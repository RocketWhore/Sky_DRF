# Generated by Django 4.2.4 on 2023-09-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='cash',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='сумма оплаты'),
        ),
    ]
