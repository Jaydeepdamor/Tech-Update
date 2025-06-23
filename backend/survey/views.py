from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
import json
import logging

from .models import SurveyResponse
from .serializers import SurveyResponseSerializer

# Set up logging
logger = logging.getLogger(__name__)


@api_view(['POST'])
@permission_classes([AllowAny])
def submit_survey(request):
    """
    Submit a survey response
    """
    try:
        # Log the incoming request
        logger.info(f"Received survey submission from IP: {request.META.get('REMOTE_ADDR')}")
        
        # Create serializer with request data
        serializer = SurveyResponseSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the survey response
            survey_response = serializer.save()
            
            logger.info(f"Survey response saved successfully with ID: {survey_response.id}")
            
            return Response({
                'success': True,
                'message': 'Survey submitted successfully!',
                'data': {
                    'id': survey_response.id,
                    'timestamp': survey_response.timestamp,
                    'email': survey_response.email
                }
            }, status=status.HTTP_201_CREATED)
        
        else:
            # Log validation errors
            logger.warning(f"Survey validation failed: {serializer.errors}")
            
            return Response({
                'success': False,
                'message': 'Validation failed',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        # Log unexpected errors
        logger.error(f"Unexpected error in survey submission: {str(e)}", exc_info=True)
        
        return Response({
            'success': False,
            'message': 'An unexpected error occurred. Please try again.',
            'error': str(e) if request.user.is_staff else 'Internal server error'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def survey_stats(request):
    """
    Get basic survey statistics (optional endpoint for analytics)
    """
    try:
        total_responses = SurveyResponse.objects.count()
        
        # Count responses for question 1
        q1_yes = SurveyResponse.objects.filter(question1='Yes').count()
        q1_no = SurveyResponse.objects.filter(question1='No').count()
        
        # Count responses for question 2  
        q2_yes = SurveyResponse.objects.filter(question2='Yes').count()
        q2_no = SurveyResponse.objects.filter(question2='No').count()
        
        return Response({
            'success': True,
            'data': {
                'total_responses': total_responses,
                'question1_stats': {
                    'yes': q1_yes,
                    'no': q1_no
                },
                'question2_stats': {
                    'yes': q2_yes,
                    'no': q2_no
                }
            }
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        logger.error(f"Error retrieving survey stats: {str(e)}", exc_info=True)
        
        return Response({
            'success': False,
            'message': 'Error retrieving statistics',
            'error': str(e) if request.user.is_staff else 'Internal server error'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def health_check(request):
    """
    Simple health check endpoint
    """
    return Response({
        'status': 'healthy',
        'message': 'Tech Survey API is running!',
        'timestamp': '2025-06-23'
    }, status=status.HTTP_200_OK)
