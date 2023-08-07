from django.urls import path, include
from rest_framework import routers
from . views import *
from django.conf import settings
from django.conf.urls.static import static 

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user') # http://127.0.0.1:8000/api/user/
router.register(r'account', AccountViewSet) # http://127.0.0.1:8000/api/account/
router.register(r'expense', ExpenseViewSet) # http://127.0.0.1:8000/api/expense/
router.register(r'income', IncomeViewSet) # http://127.0.0.1:8000/api/income/
router.register(r'reminder', ReminderViewSet) # http://127.0.0.1:8000/api/reminder/
router.register(r'budget', BudgetViewSet) # http://127.0.0.1:8000/api/budget/

urlpatterns = [
    path('auth/', include('rest_framework.urls')), # login and logout
]

urlpatterns += router.urls