from django.db import models

# Create your models here.
class Level(Model):
    name = CharField(max_length=10)
    threshold = IntegerField()


    def __str__(self):
        return self.title


class Question(Model):
    contents = TextField()
    category_id = ForeignKey(Category)
    score = IntegerField()
    level = ForeignKey(Level)

    def __str__(self):
        return f"{self.contents}"