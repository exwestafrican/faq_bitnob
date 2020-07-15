from django.contrib import admin

# Register your models here.
from answer.models import Answer


class AnswerAdmin(admin.ModelAdmin):
    raw_id_fields = ["question"]
    readonly_fields = ["created", "updated", "user"]

    def save_model(self, request, obj, form, change):
        # overide method to set user field as request.user
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Answer, AnswerAdmin)
