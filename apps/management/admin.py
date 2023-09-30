from django.contrib import admin
from .models import Employee
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
# Register your models here.

# UserChangeForm is used by UserAdmin
# UserAdmin is what Django uses to render the admin look for its user.
# Since Employee extends AbstractUser it can also leverage UserAdmin if a new form that is based on UserChangeForm uses Employee as the model.

# Create a new form that is based on UserChangeForm


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Employee

# Use the new form that is based on UserChangeForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    # Update the fields used by the formset that generates the form to include extra fields in Employee.
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("job_title", "total_recommends",
         "current_month_recommends", "eotm_wins", "is_eotm", "image", "image_url")}),
    )


admin.site.register(Employee, CustomUserAdmin)
