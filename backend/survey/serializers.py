from rest_framework import serializers
from .models import SurveyResponse


class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = ['id', 'question1', 'question2', 'question3', 'email', 'other_specification', 'timestamp']
        read_only_fields = ['id', 'timestamp']
    
    def validate_email(self, value):
        """Validate that the email is a Gmail address"""
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError("Please provide a valid Gmail address.")
        return value
    
    def validate_question3(self, value):
        """Validate that question3 is a list of valid choices"""
        valid_choices = [
            'Time constraints',
            'Information overload',
            'Lack of structured learning paths',
            'Cost of courses/resources',
            'Not knowing where to start',
            'Difficulty understanding technical concepts',
            'Other'
        ]
        
        if not isinstance(value, list):
            raise serializers.ValidationError("Question 3 must be a list of choices.")
        
        if not value:
            raise serializers.ValidationError("Please select at least one option for Question 3.")
        
        for choice in value:
            if choice not in valid_choices:
                raise serializers.ValidationError(f"'{choice}' is not a valid choice.")
        
        return value
    
    def validate(self, data):
        """Validate the entire response"""
        # If "Other" is selected in question3, other_specification should be provided
        if 'Other' in data.get('question3', []):
            if not data.get('other_specification') or not data.get('other_specification').strip():
                raise serializers.ValidationError({
                    'other_specification': 'Please specify your other challenge when selecting "Other".'
                })
        
        return data
