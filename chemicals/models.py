from django.db import models

# Create your models here.
# models.py


class Chemicals(models.Model):
    chemical_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.chemical_name

class PurchasedDetails(models.Model):
    chem_name = models.ForeignKey(Chemicals,on_delete=models.CASCADE)
    Purchased_date = models.DateField(null=True,blank=True)
    Bill_no = models.CharField(max_length=100,null=True,blank=True)
    Rate = models.IntegerField(null=True,blank=True)
    Quantity_purchased = models.IntegerField(null=True,blank=True)
    Balance =  models.IntegerField(null=True,blank=True)
    
class Utensils(models.Model):
    uten_id = models.SmallIntegerField(unique=True)
    uten_name = models.CharField(max_length=100, unique=True)
    uten_location = models.SmallIntegerField(null=True)
    price = models.IntegerField(default=0)  
    quantity = models.IntegerField(default=0) 

    def __str__(self):
        return self.uten_name

class Fine(models.Model):
    dept = [
        ('chemistry', 'Chemistry'),
        ('physics', 'Physics'),
        ('zoology', 'Zoology'),
        ('botony', 'Botony')
    ]
    yr = [
        (1, 'I year'),
        (2, 'II year'),
        (3, 'III year')
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('received', 'Received'),
    ]
    admn_no = models.IntegerField(null=False)
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField(max_length=100)
    Department = models.CharField(max_length=100, choices=dept)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    Year = models.SmallIntegerField(choices=yr, null=True, blank=True)
    Item = models.ForeignKey(Utensils, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)


    def __str__(self):
        return self.Name

    @property
    def Price(self):
        return self.Item.price