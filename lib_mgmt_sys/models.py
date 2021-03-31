from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=123)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=30)
    no_page = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, null=True)
    price = models.IntegerField(default=1000)
    cover_photo = models.ImageField(upload_to='books_photos', null=True)


    def __str__(self):
        return self.name

class AuthorPenName(models.Model):
    pen_name = models.CharField(max_length=55)
    author = models.OneToOneField(Author, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.pen_name


class Students(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    booked = models.ManyToManyField(Books)



    def __str__(self):
        return self.name




    '''
    creat table books(
    
        id int primary key autoincrement,
        name varchar (199),
        
        
        
        no_pag int    
    )
    '''
