from django.db import models
class complain(models.Model):
    complain_id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=30)
    Category=models.CharField(max_length=50)
    Phone_no=models.IntegerField()
    Address=models.CharField(max_length=50)
    def __str__(self):
        return self.Name

# Create your models here.
