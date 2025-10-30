from django.db import models
from django.contrib.auth.models import User

class Etiqueta (models.Model):
    nome = models.CharField(unique=True)
    cor = models.CharField(default="#000000")

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    class Meta:
        permissions = [
            ("can_view_all_tarefas", "Can view tasks from all users")
        ]

    def __str__(self):
        return self.titulo
    
class Perfil (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    tema = models.BooleanField(default=False)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"