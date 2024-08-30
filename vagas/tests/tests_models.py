from django.test import TestCase
from ..models import Curriculo, Empresa
from django.contrib.auth.models import User
from datetime import datetime


class CurriculoTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.perfil = Curriculo.objects.create(
            usuario=self.user,
            nome_completo="Nome Completo Teste",
            sobre_mim="Sobre Mim Teste",
            formacao="ensino_sc",
            habilidades="Habilidades Teste",
            atualizado_em=datetime.now(),
        )

    def test_create_curriculo(self):
        self.assertEqual(self.perfil.usuario.username, 'testuser')
        self.assertEqual(self.perfil.nome_completo, 'Nome Completo Teste')
        self.assertEqual(self.perfil.sobre_mim, 'Sobre Mim Teste')
        self.assertEqual(self.perfil.formacao, 'ensino_sc')
        self.assertEqual(self.perfil.habilidades, 'Habilidades Teste')
        self.assertIsNotNone(self.perfil.atualizado_em)
