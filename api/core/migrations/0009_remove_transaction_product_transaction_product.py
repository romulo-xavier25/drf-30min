# Generated by Django 4.1.2 on 2022-11-30 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_transaction_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='product',
        ),
        migrations.AddField(
            model_name='transaction',
            name='product',
            field=models.ManyToManyField(to='core.product'),
        ),
    ]
