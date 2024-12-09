from django.urls import path
from .views import TaskCreate, CategoryCreate, AuditableCreate, CommentCreate, TaskUpdate, AuditableUpdate, CategoryUpdate, CommentUpdate, TaskDelete, CategoryDelete, AuditableDelete, CommentDelete, TasksList, CategoryList, AuditableList, CommentList
urlpatterns = [
    path('cadastrar/tarefa/', TaskCreate.as_view(), name='cadastro-tarefa'),
    path('cadastrar/categoria/', CategoryCreate.as_view(), name='cadastro-categoria'),
    path('cadastrar/auditoria/', AuditableCreate.as_view(), name='cadastro-auditoria'),
    path('cadastrar/comentario/', CommentCreate.as_view(), name='cadastro-comentario'),

    path('editar/tarefa/<str:pk>', TaskUpdate.as_view(), name='atualizar-tarefa'),
    path('editar/categoria/<str:pk>', CategoryUpdate.as_view(), name='atualizar-categoria'),
    path('editar/auditoria/<str:pk>', AuditableUpdate.as_view(), name='atualizar-auditoria'),
    path('editar/comentario/<str:pk>', CommentUpdate.as_view(), name='atualizar-comentario'),

    path('excluir/tarefa/<str:pk>', TaskDelete.as_view(), name='deletar-tarefa'),
    path('excluir/categoria/<str:pk>', CategoryDelete.as_view(), name='deletar-categoria'),
    path('excluir/auditoria/<str:pk>', AuditableDelete.as_view(), name='deletar-auditoria'),
    path('excluir/comentario/<str:pk>', CommentDelete.as_view(), name='deletar-comentario'),

    path('listar/tarefas/', TasksList.as_view(), name='tarefas'),
    path('listar/categorias/', CategoryList.as_view(), name='categorias'),
    path('listar/auditorias/', AuditableList.as_view(), name='auditorias'),
    path('listar/comentarios/', CommentList.as_view(), name='comentarios'),
]