# Generated by Django 2.2.13 on 2020-07-04 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('email',)},
        ),
    ]
