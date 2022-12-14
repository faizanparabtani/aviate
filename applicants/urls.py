from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
import applicants.views as userviews
from knox import views as knox_views

from .views import *

urlpatterns = [
    # Login Register
    path('register/', CreateUserView.as_view(), name='register'),
    path('update/<int:pk>', UpdateProfileView.as_view(), name='update'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    # Update Profile, Password
    path('profile/change_password/<int:pk>', ChangePasswordView.as_view(), name='change_password'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)