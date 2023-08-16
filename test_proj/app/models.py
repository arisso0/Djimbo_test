from django.db import models


class Page(models.Model):
    """Страница"""
    name = models.CharField("Название страницы", max_length=100)
    slug = models.CharField("Идентификатор", max_length=100, unique=True)
    position = models.IntegerField("Порядок")

    updated = models.DateTimeField("Обновлено", auto_now=True)
    created = models.DateTimeField("Создано", auto_now_add=True)

    @property
    def blocks_in_page(self):
        blocks = Block.objects.filter(pageblock__page=self).order_by("pageblock__position")
        return blocks

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["position"]


class Block(models.Model):
    """Блок"""
    name = models.CharField("Название", max_length=100)
    video_url = models.URLField("УРЛ видео")
    shows_number = models.IntegerField("Количество показов", default=0)

    updated = models.DateTimeField("Обновлено", auto_now=True)
    created = models.DateTimeField("Создано", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class PageBlock(models.Model):
    """Связь страницы и блока"""
    page = models.ForeignKey(Page, on_delete=models.CASCADE, verbose_name="Страница")
    block = models.ForeignKey(Block, on_delete=models.CASCADE, verbose_name="Блок")
    position = models.IntegerField("Порядок")

    updated = models.DateTimeField("Обновлено", auto_now=True)
    created = models.DateTimeField("Создано", auto_now_add=True)
