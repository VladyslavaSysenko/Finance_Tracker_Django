from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"id:{self.id} | username:{self.username}" 


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"id:{self.id} | code:{self.code} | symbol: {self.symbol} | name: {self.name}"  


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    name = models.CharField(max_length=20)
    dflt_curr_code = models.ForeignKey(Currency, to_field="code", on_delete=models.DO_NOTHING, related_name="accounts", verbose_name="default currency code")
   
    def __str__(self):
        return f"id:{self.id} | name:{self.name} | dflt_curr_code: {self.dflt_curr_code}" 


class Category(models.Model):
    TYPE_CHOICES = (
        ('e', 'Expense'),
        ('i', 'Income')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    class Meta:
        unique_together = ('user', 'name', 'type')

    def __str__(self):
        return f"id:{self.id} | user:{self.user} | name:{self.name} | type: {self.type}"


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    amount = models.PositiveIntegerField()
    currency_code = models.ForeignKey(Currency, to_field="code", on_delete=models.DO_NOTHING, related_name="expense")
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="expense_accounts")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="expense_categories")
    comment = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='photos_expense')
    date = models.DateField(auto_now_add=True)
   
    def __str__(self):
        return f"id:{self.id} | user:{self.user} | amount: {self.amount} | cur: {self.currency_code} | account: {self.account} | categ:{self.category} | comment:{self.comment} | photo:{self.photo} | date: {self.date} "  


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes")
    amount = models.PositiveIntegerField()
    currency_code = models.ForeignKey(Currency, to_field="code", on_delete=models.DO_NOTHING, related_name="income")
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="income_accounts")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="income_categories")
    comment = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='photos_income')
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"id:{self.id} | user:{self.user} | amount: {self.amount} | cur: {self.currency_code} | account: {self.account} | categ:{self.category} | comment:{self.comment} | photo:{self.photo} | date: {self.date} "  


class Reminder(models.Model):
    FREQUENCY_CHOICES = (
        (0, 'None'),
        (1, 'Daily'),
        (7, 'Weekly'),
        (14, 'Biweekly'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reminders")
    text = models.TextField()
    date_time = models.DateTimeField()
    frequency = models.PositiveIntegerField(choices=FREQUENCY_CHOICES)
    def __str__(self):
        return f"id:{self.id} | user:{self.user} | text: {self.text} | date_time: {self.date_time} | frequency:{self.frequency}"  



class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budgets")
    amount = models.PositiveIntegerField()
    currency_code = models.ForeignKey(Currency, to_field="code", on_delete=models.DO_NOTHING, related_name="budget")
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="budget_accounts")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="budget_categories", null=True) # choose null if all expense categories
    due_date = models.DateField()
    def __str__(self):
        return f"id:{self.id} | user:{self.user} | amount: {self.amount} | cur: {self.currency_code} | account: {self.account} | categ:{self.category} | due_date: {self.due_date} "  



