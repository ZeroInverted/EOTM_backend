from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Employee
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from admin_confirm import AdminConfirmMixin



# UserChangeForm is used by UserAdmin
# UserAdmin is what Django uses to render the admin look for its user.
# Since Employee extends AbstractUser it can also leverage UserAdmin if a new form that is based on UserChangeForm uses Employee as the model.

# Create a new form that is based on UserChangeForm


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Employee

# Use the new form that is based on UserChangeForm


class CustomUserAdmin(AdminConfirmMixin, UserAdmin):
    form = CustomUserChangeForm
    # Update the fields used by the formset that generates the form to include extra fields in Employee.
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("job_title", "total_recommends",
         "current_month_recommends", "eotm_wins", "is_eotm", "number_of_likes", "image", "image_url")}),
    )
    # Use django-admin-confirm module to show confirmation page on changes
    confirm_change = True
    # On the following field that decides if the user should be employee of the month
    confirmation_fields = ["is_eotm", ]
    
    #override save model to show a message if the user has been saved already, post save success message.
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.is_eotm:
            messages.success(request, f"User '{obj}' has been set as Employee of The Month")
        

            
admin.site.register(Employee, CustomUserAdmin)
