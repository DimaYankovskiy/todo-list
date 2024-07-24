from django.urls import path

from todo_list_app.views import TaskListView, TagListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo_list_app"