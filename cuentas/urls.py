from django.urls import path
from cuentas import views 

urlpatterns = [
    path(
        route='dashboard',
        view = views.DahsboardView.as_view(),
        name='dashboard'
    ),
    path(
        route='create_account',
        view = views.CreateAccountView.as_view(),
        name='create_account'
    ),
    path(
        route='accounts',
        view = views.AccountListView.as_view(),
        name='accounts'
    )
]