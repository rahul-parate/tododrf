from django.urls import path
from . import views

urlpatterns = [
    path('', views.OverView.as_view(), name="api-overview"),
    path('app/create/', views.CreateView.as_view(), name="create"),
    path('app/update/', views.EditView.as_view(), name="update"),
    path('app/delete/<int:taskid>/', views.DeleteView.as_view(), name="delete"),
    path('app/details/', views.DetailsView.as_view(), name="detail"),
    path('app/list/', views.TaskList.as_view(), name="task-list"),
  ]