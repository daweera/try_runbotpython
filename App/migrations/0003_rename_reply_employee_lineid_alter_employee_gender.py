# Generated by Django 4.0.5 on 2022-06-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_employee_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='reply',
            new_name='lineid',
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
