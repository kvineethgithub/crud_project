# Generated by Django 2.2.1 on 2019-05-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_remove_employee_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_pic',
            field=models.FileField(upload_to='images/%Y/%m/%d/%h/%i/%s'),
        ),
    ]
