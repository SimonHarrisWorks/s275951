from django.contrib import admin
from .models import stock,customer
# The code are basic imports so that below the admin site in Django for the website can edit customers and stock 
admin.site.register(stock)
admin.site.register(customer)