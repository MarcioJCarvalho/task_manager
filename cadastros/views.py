from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Task, Comment, Category, Auditable
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django_filters.views import FilterView
from .filters import TaskFilter, CommentFilter
# Create your views here.

############# CADASTROS #############
class CategoryCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('signin')
    model = Category
    fields = ['name']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('categorias')

class CommentCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('signin')
    model = Comment
    fields = ['creation_date', 'text']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('comentarios')

class AuditableCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('signin')
    model = Auditable
    fields = ['timestamp', 'action']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('auditorias')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Auditorias"
        context['botao'] = "Salvar"
        return context

class TaskCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('signin')
    group_required = ['admin', 'users']
    model = Task
    fields = ['title', 'description', 'due_date', 'creation_date', 'user', 'category', 'comment', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('tarefas')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        # não salvou no banco ainda
        url = super().form_valid(form)
        # já está salvo no banco
        return url

############# ATUALIZAÇÂO #############
class CategoryUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('signin')
    model = Category
    fields = ['name']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('categorias')

class CommentUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('signin')
    model = Comment
    fields = ['text']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('comentarios')

class AuditableUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('signin')
    model = Auditable
    fields = ['action']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('auditorias')

class TaskUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('signin')
    group_required = ['admin', 'users']
    model = Task
    fields = ['title', 'description', 'due_date', 'creation_date', 'completion_date', 'user', 'category', 'comment', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('tarefas')

############# DELETE #############
class CategoryDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('signin')
    model = Category
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('categorias')

class CommentDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('signin')
    model = Comment
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('comentarios')

class AuditableDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('signin')
    model = Auditable
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('auditorias')

class TaskDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('signin')
    group_required = ['admin', 'users']
    model = Task
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('tarefas') 

############# LISTA #############
class CategoryList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('signin')
    model = Category
    template_name = 'cadastros/lista/categorias.html'

class CommentList(LoginRequiredMixin, FilterView):
    login_url = reverse_lazy('signin')
    model = Comment
    template_name = 'cadastros/lista/comentarios.html'
    paginate_by = 50
    filterset_class = CommentFilter

class AuditableList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('signin')
    model = Auditable
    template_name = 'cadastros/lista/auditorias.html'

class TasksList(GroupRequiredMixin, LoginRequiredMixin, FilterView):
    login_url = reverse_lazy('signin')
    group_required = ['admin', 'users']
    model = Task
    template_name = 'cadastros/lista/tarefas.html'
    paginate_by = 50
    filterset_class = TaskFilter

    def get_queryset(self):
        self.object_list = Task.objects.filter(usuario=self.request.user)
        return self.object_list.select_related('user', 'category', 'comment') 