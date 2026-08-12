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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Mock data for all dealers
ALL_DEALERS = [
    {"id": 1, "name": "Best Cars Downtown", "address": "123 Main St, Detroit, MI", "phone": "+1 (800) 555-0001", "rating": 4.5},
    {"id": 2, "name": "AutoWorld", "address": "456 Oak Ave, Chicago, IL", "phone": "+1 (800) 555-0002", "rating": 4.2},
    {"id": 3, "name": "DriveTime Motors", "address": "789 Elm Blvd, New York, NY", "phone": "+1 (800) 555-0003", "rating": 3.8},
    {"id": 4, "name": "Premium Auto Sales", "address": "321 Pine St, Los Angeles, CA", "phone": "+1 (800) 555-0004", "rating": 4.7},
    {"id": 5, "name": "City Cars", "address": "654 Maple Ave, Houston, TX", "phone": "+1 (800) 555-0005", "rating": 4.0}
]

@csrf_exempt
def get_all_dealers(request):
    """
    Get all dealers
    """
    if request.method == 'GET':
        return JsonResponse({
            'dealers': ALL_DEALERS,
            'total': len(ALL_DEALERS)
        }, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def get_dealer_by_id(request, dealer_id):
    """
    Get dealer by ID
    """
    if request.method == 'GET':
        dealer = next((d for d in ALL_DEALERS if d['id'] == dealer_id), None)
        if dealer:
            return JsonResponse({'dealer': dealer}, status=200)
        return JsonResponse({'error': 'Dealer not found'}, status=404)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def get_dealer_by_id(request, dealer_id):
    """
    Get dealer by ID
    """
    if request.method == 'GET':
        # Mock data for dealers
        ALL_DEALERS = [
            {"id": 1, "name": "Best Cars Downtown", "address": "123 Main St, Detroit, MI", "phone": "+1 (800) 555-0001", "rating": 4.5, "email": "info@bestcarsdowntown.com", "website": "www.bestcarsdowntown.com"},
            {"id": 2, "name": "AutoWorld", "address": "456 Oak Ave, Chicago, IL", "phone": "+1 (800) 555-0002", "rating": 4.2, "email": "info@autoworld.com", "website": "www.autoworld.com"},
            {"id": 3, "name": "DriveTime Motors", "address": "789 Elm Blvd, New York, NY", "phone": "+1 (800) 555-0003", "rating": 3.8, "email": "info@drivetimemotors.com", "website": "www.drivetimemotors.com"},
            {"id": 4, "name": "Premium Auto Sales", "address": "321 Pine St, Los Angeles, CA", "phone": "+1 (800) 555-0004", "rating": 4.7, "email": "info@premiumautosales.com", "website": "www.premiumautosales.com"},
            {"id": 5, "name": "City Cars", "address": "654 Maple Ave, Houston, TX", "phone": "+1 (800) 555-0005", "rating": 4.0, "email": "info@citycars.com", "website": "www.citycars.com"}
        ]
        
        dealer = next((d for d in ALL_DEALERS if d['id'] == dealer_id), None)
        if dealer:
            return JsonResponse({'dealer': dealer}, status=200)
        return JsonResponse({'error': 'Dealer not found'}, status=404)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
