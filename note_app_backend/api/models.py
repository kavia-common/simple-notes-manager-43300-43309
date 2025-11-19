from django.db import models

class Note(models.Model):
    """
    Model representing a simple note.
    """
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
