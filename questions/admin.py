from django.contrib import admin

# Register your models here.
from questions.models import Question


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ["user", "created", "updated"]

    def save_model(self, request, obj, form, change):
        # overide method to set user field as request.user
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Question, QuestionAdmin)
