# Generated by Django 4.2.7 on 2023-11-29 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='spec',
        ),
        migrations.AddField(
            model_name='mydoctor',
            name='spec',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
