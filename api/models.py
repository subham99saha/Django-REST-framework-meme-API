from django.db import models

# Create your models here.
class Meme(models.Model):

	name = models.CharField(max_length = 30)
	caption = models.CharField(max_length = 200)
	url = models.URLField(max_length = 200)

	class Meta:
		db_table = 'Meme'