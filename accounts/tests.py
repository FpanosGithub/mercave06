from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class TestsUsuario(TestCase):
    def test_crear_usuario(self):
        Usuario_test = get_user_model()
        usuario_test = Usuario_test.objects.create_user(username='will',email='will@will.com',password='testpass123', organizacion='Tria')
        self.assertEqual(usuario_test.username, 'will')
        self.assertEqual(usuario_test.email, 'will@will.com')
        self.assertEqual(usuario_test.organizacion,'Tria')
        self.assertTrue(usuario_test.is_active)
        self.assertFalse(usuario_test.is_staff)

    def test_crear_superusuario(self):
        Usuario_admin = get_user_model()
        usuario_admin = Usuario_admin.objects.create_superuser(username='will',email='will@will.com',password='testpass123', organizacion='Tria')
        self.assertEqual(usuario_admin.username, 'will')
        self.assertEqual(usuario_admin.email, 'will@will.com')
        self.assertEqual(usuario_admin.organizacion,'Tria')
        self.assertTrue(usuario_admin.is_active)
        self.assertTrue(usuario_admin.is_staff)