from django.db import models

# Create your models here.
class RawData(models.Model):
    column_1 = models.DecimalField(max_digits=20,decimal_places=4)
    column_2 = models.DecimalField(max_digits=20,decimal_places=4)
    column_3 = models.DecimalField(max_digits=20,decimal_places=4)
    column_4 = models.DecimalField(max_digits=20,decimal_places=4)
    column_5 = models.DecimalField(max_digits=20,decimal_places=4)

    def __unicode__(self):
        return self