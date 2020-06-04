from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'employee'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), 
    path('month', views.MonthCalendar.as_view(), name='month'), 
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'), 
    path('add/', views.AddView.as_view(), name='add'), 
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'), 
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'), 
    path('detail/<int:pk>/', views.detail, name='detail'), 
]