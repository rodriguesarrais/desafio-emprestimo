from django.urls import path
from .views import customer_loans, customer_loans_form

urlpatterns = [
    path('customer-loans', customer_loans, name='customer_loans'),
    path('loans/form', customer_loans_form, name='customer_loans_form'),
]