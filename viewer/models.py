from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    IntegerField,
    TextField,
    BooleanField,
    CASCADE,
    DO_NOTHING,
)
from django.contrib.auth.models import User


class Level(Model):
    name = CharField(max_length=10)
    threshold = IntegerField()

    def __str__(self):
        return self.name


class Category(Model):
    name = CharField(max_length=100, null=True)


class Article(Model):
    title = CharField(max_length=100, null=True)
    content = TextField()
    category_id = ForeignKey(Category, on_delete=DO_NOTHING)
    image = CharField(max_length=200, null=True)


class Question(Model):
    contents = TextField()
    category_id = ForeignKey(Category, on_delete=DO_NOTHING)
    score = IntegerField()
    level = ForeignKey(Level, on_delete=DO_NOTHING)

    def __str__(self):
        return f"{self.contents[0:30]}..."


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
        return str(self.id)


class Quiz(Model):
    user_id = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=100, null=True)
    quiz_score = IntegerField(default=0)

    def __str__(self):
        return f"id: {self.id}, {self.user_id}, {self.name}, {self.quiz_score}"


class Quiz_question(Model):
    quiz_id = ForeignKey(Quiz, on_delete=CASCADE)
    question_id = ForeignKey(Question, on_delete=CASCADE)

    def __str__(self):
        return f"{self.quiz_id}, {self.question_id}"


class User_category(Model):
    user_id = ForeignKey(User, on_delete=CASCADE)
    category_id = ForeignKey(Category, on_delete=DO_NOTHING)
    points = IntegerField(default=0)
