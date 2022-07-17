from django.urls import path

from todoapp.todo.views import apiOverview, taskList, taskDetails, taskCreate, taskUpdate, taskDelete

urlpatterns = (
    path('', apiOverview, name='api-overview'),
    path('task-list/', taskList, name='task-list'),
    path('task-create/', taskCreate, name='task-create'),
    path('task-detail/<str:pk>/', taskDetails, name='task-detail'),
    path('task-update/<str:pk>/', taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', taskDelete, name='task-delete'),
)