from django.contrib import admin
from .models import Employee
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
# Register your models here.


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Employee


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("job_title", "total_recommends",
         "current_month_recommends", "eotm_wins", "is_eotm", "image", "image_url")}),
    )


admin.site.register(Employee, CustomUserAdmin)
