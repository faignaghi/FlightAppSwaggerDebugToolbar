from django.urls import path, include
from .views import RegisterView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),    # 'dj-rest-auth/'
    path('register/', RegisterView.as_view())
]
