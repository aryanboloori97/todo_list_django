from django.urls import path
from todo import views


urlpatterns = [
    path("", views.home_page, name='home'),
    path("add_task", views.add_task, name="add_task"),
    path("remove_task/<str:id>", views.remove_task, name="remove_task"),
    path("mark_as_done/<str:id>", views.mark_as_done, name="mark_as_done"),
    path("mark_as_undone/<str:id>", views.mark_as_undone, name="mark_as_undone"),
    path("edit_task/<str:id>", views.edit_task, name="edit_task"),
]
