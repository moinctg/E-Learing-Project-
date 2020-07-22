
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_view
#from django.conf import settings 
#from django.conf.urls.static import static
#from accounts import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('register/', user_views.register, name='register'),
    ##path('profile/', user_views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('course/', include('coureses.urls')),
]

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
