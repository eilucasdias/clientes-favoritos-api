from django.db import models
from django.conf import settings

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
    
class ProdutoFavorito(models.Model):
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produto_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    reviewScore = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('cliente', 'produto_id')

    def __str__(self):
        return f'{self.title} ({self.cliente})'