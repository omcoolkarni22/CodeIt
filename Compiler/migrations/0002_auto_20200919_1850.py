# Generated by Django 3.0 on 2020-09-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codes',
            name='files',
            field=models.FileField(null=True, upload_to='files/', verbose_name=''),
        ),
    ]
