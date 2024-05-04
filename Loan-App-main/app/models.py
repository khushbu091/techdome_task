from django.db import models

class Customer(models.Model):
    access = [('General','General'),('Admin','Admin')]
    user = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(default=None)
    phone = models.IntegerField(max_length=10, verbose_name='Contact No.', default=None)
    access = models.CharField(max_length=10, choices=access, default='General')

    def __str__(self):
        return self.user
class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.IntegerField()
    state = models.CharField(max_length=20, default='PENDING')

    def __str__(self):
        return self.customer.user

class Repayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = models.CharField(max_length=20, default='PENDING')