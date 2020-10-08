from django.db import models
from django.utils.text import slugify


class SluggedModel(models.Model):
    name = models.CharField(max_length=50, null=True)
    #slug = models.SlugField(unique=True)

    class Meta:
        abstract = True

    #def save(self, *args, **kwargs):
    #   self.slug = slugify(self.name)
    #    super(SluggedModel, self).save(*args, **kwargs)


class Service(SluggedModel):
    service = models.CharField('Услуга', max_length=100)

    def __str__(self):
        return 'Service {}'.format(self.name)


class SubService(SluggedModel):
    subservice = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services')
    service_price = models.DecimalField('Цена услги', max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return 'SubService {}'.format(self.name)


class Price(SluggedModel):
    price_work = models.CharField('Наименование работ', max_length=100)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return 'Price {}'.format(self.name)


class Comment(SluggedModel):
    comment_theme = models.CharField("Тема", max_length=50)
    comment_body = models.TextField("Отзывы")
    comment_name = models.CharField("Введите имя", max_length=50)
    comment_email = models.EmailField("Введите email", max_length=100)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {}'.format(self.name)

    class Meta:
        ordering = ['-comment_date']
