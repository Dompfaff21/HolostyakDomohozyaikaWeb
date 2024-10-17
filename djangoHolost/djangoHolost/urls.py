from django.contrib import admin
from django.urls import path, include
from users.views import LoginView, RegisterView, UserProfileView, UserProfileUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('recipe/', include('recipe.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profiles/<int:id>', UserProfileView.as_view()),
    path('update_profile/', UserProfileUpdateView.as_view())
]

handler404 = 'main.views.error_404_view'