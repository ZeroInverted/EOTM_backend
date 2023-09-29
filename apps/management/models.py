from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    job_title = models.CharField(max_length=128, null=True)
    total_recommends = models.PositiveIntegerField(default=0)
    current_month_recommends = models.PositiveIntegerField(default=0)
    eotm_wins = models.PositiveIntegerField(default=0)
    is_eotm = models.BooleanField(
        default=False, verbose_name="Employee of the month")
    image = models.ImageField(null=True, blank=True)
    image_url = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self) -> str:
        return self.username

    # Functionality to assert that only one employee is EOTM:

    def save(self, *args, **kwargs):

        # unset all other EOTM flags if this employee has been chosen as EOTM:
        if self.is_eotm:
            Employee.objects.filter(is_eotm=True).exclude(
                pk=self.pk).update(is_eotm=False)

        super().save(*args, **kwargs)
