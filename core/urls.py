from django.urls import path
from core.views import Index, Collection, CategoryView, ProductView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("collection/", Collection.as_view(), name="collection"),
    path("category/", CategoryView.as_view(), name="category"),
    path("product/<int:id>", ProductView.as_view(), name="product"),
    # path("sign-up/", UserRegisterView.as_view(), name="register"),
    # path("my-login/", CustomLoginView.as_view(), name="custom_login")
]
