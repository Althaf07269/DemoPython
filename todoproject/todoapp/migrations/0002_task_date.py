# Generated by Django 4.2.6 on 2023-10-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2002-01-07'),
            preserve_default=False,
        ),
    ]
