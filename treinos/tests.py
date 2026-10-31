from django.test import TestCase

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from exercicios.models import Exercicio
from instrutor.models import Instrutor
from treinos.models import Treino, TreinoExercicio


class PermissoesETreinoTests(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='usuario_teste', password='teste_seguro_123')
        self.client.force_login(self.usuario)

    def test_usuario_sem_permissao_recebe_403_com_mensagem(self):
        resposta = self.client.get(reverse('treinos:criar'))
        self.assertEqual(resposta.status_code, 403)
        self.assertContains(resposta, 'Você não possui permissão', status_code=403)

    def test_usuario_sem_permissao_nao_pode_criar_treino(self):
        resposta = self.client.post(reverse('treinos:criar'), data={'nome': 'Teste'})
        self.assertEqual(resposta.status_code, 403)

    def test_detalhes_treino_sem_exercicios(self):
        instrutor = Instrutor.objects.create(username='instrutor_teste', nome='Instrutor Teste', cpf='00000000000', especialidade='Musculação', cref='TESTE123')
        treino = Treino.objects.create(nome='Treino teste', objetivo='Condicionamento', instrutor=instrutor)
        resposta = self.client.get(reverse('treinos:detalhes', args=[treino.pk]))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Nenhum exercício associado')

    def test_detalhes_treino_com_exercicio_associado(self):
        instrutor = Instrutor.objects.create(
            username='instrutor_exercicio', nome='Instrutor Exercicio',
            cpf='11111111111', especialidade='Musculação', cref='TESTE456'
        )
        treino = Treino.objects.create(nome='Treino A', objetivo='Força', instrutor=instrutor)
        exercicio = Exercicio.objects.create(nome='Agachamento', grupo_muscular='Pernas')
        TreinoExercicio.objects.create(treino=treino, exercicio=exercicio)
        resposta = self.client.get(reverse('treinos:detalhes', args=[treino.pk]))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Agachamento')
