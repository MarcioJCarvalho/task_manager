import django_filters
from .models import Task, Comment

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'due_date': ['exact'],
        }

class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = {
            'text': ['icontains'],
        }



#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     title = models.CharField(max_length=50, unique=True, verbose_name="Título")
#     description = models.TextField(verbose_name="Descrição")
#     due_date = models.DateField(verbose_name="Prazo")
#     creation_date = models.DateField(verbose_name="Criação")
#     completion_date = models.DateField(null=True, blank=True, verbose_name="Finalização")
#     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
#     category = models.ForeignKey(Category, on_delete=models.PROTECT)
#     comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.PROTECT)
#     arquivo = models.FileField(upload_to='pdf/', null=True)
#     usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="tasks_as_usuario") 

