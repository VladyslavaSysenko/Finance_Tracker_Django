from . import models
from rest_framework import serializers


# User Serializer
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = ('id','username','email', 'is_staff')

# Account Serializer
class AccountSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model = models.Account
		fields = '__all__'

# Expense serializer
class ExpenseSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model = models.Expense
		fields = '__all__'

# Income serializer
class IncomeSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model = models.Income
		fields = '__all__'


# Reminder serializer
class ReminderSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model = models.Reminder
		fields = '__all__'


# Budget serializer
class BudgetSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model = models.Budget
		fields = '__all__'

