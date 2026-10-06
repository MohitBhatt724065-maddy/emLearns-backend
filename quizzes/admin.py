from django.contrib import admin
from .models import Quiz, Question, Option, Attempt, QuestionResponse


class OptionInline(admin.TabularInline):
    model = Option
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "quiz", "difficulty")
    inlines = [OptionInline]


admin.site.register(Quiz)
admin.site.register(Attempt)
admin.site.register(QuestionResponse)