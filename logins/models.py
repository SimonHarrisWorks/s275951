from django.db import models

# creates the stock table featuring stock id stock, name, price and quantity
class stock(models.Model):
    StockId = models.IntegerField()
    StockName =models.CharField(max_length=64)
    Price = models.DecimalField(decimal_places=2, max_digits=8)
    QTY = models.IntegerField()
    # defines the name of the what the information is under so stock id 10 with the stock name wood would just be seen as wood in admin
    # but all the details of wood will show when clicked on 
    def __str__(self):
        return self.StockName
    
# creates the customer table featuring first name, username, email, and password
class customer(models.Model):
    CFirstName = models.CharField(max_length=250)
    CUsername = models.CharField(max_length=250)
    CEmail = models.EmailField(max_length=255, default="example@example.com")
    CPassword = models.CharField(max_length=255, default="password1234")

    # each customer only uses there firstname but has other details when clicked
    def __str__(self):
        return self.CFirstName
    