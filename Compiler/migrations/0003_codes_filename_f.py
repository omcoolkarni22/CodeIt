# Generated by Django 3.0 on 2020-09-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compiler', '0002_auto_20200919_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='codes',
            name='filename_f',
            field=models.CharField(default='FileName', max_length=50, null=True),
        ),
    ]
