from django.db import models

# Create your models here.
class vote_info(models.Model):
    """ create a vote model, holding voting result """
    agree = models.BooleanField(default=True)
    email = models.EmailField(max_length=255, unique=True)

    class Meta:
        db_table = "VOTE"
