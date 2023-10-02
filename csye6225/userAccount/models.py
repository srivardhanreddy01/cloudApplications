from django.db import models
from datetime import datetime

# Create your models here.

class UserAccount(models.Model):
    class Meta:
        db_table = 'user_accounts'
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    account_created = models.DateTimeField(default=datetime.utcnow)
    account_updated = models.DateTimeField(default=datetime.utcnow)

    # def __init__(self, first_name, last_name, email, password):
    #     super().__init__()
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self.password = password
    def __str__(self):
        return self.email