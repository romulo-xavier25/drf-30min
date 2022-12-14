# Generated by Django 4.1.2 on 2022-11-17 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='valor',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product')),
            ],
        ),
    ]
