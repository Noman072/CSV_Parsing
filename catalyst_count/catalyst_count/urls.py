from django.contrib import admin
from django.urls import path, include
from catalyst_task.views import main, filter_view, filter_api, CustomLoginView, CustomLogoutView, CustomSignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='file'),
    path('filter/', filter_view, name='filter'),
    path('api/', filter_api),
    path('accounts/', include('allauth.urls')),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='account_logout'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),

]
