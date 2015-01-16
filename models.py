from django.db import models

# Create your models here.
class portfolio(models.Model):
	title = models.CharField(max_length=200)
	short = models.CharField(max_length=200)
	url = models.CharField(max_length=500, blank=True)
	content = models.TextField()
	introImage = models.CharField(max_length=200)



class page(models.Model):
	title = models.CharField(max_length=200)
	descript = models.CharField(max_length=200)
	content = models.TextField()
	onMenu = models.BooleanField(default=False)



class project(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	externalUrl = models.CharField(max_length=400)
	introImage = models.CharField(max_length=200)


class blog(page):
	pub_date = models.DateTimeField("pub")
