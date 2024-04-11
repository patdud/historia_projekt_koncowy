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
    DO_NOTHING
)


class AnswerType(Model):
    type_name = CharField(max_length=255)

    def __str__(self):
        return self.type_name


class Answer(Model):
    question_id = ForeignKey(Question)
    content = CharField(max_length=255)
    type_id = ForeignKey(AnswerType, on_delete=DO_NOTHING)
    flag = BooleanField(default=False)

    def __str__(self):
        return self.content
