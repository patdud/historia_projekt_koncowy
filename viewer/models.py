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
    SET_NULL
)
from django.contrib.auth.models import User


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


class AnswerType(Model):
    type_name = CharField(max_length=255)

    def __str__(self):
        return self.type_name


class Answer(Model):
    question_id = ForeignKey(Question, on_delete=DO_NOTHING)
    content = CharField(max_length=255)
    type_id = ForeignKey(AnswerType, on_delete=DO_NOTHING)
    flag = BooleanField(default=False)

    def __str__(self):
        return self.content


class Quiz(Model):
    user_id = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=100, null=True) # czy to jest potrzebne?

    def __str__(self):
        return self.name


class Quiz_question(Model):
    quiz_id = ForeignKey(Quiz, on_delete=CASCADE)
    question_id = ForeignKey(Question, on_delete=CASCADE)


class User_category(Model):
    user_id = ForeignKey(User, on_delete=CASCADE)
    category_id = ForeignKey(Category, on_delete=DO_NOTHING)
    points = IntegerField()

 
    
