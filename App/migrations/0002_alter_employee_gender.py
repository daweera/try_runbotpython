# Generated by Django 4.0.5 on 2022-06-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('Other', 'Other'), ('F', 'F'), ('M', 'M')], max_length=100, null=True),
        ),
    ]
