from django.db import models
class Books(models.Model):
    book_name=models.CharField(max_length=500)
    book_container=models.IntegerField()
    registered=models.BooleanField(default=False)
    reg_under=models.IntegerField()
