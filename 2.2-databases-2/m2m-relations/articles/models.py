from django.db import models
from django.core.exceptions import ValidationError


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Тег")
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    published_at = models.DateTimeField(verbose_name="Дата публикации")
    image = models.ImageField(upload_to='article_images/',null=True, blank=True, verbose_name="Изображение")

    tags = models.ManyToManyField(Tag, through="Scope", related_name='tag')


    def clean(self):
        if self.pk is None:
            if Article.objects.filter(title=self.title).exists():
                raise ValidationError("Статья с таким названием уже существует")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name="Основной тег")

    class Meta:
        unique_together = ('article', 'tag')

    def clean(self):
        if self.is_main:
            if Scope.objects.filter(article=self.article, is_main=True).exclude(pk=self.pk).exists():
                raise ValidationError('Можно указать только один основной раздел для статьи')

    def __str__(self):
        return f"{self.article.title} - {self.tag.name}"
    