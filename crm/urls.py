from django.urls import path
from . import views
urlpatterns = [
    path('signin/',views.signin, name="signin" ),
    path('signup/',views.signup, name="signup" ),
    path('index/',views.index, name="index" ),
    path('logout/',views.logout, name="logout" ),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:task_id>/', views.update, name='update'),
]