from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Category

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class Index(TemplateView):
    template_name = "index.html"


class Collection(TemplateView):
    template_name = 'collection.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class CategoryView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_param = self.request.GET.get('category')
        categories = Category.objects.get(title=query_param)
        context['products'] = categories.products.all()
        context['category'] = query_param
        return context


class ProductView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get('id')
        context['products'] = Product.objects.all()
        context['product'] = Product.objects.get(id=product_id)
        return context


# class UserRegisterView(CreateView):
#     model = User
#     form_class = CustomUserCreationForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('login')
#
#
# class CustomLoginView(LoginView):
#     template_name = 'registration/login.html'
#     authentication_form = CustomAuthenticationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('index')