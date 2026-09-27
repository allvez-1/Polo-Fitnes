from django.urls import path

from . import views


app_name = 'treinos'


urlpatterns = [

    # TREINO

    path(
        '',
        views.lista,
        name='lista'
    ),

    path(
        'novo/',
        views.criar,
        name='criar'
    ),

    path(
        '<int:pk>/editar/',
        views.editar,
        name='editar'
    ),

    path(
        '<int:pk>/excluir/',
        views.excluir,
        name='excluir'
    ),


    # ALUNO TREINO

    path(
        'alunos/',
        views.lista_aluno_treino,
        name='lista_aluno_treino'
    ),

    path(
        'alunos/novo/',
        views.criar_aluno_treino,
        name='criar_aluno_treino'
    ),

    path(
        'alunos/<int:pk>/editar/',
        views.editar_aluno_treino,
        name='editar_aluno_treino'
    ),

    path(
        'alunos/<int:pk>/excluir/',
        views.excluir_aluno_treino,
        name='excluir_aluno_treino'
    ),


    # TREINO EXERCICIO

    path(
        'exercicios/',
        views.lista_treino_exercicio,
        name='lista_treino_exercicio'
    ),

    path(
        'exercicios/novo/',
        views.criar_treino_exercicio,
        name='criar_treino_exercicio'
    ),

    path(
        'exercicios/<int:pk>/editar/',
        views.editar_treino_exercicio,
        name='editar_treino_exercicio'
    ),

    path(
        'exercicios/<int:pk>/excluir/',
        views.excluir_treino_exercicio,
        name='excluir_treino_exercicio'
    ),
]