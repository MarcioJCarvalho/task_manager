from django.urls import path
from .views import UserCreate, TaskCreate, TaskListCreate, CategoryCreate, AuditableCreate, CommentCreate, UserUpdate, TaskUpdate, AuditableUpdate, TaskListUpdate, CategoryUpdate, CommentUpdate, UserDelete, TaskDelete, CategoryDelete, AuditableDelete, CommentDelete, TaskListDelete, UserList, TasksList, TaskListList, CategoryList, AuditableList, CommentList
urlpatterns = [
    path('cadastrar/usuario/', UserCreate.as_view(), name='cadastro-usuario'),
    path('cadastrar/tarefa/', TaskCreate.as_view(), name='cadastro-tarefa'),
    path('cadastrar/lista-tarefas/', TaskListCreate.as_view(), name='cadastro-lista-tarefas'),
    path('cadastrar/categoria/', CategoryCreate.as_view(), name='cadastro-categoria'),
    path('cadastrar/auditoria/', AuditableCreate.as_view(), name='cadastro-auditoria'),
    path('cadastrar/comentario/', CommentCreate.as_view(), name='cadastro-comentario'),

    path('editar/usuario/<str:pk>', UserUpdate.as_view(), name='atualizar-usuario'),
    path('editar/tarefa/<str:pk>', TaskUpdate.as_view(), name='atualizar-tarefa'),
    path('editar/categoria/<str:pk>', CategoryUpdate.as_view(), name='atualizar-categoria'),
    path('editar/auditoria/<str:pk>', AuditableUpdate.as_view(), name='atualizar-auditoria'),
    path('editar/comentario/<str:pk>', CommentUpdate.as_view(), name='atualizar-comentario'),
    path('editar/lista-tarefas/<str:pk>', TaskListUpdate.as_view(), name='atualizar-lista-tarefas'),

    path('excluir/usuario/<str:pk>', UserDelete.as_view(), name='deletar-usuario'),
    path('excluir/tarefa/<str:pk>', TaskDelete.as_view(), name='deletar-tarefa'),
    path('excluir/categoria/<str:pk>', CategoryDelete.as_view(), name='deletar-categoria'),
    path('excluir/auditoria/<str:pk>', AuditableDelete.as_view(), name='deletar-auditoria'),
    path('excluir/comentario/<str:pk>', CommentDelete.as_view(), name='deletar-comentario'),
    path('excluir/lista-tarefas/<str:pk>', TaskListDelete.as_view(), name='deletar-lista-tarefas'),

    path('listar/usuarios/', UserList.as_view(), name='usuarios'),
    path('listar/tarefas/', TasksList.as_view(), name='tarefas'),
    path('listar/categorias/', CategoryList.as_view(), name='categorias'),
    path('listar/auditorias/', AuditableList.as_view(), name='auditorias'),
    path('listar/comentarios/', CommentList.as_view(), name='comentarios'),
    path('listar/lista-tarefas/', TaskListList.as_view(), name='lista-tarefas'),
]