from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import User, Task, TaskList, Comment, Category, Auditable
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
# Create your views here.

############# CADASTROS #############

class UserCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('signin')
    model = User
    fields = ['username', 'email', 'password']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('usuarios')

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

class TaskCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('signin')
    group_required = u'admin'
    model = Task
    fields = ['title', 'description', 'due_date', 'creation_date', 'user', 'category', 'comment']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('tarefas')

class TaskListCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('signin')
    model = TaskList
    fields = ['name']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-tarefas')

############# ATUALIZAÇÂO #############

class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('signin')
    model = User
    fields = ['username', 'email', 'password']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('usuarios')

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
    group_required = u'admin'
    model = Task
    fields = ['title', 'description', 'due_date', 'creation_date', 'completion_date', 'user', 'category', 'comment']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('tarefas')

class TaskListUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('signin')
    model = TaskList
    fields = ['name']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-tarefas')

############# DELETE #############

class UserDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('signin')
    model = User
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('usuarios')

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
    group_required = u'admin'
    model = Task
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('tarefas')

class TaskListDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('signin')
    model = TaskList
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('lista-tarefas')  

############# LISTA #############

class UserList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('signin')
    model = User
    template_name = 'cadastros/lista/usuarios.html'

class CategoryList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('signin')
    model = Category
    template_name = 'cadastros/lista/categorias.html'

class CommentList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('signin')
    model = Comment
    template_name = 'cadastros/lista/comentarios.html'

class AuditableList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('signin')
    model = Auditable
    template_name = 'cadastros/lista/auditorias.html'

class TasksList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('signin')
    group_required = u'admin'
    model = Task
    template_name = 'cadastros/lista/tarefas.html'

class TaskListList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('signin')
    model = TaskList
    template_name = 'cadastros/lista/lista-tarefas.html'