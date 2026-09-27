from django.db import models

from alunos.models import Aluno
from instrutor.models import Instrutor
from exercicios.models import Exercicio


class Treino(models.Model):
    nome = models.CharField(max_length=100)

    objetivo = models.CharField(
        max_length=150
    )

    descricao = models.TextField(
        blank=True
    )

    data_criacao = models.DateField(
        auto_now_add=True
    )

    instrutor = models.ForeignKey(
        Instrutor,
        on_delete=models.PROTECT,
        related_name='treinos'
    )

    exercicios = models.ManyToManyField(
        Exercicio,
        through='TreinoExercicio',
        related_name='treinos'
    )

    def __str__(self):
        return self.nome


class AlunoTreino(models.Model):
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='alunos_treinos'
    )

    treino = models.ForeignKey(
        Treino,
        on_delete=models.CASCADE,
        related_name='alunos_treinos'
    )

    data_inicio = models.DateField()

    data_fim = models.DateField(
        null=True,
        blank=True
    )

    ativo = models.BooleanField(
        default=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['aluno', 'treino'],
                name='aluno_treino_unico'
            )
        ]

    def __str__(self):
        return f'{self.aluno} - {self.treino}'


class TreinoExercicio(models.Model):
    treino = models.ForeignKey(
        Treino,
        on_delete=models.CASCADE,
        related_name='treino_exercicios'
    )

    exercicio = models.ForeignKey(
        Exercicio,
        on_delete=models.CASCADE,
        related_name='treino_exercicios'
    )

    ordem = models.PositiveIntegerField(
        default=1
    )

    series = models.PositiveIntegerField(
        default=3
    )

    repeticoes = models.PositiveIntegerField(
        default=10
    )

    carga_kg = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )

    descanso_segundos = models.PositiveIntegerField(
        default=60
    )

    observacao = models.TextField(
        blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['treino', 'exercicio'],
                name='treino_exercicio_unico'
            )
        ]

        ordering = ['ordem']

    def __str__(self):
        return f'{self.treino} - {self.exercicio}'