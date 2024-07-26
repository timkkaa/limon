from django.db import models

class Category(models.Model):
    title = models.CharField()


    class Meta:
            verbose_name_plural = 'Категории публикаций'
            verbose_name = 'Категория публикации'


class Publication(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
  #  hashteg = models.ManyToManyField(Hashtager)
    title = models.CharField(verbose_name='название',max_length=255)
    short_description = models.TextField(max_length=500)
    description = models.TextField()
    image = models.ImageField()

    created_te = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'
