# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView, FormView
from django.views.generic.base import TemplateView
from django.db.models import  Sum
from cuentas.forms import CreateAccountForm
from cuentas.models import Account, ProfileDetail, AccountDetail
from datetime import datetime, timedelta

class DahsboardView(LoginRequiredMixin, TemplateView):

    template_name = 'cuentas/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts_without_pay'] = ProfileDetail.objects.filter(is_pay=False).order_by('-created_at')[:100]

        total_profile_money = ProfileDetail.objects.all().aggregate(total_pay=Sum('pay_value'))
        context['total_profile_money'] = "${:,.2f}".format(total_profile_money['total_pay']) 

        total_profile_pay = ProfileDetail.objects.filter(is_pay=True).aggregate(total_pay=Sum('pay_value'))
        context['total_profile_pay'] = "${:,.2f}".format(total_profile_pay['total_pay'])

        total_profile_wo_pay = total_profile_money['total_pay'] - total_profile_pay['total_pay']
        context['total_profile_wo_pay'] = "${:,.2f}".format(total_profile_wo_pay)

        enddate = datetime.today()
        startdate = enddate - timedelta(days=15)
        context['accounts_near_to_expire'] = ProfileDetail.objects.filter(expire_at__range=[startdate, enddate]).order_by('expire_at')[:100]
        
        total_account_invest = AccountDetail.objects.all().aggregate(total_pay=Sum('pay_value'))
        context['total_account_invest'] = "${:,.2f}".format(total_account_invest['total_pay'])

        total_gain = total_profile_money['total_pay'] - total_account_invest['total_pay']
        context['total_gain'] = "${:,.2f}".format(total_gain)


        return context

class CreateAccountView(LoginRequiredMixin, FormView):
    """Users sign up view."""

    template_name = 'cuentas/create_account.html'
    form_class = CreateAccountForm
    success_url = reverse_lazy('cuentas:accounts')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

class AccountListView(LoginRequiredMixin, ListView):

    template_name = 'cuentas/accounts.html'
    model = Account
    ordering = ('-created_at',)
    paginate_by = 20
    context_object_name = 'accounts'