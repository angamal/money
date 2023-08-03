from django.db import models


class Formss(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.TextField(choices=[('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')])
    phone_number = models.CharField(max_length=250)
    email = models.EmailField()
    address=models.TextField()
    district = models.TextField(choices=[('ernamkulam', 'Ernamkulam'),('thrissur', 'Thrissur'),  ('kottayam', 'Kottayam'), ('alappuzha', 'Alappuzha'),('idukki' ,'Idukki')])
    account_type = models.TextField(choices=[('savings', 'Savings'), ('current', 'Current')])
    branch = models.TextField(choices=[('aluva','Aluva'),('edapally','edapally'),('angamaly','Angamaly'),('paravur','Paravur')])
    materials_required = models.TextField(choices=[('debit', 'Debit Card'), ('credit', 'Credit Card'), ('cheque', 'Chequebook')])

def __str__(self):
    return self.name

