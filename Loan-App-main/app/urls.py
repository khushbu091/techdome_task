from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'index', views.CustomerViewSet)
router.register(r'loans', views.LoanViewSet)
router.register(r'repayments', views.RepaymentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('loan-list/', views.loan_list, name='loan_list'),
    path('add-repayment/', views.add_repayment, name='add_repayment')
]
