"""django010Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views


app_name = "AppStaticSite"
urlpatterns = [
    path("index", views.index),
    path("", views.home),
    path("home", views.home, name="AppStaticSite-home"),
    path("form", views.form, name="AppStaticSite-form"),
    path("form_abc", views.form_abc, name="AppStaticSite-form_abc"),
    path("store", views.store, name="AppStaticSite-store"),
    path("store_result", views.store_result, name="store_result"),
    path("abc_result", views.abc_result, name="abc_result"),
    # path("page_01/<path:queryStr>", views.page_01, name="AppStaticSite-page_01"),
]
