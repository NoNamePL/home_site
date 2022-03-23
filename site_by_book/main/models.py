from django.db import models


class NewsCart(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    image = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name="Картинка")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name_plural = "Новости"
        verbose_name = 'Новость'
        ordering = ['-published']
