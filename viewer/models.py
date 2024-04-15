from django.db import models

# Create your models here.


from django.db.models import (
    Model,
    CharField,
    DateField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    TextField,
    BooleanField,
    CASCADE,
    DO_NOTHING,
    SET_NULL,
)

from django.contrib.auth.models import User

class Category(Model):
    name = CharField(max_length=100, null=True)

class Article(Model):
    title = CharField(max_length=100, null=True)
    content = TextField()
    category_id = ForeignKey(Category, on_delete=DO_NOTHING)
    image = CharField(max_length=200, null=True)

    #test