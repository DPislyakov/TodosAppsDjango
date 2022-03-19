from django.db import models


class Todos(models.Model):

    title = models.CharField(max_length=200)
    color = models.CharField(max_length=200)

    def __str__(self):
        return f'<todos: {self.title}>'

    class Meta:
        ordering = ('title',)
        verbose_name = 'todos'
        verbose_name_plural = 'todos'


class Tasks(models.Model):

    todos = models.ForeignKey('Todos', related_name='tasks_ids', on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'<tasks: {self.task}>'

    class Meta:
        ordering = ('task',)
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
