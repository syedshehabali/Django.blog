from .views import *
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register', register_view, name = 'register'),
    # path('blog/', blog, name = 'blog'),
]
