# Generated by Django 4.1.7 on 2023-03-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_restaurant_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='review',
            field=models.CharField(default='good place to eat', max_length=200),
            preserve_default=False,
        ),
    ]
