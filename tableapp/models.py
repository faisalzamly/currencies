from django.db import models

# Create your models here.
class table_bank(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class table_price(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    


class table_gold(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
