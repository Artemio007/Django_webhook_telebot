# Generated by Django 4.2.2 on 2023-06-22 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('user_id', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=30)),
                ('vcard', models.CharField(max_length=30)),
            ],
        ),
    ]
