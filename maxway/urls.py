"""maxway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views import CreateCategoryView
from product.views import CreateBurgerView
from product.views import get_by_category_id
from product.views import get_product

from product.views import import_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('import/', import_data),
    path('', get_product),
    path("<int:category_id>/", get_by_category_id),
    path('add/', CreateBurgerView.as_view()),
    path('ads/', CreateCategoryView.as_view())
]