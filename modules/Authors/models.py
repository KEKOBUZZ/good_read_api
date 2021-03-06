from django.db import models

# Create your models here.

GENDER = (
	("M","Masculino"),
	("F","Femenino"),
	)

#se agrego despues para seleccionar el genero literario
"""LIT_GENRE= (
	("sf","science fiction"),
	("dr","drama"),
	("ft","fantasy"),
	("bg","biography"),
	("ht","history"),
	("ot","others")
	)
"""

class Author(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	nacionality = models.CharField(max_length=50)
	biography = models.TextField()
	gender = models.CharField(max_length=20, choices=GENDER)
	#lit_genre = models.CharField(max_length=80, choices=LIT_GENRE)
	age = models.IntegerField(null=True)
	is_alive = models.BooleanField(default=True)

	def __str__(self):
			return "Autor: %s %s" % (self.name,self.last_name) #pondra el nombre del libro




