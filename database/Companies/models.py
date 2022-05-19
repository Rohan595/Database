from django.db import models


class Comapany(models.Model):
    class Meta(object):
        db_table = 'company'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=50, db_index=True, default='Anonymous'
    )
    role = models.TextField(
        'Role', blank=False, null=False, db_index=True
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )
