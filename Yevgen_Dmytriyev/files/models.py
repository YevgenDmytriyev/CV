from django.db import models
from django.utils.translation import gettext_lazy as _
    
class HomePageContent(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    content = models.TextField(verbose_name="Content")

    class Meta:
        verbose_name = "Home Page Content"
        verbose_name_plural = "Home Page Contents"

    def __str__(self):
        return self.title
