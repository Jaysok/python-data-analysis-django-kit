from django.db import models

# Create your models here.
class Foo(models.Model):
    fid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'foo'

    def __str__(self):
        return self.name
