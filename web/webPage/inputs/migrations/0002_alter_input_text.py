# Generated by Django 4.1.3 on 2022-11-13 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='text',
            field=models.TextField(),
        ),
    ]
