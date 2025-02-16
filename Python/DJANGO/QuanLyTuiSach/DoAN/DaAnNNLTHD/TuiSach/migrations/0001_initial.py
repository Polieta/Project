# Generated by Django 5.0.4 on 2024-05-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=100)),
                ('customer_phone', models.CharField(max_length=100)),
                ('customer_address', models.CharField(max_length=100)),
                ('customer_password', models.CharField(max_length=100)),
                ('customer_status', models.BooleanField()),
                ('customer_sex', models.CharField(max_length=100)),
                ('customer_role', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
    ]
