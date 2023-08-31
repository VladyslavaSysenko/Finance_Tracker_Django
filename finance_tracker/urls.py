from django.urls import include, path
from rest_framework import routers

from finance_tracker.views import *

router = routers.DefaultRouter()
router.register(r"user", UserViewSet, basename="user")  # http://127.0.0.1:8000/api/user/
router.register(r"account", AccountViewSet)  # http://127.0.0.1:8000/api/account/
router.register(r"expense", ExpenseViewSet)  # http://127.0.0.1:8000/api/expense/
router.register(r"income", IncomeViewSet)  # http://127.0.0.1:8000/api/income/
router.register(r"reminder", ReminderViewSet)  # http://127.0.0.1:8000/api/reminder/
router.register(r"budget", BudgetViewSet)  # http://127.0.0.1:8000/api/budget/

urlpatterns = [
    path("auth/", include("rest_framework.urls")),  # login http://127.0.0.1:8000/api/auth/login
    # logout http://127.0.0.1:8000/api/auth/logout
]

urlpatterns += router.urls
