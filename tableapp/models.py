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
class table_gold_dinar(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class table_price_market(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class price_numper(models.Model):
    numper=models.FloatField(default=1)
    

class name_table(models.Model):
    name=models.CharField(max_length=50)
    

