# Generated by Django 4.2.5 on 2023-09-08 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splittify', '0002_alter_bill_owers_alter_bill_payer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='name',
        ),
    ]
