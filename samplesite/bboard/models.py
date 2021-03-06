from unicodedata import name
from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name="Deal title")
    content = models.TextField(null=True, blank=True, verbose_name="Deal description")
    price = models.FloatField(null=True, blank=True, verbose_name="Price")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Published")
    rubric = models.ForeignKey("Rubric", null=True, on_delete=models.PROTECT, verbose_name="Rubric")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Deal"
        verbose_name_plural = "Deals"
        ordering = ["-published"]

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Rubric name")

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Rubric"
        verbose_name_plural = "Rubrics"
        ordering = ["name"]
