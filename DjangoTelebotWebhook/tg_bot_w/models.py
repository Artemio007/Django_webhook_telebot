from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=10, null=True)
    user_id = models.CharField(max_length=10, null=True)
    phone_number = models.CharField(max_length=30, null=True, unique=True)
    vcard = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'user_db'

