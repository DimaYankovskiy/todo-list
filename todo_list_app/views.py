from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list_app.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.order_by('is_done', '-created_at')


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("todo_list_app:task-list")
    template_name = "todo_list_app/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("todo_list_app:task-list")
    template_name = "todo_list_app/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list_app:task-list")
    template_name = "todo_list_app/task_confirm_delete.html"


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:tag-list")
    template_name = "todo_list_app/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:tag-list")
    template_name = "todo_list_app/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list_app:tag-list")
    template_name = "todo_list_app/tag_confirm_delete.html"
