from json import JSONDecodeError

from django.http import JsonResponse
from rest_framework import generics, status, views, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from finance_tracker.models import *
from finance_tracker.permissions import *
from finance_tracker.serializers import *


# User CRUD
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]

    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     if pk:
    #         return User.objects.filter(pk=pk)
    #     return User.objects.all()[:3]

    # add default categories to user
    def perform_create(self, serializer):
        user = serializer.save()
        dflt_category_expense = [
            "Leisure",
            "Home",
            "Groceries",
            "Transportation",
            "Health",
            "Cafe",
            "Hobby",
            "Pets",
            "Education",
            "Rent",
            "Gift",
            "Other",
        ]
        dflt_category_income = ["Salary", "Gift", "Other"]
        categories_expense_list = [
            Category(user=user, name=cat, type="e") for cat in dflt_category_expense
        ]
        categories_income_list = [
            Category(user=user, name=cat, type="i") for cat in dflt_category_income
        ]
        Category.objects.bulk_create(categories_expense_list + categories_income_list)

    # @action(methods=['get'], detail=False)
    # def usernames(self, request):
    #     users = User.objects.all()
    #     return Response({'usernames':[u.username for u in users]})

    # @action(methods=['get'], detail=True)
    # def username(self, request, pk=None):
    #     user = User.objects.get(pk=pk)
    #     return Response({'usernames':user.username})


# Account CRUD
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# Expense CRUD
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


# Income CRUD
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


# Reminder CRUD
class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


# Budget CRUD
class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


# class UserAPIListCreate(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserAPIUpdate(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserAPIRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
