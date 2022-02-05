from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        abstract = True


class Poll(BaseModel):
    question = models.TextField(max_length=500, verbose_name='Вопрос')

    def __str__(self):
        return f'{self.id}. {self.question}'

    class Meta:
        db_table = 'Pools'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'