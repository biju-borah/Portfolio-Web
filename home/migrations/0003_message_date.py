# Generated by Django 3.2.1 on 2021-06-06 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210606_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateField(default=datetime.date(2021, 6, 6)),
        ),
    ]