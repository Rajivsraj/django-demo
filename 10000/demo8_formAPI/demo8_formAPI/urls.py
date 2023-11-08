"""
URL configuration for demo8_formAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from from1 import views
from form2 import views as api
from form3 import views as frm3
from form_validation import views as fv

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("register/", views.register),
    # path("register-post/", views.register_post),
    # path("form-api/", api.register_frm_api),
    # path("form-idattr/", api.register_id_attr),
    # path("form/", api.register_frm2),
    # path("form3/", frm3.register)

    path("validation/", frm3.register_frm_validation),
    path("validation2/", fv.frm_validation),

]
