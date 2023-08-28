from rest_framework import serializers

from . import models


# User Serializer
class UserSerializer(serializers.ModelSerializer):

	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = models.User
		fields = ('id','username','email', 'is_staff','password', 'password2')
		extra_kwargs = {
			'password': {'write_only': True},
			'is_staff': {'read_only': True},
			'is_active': {'read_only': True},
			}
	
	def save(self):
		account = models.User(
				username = self.validated_data['username'],
				email = self.validated_data['email']
			)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords do not match.'})
		account.set_password(password)
		account.save()


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

