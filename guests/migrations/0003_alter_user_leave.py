# Generated by Django 3.2.8 on 2021-10-28 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0002_auto_20211019_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='leave',
            field=models.DateTimeField(),
        ),
    ]
