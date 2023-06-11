from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True)
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_date']



