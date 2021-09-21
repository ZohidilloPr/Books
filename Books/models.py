from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.

length = 100
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

class Authors(models.Model):
    first_name = models.CharField(max_length=length, blank=True, null=True)
    last_name = models.CharField(max_length=length, blank=True, null=True)
    slug = models.SlugField(max_length=length)
    birth_date = models.DateField()
    description = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.first_name + self.last_name

    def get_absolute_url(self):
        return reverse('Books:Book', kwargs={'slug':self.slug})
 

class BookCoverManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(have_book_cover=True)

class Book(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=length, blank=True, null=True)
    slug = models.SlugField(max_length=length)
    book_cover = models.ImageField(default='mockup1.png', upload_to='book_covers/')
    book_cover1 = models.ImageField(default='pages.png', upload_to='book_covers/')
    book_cover2 = models.ImageField(default='pages.png', upload_to='book_covers/')
    book_cover3 = models.ImageField(default='pages.png', upload_to='book_covers/')
    have_book_cover = models.BooleanField(default=False)
    description = models.TextField()
    pup_date = models.DateField()
    added_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    book_coverObj = BookCoverManager()

    def __str__(self):
        return f'{self.book_name} by {self.author}'

    def __unicode__(self):
        return f'{self.book_name} by {self.author}'

    def get_absolute_url(self):
        return reverse('Books:Home', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.book_name)
        return super().save(*args, **kwargs)



