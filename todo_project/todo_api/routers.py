from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin
from . import views


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


todo_api_router = NestedDefaultRouter(trailing_slash=False)

projects_router = todo_api_router.register('todos', views.TodosView)

projects_tasks = projects_router.register('tasks',
                                          views.TasksView,
                                          basename='todos-tasks',
                                          parents_query_lookups=['todos'])


tasks_router = todo_api_router.register('tasks', views.TasksView)
