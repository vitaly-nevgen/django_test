# Generated by Django 2.0.1 on 2018-08-31 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
