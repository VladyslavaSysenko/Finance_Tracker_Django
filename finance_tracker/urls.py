from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register("user", UserViewSet, basename="user")  # http://127.0.0.1:8000/api/user/
router.register("account", AccountViewSet)  # http://127.0.0.1:8000/api/account/
router.register("expense", ExpenseViewSet)  # http://127.0.0.1:8000/api/expense/
router.register("income", IncomeViewSet)  # http://127.0.0.1:8000/api/income/
router.register("reminder", ReminderViewSet)  # http://127.0.0.1:8000/api/reminder/
router.register("budget", BudgetViewSet)  # http://127.0.0.1:8000/api/budget/

urlpatterns = [
    path("auth/", include("rest_framework.urls")),  # login http://127.0.0.1:8000/api/auth/login
                                                    # logout http://127.0.0.1:8000/api/auth/logout
]

urlpatterns += router.urls
