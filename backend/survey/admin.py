from django.contrib import admin
from .models import SurveyResponse


@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ['email', 'question1', 'question2', 'question3_display', 'created_at']
    list_filter = ['question1', 'question2', 'created_at']
    search_fields = ['email', 'other_specification']
    readonly_fields = ['timestamp', 'created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Survey Responses', {
            'fields': ('question1', 'question2', 'question3', 'other_specification')
        }),
        ('Contact Information', {
            'fields': ('email',)
        }),
        ('Metadata', {
            'fields': ('timestamp', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def question3_display(self, obj):
        """Display question3 choices in a readable format"""
        return obj.question3_display
    question3_display.short_description = 'Question 3 Choices'
