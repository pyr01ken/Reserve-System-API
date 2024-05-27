from django.urls import path
from . import views

app_name = 'reservations'
urlpatterns = [
    path("table/week/<int:week_number>/", views.ReservationsTableView.as_view(), name="table"),
    path("reserve/<int:timestamp>/", views.ReservationsDetailView.as_view(),
         name="detail"),
    path("payment/request/", views.ReservationsPaymentView.as_view(),
         name="payment_request"),
    path("payment/verify/", views.ReservationsVerifyView.as_view(), name="payment_verify"),
]
