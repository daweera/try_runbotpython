# Generated by Django 4.0.5 on 2022-07-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_reply_employee_lineid_alter_employee_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='lineid',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='namenotify',
            new_name='occupation',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='status',
            new_name='salary',
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('F', 'F'), ('M', 'M')], max_length=100, null=True),
        ),
    ]