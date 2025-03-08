from django.db import models

class Item(models.Model):
    content = models.TextField()
    update_date = models.DateTimeField("date updated")

class Tag(models.Model):
    label = models.CharField(max_length=1000)

    def __str__(self):
        return self.label

class ItemTag(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)



