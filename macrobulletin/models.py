from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=127, unique=True, verbose_name="Название разделала")
    slug = models.CharField(max_length=127, unique=True)

    def __str__(self):
        return f"Название раздела: {self.name}"



class EconomicIndex(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=127, unique=True)
    macro_topic = models.ForeignKey("Topic", on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Название экономического показателя: {self.name}"


class Table(models.Model):
    excel = models.FileField(upload_to="excels", default=None, blank=True, null=True)
    macro_economic_index = models.ForeignKey("EconomicIndex", on_delete=models.PROTECT)

    def __str__(self):
        return f"Название экономического показателя: {self.macro_economic_index.name}, путь: {self.excel}"
