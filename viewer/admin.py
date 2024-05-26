from django.contrib import admin
from viewer import models


admin.site.register(models.Level)
admin.site.register(models.Category)
admin.site.register(models.Article)
admin.site.register(models.Question)
admin.site.register(models.AnswerType)
admin.site.register(models.Answer)
admin.site.register(models.Quiz)
admin.site.register(models.Quiz_question)
admin.site.register(models.User_category)
