# Generated by Django 4.1.3 on 2022-11-14 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('age', models.PositiveIntegerField(verbose_name='Age')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('id_company', models.CharField(max_length=255, verbose_name='Company code')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]