# Generated by Django 4.2.2 on 2023-06-22 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_bot_w', '0003_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
