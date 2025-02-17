from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """A blog that the user is writing."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Post(models.Model):
    """A specific post within a blog."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'posts'
    
    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.text)>50:
            return f"{self.text[:50]}..."
        else:
            return self.text