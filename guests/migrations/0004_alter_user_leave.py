# Generated by Django 3.2.8 on 2021-10-28 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0003_alter_user_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='leave',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
