# Generated by Django 2.2.10 on 2021-11-11 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poles_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.IntegerField(),
        ),
    ]