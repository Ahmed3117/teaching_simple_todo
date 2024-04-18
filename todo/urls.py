from django.contrib import admin
from django.urls import path
from .views import create_todo, delete_todo, todos, update_todo,edit_status_todo
app_name = 'todo'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' , todos, name="todos"),
    path('create_todo/' , create_todo, name="create_todo"),
    path('update_todo/<int:pk>' , update_todo, name="update_todo"),
    path('delete_todo/<int:pk>' , delete_todo, name="delete_todo"),
    path('edit_status_todo/<int:pk>' , edit_status_todo, name="edit_status_todo"),
]
