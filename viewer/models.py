from django.db import models
from django.contrib.auth.models import User


class Level(models.Model):
    name = models.CharField(max_length=10)
    threshold = models.IntegerField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    image = models.CharField(max_length=200, null=True)


class Question(models.Model):
    contents = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    score = models.IntegerField()
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.category_id}, {self.contents[0:30]}..."


class AnswerType(models.Model):
    type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.type_name


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    type_id = models.ForeignKey(AnswerType, on_delete=models.DO_NOTHING)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Quiz(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    quiz_score = models.IntegerField(default=0)
    quiz_step = models.IntegerField(default=0)

    def __str__(self):
        return f"id: {self.id}, {self.user_id}, {self.name}, {self.quiz_score}"


class Quiz_question(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quiz_id}, {self.question_id}"


class User_category(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    points = models.IntegerField(default=0)
