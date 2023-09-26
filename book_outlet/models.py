from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.text import slugify

# Create your models here.




class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_codde = models.CharField(max_length=5)
    city = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.street}"



class Country(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10)



    def __str__(self):
        return f"{self.name}"


    class Meta:
        verbose_name_plural ="Countries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True)



    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname()

class Book(models.Model):
    title = models.CharField(max_length = 50)
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="author")
    is_bestselling = models.BooleanField(default = False)
    slug = models.SlugField(default = "",null = False)
    country = models.ManyToManyField(Country)



    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Book,self).save(*args,**kwargs)


    def __str__(self):
        return f"{self.title} ({self.rating})"
    

