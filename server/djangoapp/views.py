from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'message': 'Login successful',
                    'username': username
                }, status=200)
            else:
                return JsonResponse({
                    'error': 'Invalid credentials'
                }, status=401)
        except:
            return JsonResponse({
                'error': 'Invalid request'
            }, status=400)
    return JsonResponse({
        'error': 'Method not allowed'
    }, status=405)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Mock data for dealer reviews
DEALER_REVIEWS = {
    1: [
        {"id": 1, "dealer_id": 1, "reviewer": "John D.", "rating": 5, "comment": "Excellent service! Highly recommend.", "date": "2025-02-15"},
        {"id": 2, "dealer_id": 1, "reviewer": "Sarah M.", "rating": 4, "comment": "Good experience, fair prices.", "date": "2025-02-14"}
    ],
    2: [
        {"id": 3, "dealer_id": 2, "reviewer": "Mike R.", "rating": 3, "comment": "Decent dealership, could improve customer service.", "date": "2025-02-13"},
        {"id": 4, "dealer_id": 2, "reviewer": "Emily W.", "rating": 5, "comment": "Amazing car selection!", "date": "2025-02-12"}
    ],
    3: [
        {"id": 5, "dealer_id": 3, "reviewer": "David L.", "rating": 4, "comment": "Professional staff, good deals.", "date": "2025-02-11"}
    ]
}

@csrf_exempt
def get_dealer_reviews(request, dealer_id):
    """
    Get reviews for a specific dealer
    """
    if request.method == 'GET':
        reviews = DEALER_REVIEWS.get(dealer_id, [])
        return JsonResponse({
            'dealer_id': dealer_id,
            'reviews': reviews,
            'total_reviews': len(reviews)
        }, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def get_all_dealers(request):
    """
    Get all dealers (mock data)
    """
    if request.method == 'GET':
        dealers = [
            {"id": 1, "name": "Best Cars Downtown", "address": "123 Main St, Detroit, MI"},
            {"id": 2, "name": "AutoWorld", "address": "456 Oak Ave, Chicago, IL"},
            {"id": 3, "name": "DriveTime Motors", "address": "789 Elm Blvd, New York, NY"}
        ]
        return JsonResponse({'dealers': dealers}, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
