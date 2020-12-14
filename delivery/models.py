from django.db import models
from django.urls import reverse

class Personnel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=20, null=True, verbose_name='Отчество')
    post = models.CharField(max_length=20, verbose_name='Должность')
    serial_pas = models.IntegerField()
    num_pas = models.IntegerField()
    address = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=20, verbose_name='Номер телефона')

    def __str__(self):
        template = '{0.first_name} {0.last_name} {0.patronymic}'
        return template.format(self)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    artikul = models.IntegerField()
    product_name = models.CharField(max_length=20)
    composition = models.CharField(max_length=255)
    cost_one = models.IntegerField()
    amount = models.IntegerField()
    expiration_date = models.DateTimeField()
    description = models.CharField(max_length=100)

    def __str__(self):
        template = '{0.product_name}'
        return template.format(self)



class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Order_product(models.Model):
    id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, default=False)
    amount = models.IntegerField()
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE, default=False)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=False)
    def __str__(self):
        template = '{0.id} {0.product} {0.amount} {0.supplier} {0.personnel}'
        return template.format(self)


class Product_supply(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order_product, on_delete=models.DO_NOTHING, default=False)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=False)
    supply_date = models.DateField(auto_now_add=True)
    supply_time = models.TimeField(auto_now_add=True)
    quantity = models.IntegerField()
    personnel = models.ForeignKey(Personnel, on_delete=models.DO_NOTHING, default=False )

    def save(self, *args, **kwargs):
        a = Product.objects.get(product_name=self.product)
        a.amount += self.quantity
        a.save()
        super().save(*args, **kwargs)


    def __str__(self):
        template = '{0.id} ||| {0.order} ||| {0.quantity} {0.personnel} {0.product} {0.product.amount}'
        return template.format(self)


class Product_sale(models.Model):
    id = models.AutoField(primary_key=True)
    personnel = models.ForeignKey(Personnel, on_delete=models.DO_NOTHING, default=False)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=False)
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        a = Product.objects.get(product_name=self.product)
        a.amount -= self.count
        a.save()
        super().save(*args, **kwargs)


    def __str__(self):
        template = '{0.product} {0.count} {0.personnel} {0.date}'
        return template.format(self)


class Salary(models.Model):
    id = models.AutoField(primary_key=True)
    personnel = models.OneToOneField(Personnel, on_delete=models.CASCADE, default=False)
    salary = models.IntegerField()
    prize = models.IntegerField()
    prepayment = models.IntegerField(null=True)

    def __str__(self):
        template = '{0.personnel}'
        return template.format(self)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    serial_pas_c = models.IntegerField()
    number_pas_c = models.IntegerField()
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=20, verbose_name='Отчество')
    address = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=20)

    def __str__(self):
        template = '{0.first_name} {0.last_name}'
        return template.format(self)


class Pharmacy_expense(models.Model):
    id = models.AutoField(primary_key=True)
    months = (
        ('1-JAN', 'January'),
        ('2-FEB', 'February'),
        ('3-MAR', 'March'),
        ('4-APR', 'April'),
        ('5-MAY', 'May'),
        ('6-JUN', 'June'),
        ('7-JUL', 'July'),
        ('8-AUG', 'August'),
        ('9-SEP', 'September'),
        ('10-OCT', 'October'),
        ('11-NOV', 'November'),
        ('12DEC', 'December'),
        )
    month = models.CharField(choices=months, max_length=20)
    year = models.IntegerField()
    rent = models.IntegerField()
    utilities = models.IntegerField()
    advertising = models.IntegerField()
    inner_expenses = models.IntegerField()
    total_expense = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total_expense = self.rent + self.utilities + self.advertising + self.inner_expenses
        super().save(*args, **kwargs)

    def __str__(self):
        template = '{0.month} {0.year}'
        return template.format(self)


class Pharmacy_income(models.Model):
    id = models.AutoField(primary_key=True)
    months = (
        ('1-JAN', 'January'),
        ('2-FEB', 'February'),
        ('3-MAR', 'March'),
        ('4-APR', 'April'),
        ('5-MAY', 'May'),
        ('6-JUN', 'June'),
        ('7-JUL', 'July'),
        ('8-AUG', 'August'),
        ('9-SEP', 'September'),
        ('10-OCT', 'October'),
        ('11-NOV', 'November'),
        ('12DEC', 'December'),
        )
    month = models.CharField(choices=months, max_length=20)
    year = models.IntegerField()
    personnel_income = models.IntegerField()

    def __str__(self):
        template = '{0.month} {0.year}'
        return template.format(self)



class Accounting(models.Model):
    id = models.AutoField(primary_key=True)
    month_i = models.OneToOneField(Pharmacy_income, on_delete=models.DO_NOTHING, default=False)
    month_e = models.OneToOneField(Pharmacy_expense, on_delete=models.DO_NOTHING, default=False)
    total_number = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total_number += self.month_i.personnel_income - self.month_e.total_expense
        super().save(*args, **kwargs)

    def __str__(self):
        if str(self.month_i) == str(self.month_e):
            template = 'Дата:{0.month_i} ||| Общий доход:{0.total_number}'
            return template.format(self)
        else:
            return 'Incorrect input'
