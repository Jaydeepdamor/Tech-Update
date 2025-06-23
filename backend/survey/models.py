from django.db import models
from django.utils import timezone


class SurveyResponse(models.Model):
    # Survey questions responses
    question1 = models.CharField(
        max_length=10,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        help_text="Have you ever wanted to stay updated with cutting-edge Tech advancements?"
    )
    
    question2 = models.CharField(
        max_length=10,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        help_text="Do you feel that you want to be updated, but you are not able to catch up with the advancements?"
    )
    
    # For question 3, we'll store it as a JSON field since it's multiple choice
    question3 = models.JSONField(
        help_text="What makes it hard for you to stay truly up-to-date with new knowledge of your field?"
    )
    
    # Email field
    email = models.EmailField(
        help_text="Gmail address"
    )
    
    # Optional other specification
    other_specification = models.TextField(
        blank=True,
        null=True,
        help_text="Additional details if 'Other' was selected"
    )
    
    # Metadata
    timestamp = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Survey Response"
        verbose_name_plural = "Survey Responses"
    
    def __str__(self):
        return f"Survey Response from {self.email} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    @property
    def question3_display(self):
        """Return a readable format of question3 choices"""
        if isinstance(self.question3, list):
            return ", ".join(self.question3)
        return str(self.question3)
