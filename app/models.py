from django.db import models


class Orders(models.Model):
    AT_WORK = 1
    READY = 2
    ISSUED = 3
    STATUSES = (
        (AT_WORK, 'В работе'),
        (READY, 'Готов к выдаче'),
        (ISSUED, 'Выдан'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    status = models.SmallIntegerField(default=AT_WORK, choices=STATUSES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id}. {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
