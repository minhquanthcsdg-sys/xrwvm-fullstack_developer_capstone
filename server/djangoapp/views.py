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

@csrf_exempt
def get_dealers_by_state(request, state):
    """
    Get dealers by state
    """
    if request.method == 'GET':
        # Mock data for dealers with state information
        ALL_DEALERS = [
            {"id": 1, "name": "Best Cars Downtown", "address": "123 Main St, Detroit, MI", "state": "MI", "phone": "+1 (800) 555-0001", "rating": 4.5},
            {"id": 2, "name": "AutoWorld", "address": "456 Oak Ave, Chicago, IL", "state": "IL", "phone": "+1 (800) 555-0002", "rating": 4.2},
            {"id": 3, "name": "DriveTime Motors", "address": "789 Elm Blvd, New York, NY", "state": "NY", "phone": "+1 (800) 555-0003", "rating": 3.8},
            {"id": 4, "name": "Premium Auto Sales", "address": "321 Pine St, Los Angeles, CA", "state": "CA", "phone": "+1 (800) 555-0004", "rating": 4.7},
            {"id": 5, "name": "City Cars", "address": "654 Maple Ave, Houston, TX", "state": "TX", "phone": "+1 (800) 555-0005", "rating": 4.0},
            {"id": 6, "name": "Kansas City Motors", "address": "789 Broadway, Kansas City, KS", "state": "KS", "phone": "+1 (800) 555-0006", "rating": 4.3},
            {"id": 7, "name": "Topeka Auto Sales", "address": "123 Capitol Ave, Topeka, KS", "state": "KS", "phone": "+1 (800) 555-0007", "rating": 3.9},
            {"id": 8, "name": "Wichita Cars", "address": "456 Douglas Ave, Wichita, KS", "state": "KS", "phone": "+1 (800) 555-0008", "rating": 4.1},
            {"id": 9, "name": "Sunflower Motors", "address": "789 State St, Lawrence, KS", "state": "KS", "phone": "+1 (800) 555-0009", "rating": 4.4}
        ]
        
        # Filter dealers by state (case insensitive)
        dealers_in_state = [d for d in ALL_DEALERS if d['state'].upper() == state.upper()]
        
        if dealers_in_state:
            return JsonResponse({
                'state': state.upper(),
                'dealers': dealers_in_state,
                'total': len(dealers_in_state)
            }, status=200)
        return JsonResponse({
            'state': state.upper(),
            'dealers': [],
            'total': 0,
            'message': f'No dealers found in {state.upper()}'
        }, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

# Mock data for car makes and models
CAR_MAKES_AND_MODELS = {
    "makes": [
        {
            "id": 1,
            "name": "Toyota",
            "country": "Japan",
            "models": [
                {"id": 101, "name": "Camry", "year": 2024, "price": 28000},
                {"id": 102, "name": "Corolla", "year": 2024, "price": 22000},
                {"id": 103, "name": "RAV4", "year": 2024, "price": 31000},
                {"id": 104, "name": "Highlander", "year": 2024, "price": 38000}
            ]
        },
        {
            "id": 2,
            "name": "Honda",
            "country": "Japan",
            "models": [
                {"id": 201, "name": "Accord", "year": 2024, "price": 27000},
                {"id": 202, "name": "Civic", "year": 2024, "price": 24000},
                {"id": 203, "name": "CR-V", "year": 2024, "price": 30000},
                {"id": 204, "name": "Pilot", "year": 2024, "price": 37000}
            ]
        },
        {
            "id": 3,
            "name": "Ford",
            "country": "USA",
            "models": [
                {"id": 301, "name": "Mustang", "year": 2024, "price": 32000},
                {"id": 302, "name": "F-150", "year": 2024, "price": 35000},
                {"id": 303, "name": "Escape", "year": 2024, "price": 29000},
                {"id": 304, "name": "Explorer", "year": 2024, "price": 36000}
            ]
        },
        {
            "id": 4,
            "name": "Chevrolet",
            "country": "USA",
            "models": [
                {"id": 401, "name": "Malibu", "year": 2024, "price": 25000},
                {"id": 402, "name": "Silverado", "year": 2024, "price": 38000},
                {"id": 403, "name": "Equinox", "year": 2024, "price": 28000},
                {"id": 404, "name": "Tahoe", "year": 2024, "price": 42000}
            ]
        },
        {
            "id": 5,
            "name": "BMW",
            "country": "Germany",
            "models": [
                {"id": 501, "name": "3 Series", "year": 2024, "price": 42000},
                {"id": 502, "name": "5 Series", "year": 2024, "price": 54000},
                {"id": 503, "name": "X3", "year": 2024, "price": 46000},
                {"id": 504, "name": "X5", "year": 2024, "price": 62000}
            ]
        },
        {
            "id": 6,
            "name": "Mercedes-Benz",
            "country": "Germany",
            "models": [
                {"id": 601, "name": "C-Class", "year": 2024, "price": 44000},
                {"id": 602, "name": "E-Class", "year": 2024, "price": 56000},
                {"id": 603, "name": "GLC", "year": 2024, "price": 48000},
                {"id": 604, "name": "GLE", "year": 2024, "price": 64000}
            ]
        },
        {
            "id": 7,
            "name": "Tesla",
            "country": "USA",
            "models": [
                {"id": 701, "name": "Model 3", "year": 2024, "price": 45000},
                {"id": 702, "name": "Model S", "year": 2024, "price": 75000},
                {"id": 703, "name": "Model X", "year": 2024, "price": 80000},
                {"id": 704, "name": "Model Y", "year": 2024, "price": 50000}
            ]
        }
    ],
    "total_makes": 7,
    "total_models": 28
}

@csrf_exempt
def get_all_car_makes(request):
    """
    Get all car makes and their models
    """
    if request.method == 'GET':
        return JsonResponse(CAR_MAKES_AND_MODELS, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def get_car_make_by_id(request, make_id):
    """
    Get car make by ID with its models
    """
    if request.method == 'GET':
        make = next((m for m in CAR_MAKES_AND_MODELS['makes'] if m['id'] == make_id), None)
        if make:
            return JsonResponse({'make': make}, status=200)
        return JsonResponse({'error': 'Car make not found'}, status=404)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def get_car_models_by_make(request, make_name):
    """
    Get car models by make name
    """
    if request.method == 'GET':
        make = next((m for m in CAR_MAKES_AND_MODELS['makes'] if m['name'].lower() == make_name.lower()), None)
        if make:
            return JsonResponse({
                'make': make['name'],
                'models': make['models'],
                'total': len(make['models'])
            }, status=200)
        return JsonResponse({'error': 'Car make not found'}, status=404)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

import re
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Simple sentiment analysis function
def analyze_sentiment(text):
    """
    Simple sentiment analysis based on keyword matching
    Returns: dict with sentiment, score, and confidence
    """
    text_lower = text.lower()
    
    # Positive keywords
    positive_words = [
        'fantastic', 'excellent', 'great', 'good', 'amazing', 'wonderful', 
        'best', 'perfect', 'outstanding', 'superb', 'exceptional', 'awesome',
        'love', 'like', 'nice', 'brilliant', 'incredible', 'remarkable'
    ]
    
    # Negative keywords
    negative_words = [
        'bad', 'terrible', 'awful', 'horrible', 'worst', 'poor', 'disappointing',
        'hate', 'dislike', 'unacceptable', 'terrible', 'mediocre', 'subpar'
    ]
    
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    # Calculate sentiment
    if positive_count > negative_count:
        sentiment = 'positive'
        score = positive_count / (positive_count + negative_count + 1)
        confidence = min(0.95, 0.7 + (positive_count * 0.1))
    elif negative_count > positive_count:
        sentiment = 'negative'
        score = -negative_count / (positive_count + negative_count + 1)
        confidence = min(0.95, 0.7 + (negative_count * 0.1))
    else:
        sentiment = 'neutral'
        score = 0
        confidence = 0.5
    
    return {
        'sentiment': sentiment,
        'score': round(score, 3),
        'confidence': round(confidence, 3),
        'text': text,
        'positive_words_found': positive_count,
        'negative_words_found': negative_count
    }

@csrf_exempt
def analyze_review_sentiment(request):
    """
    Analyze sentiment of a review text
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            review_text = data.get('review', '')
            
            if not review_text:
                return JsonResponse({
                    'error': 'Review text is required'
                }, status=400)
            
            # Analyze sentiment
            result = analyze_sentiment(review_text)
            
            return JsonResponse({
                'status': 'success',
                'analysis': result
            }, status=200)
            
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON format'
            }, status=400)
    
    elif request.method == 'GET':
        # For GET request, use query parameter
        review_text = request.GET.get('review', '')
        
        if not review_text:
            return JsonResponse({
                'error': 'Review text is required as query parameter'
            }, status=400)
        
        result = analyze_sentiment(review_text)
        
        return JsonResponse({
            'status': 'success',
            'analysis': result
        }, status=200)
    
    return JsonResponse({
        'error': 'Method not allowed. Use POST or GET.'
    }, status=405)

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_user(request):
    """
    API endpoint for user login
    """
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'status': 'success',
                    'message': 'Login successful',
                    'username': username,
                    'email': user.email,
                    'user_id': user.id
                }, status=200)
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Invalid credentials'
                }, status=401)
                
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON format'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Method not allowed. Use POST.'
    }, status=405)

from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@csrf_exempt
def logout_user(request):
    """
    API endpoint for user logout
    """
    if request.method == 'POST':
        try:
            # Check if user is logged in
            if request.user.is_authenticated:
                username = request.user.username
                logout(request)
                return JsonResponse({
                    'status': 'success',
                    'message': f'User {username} logged out successfully'
                }, status=200)
            else:
                return JsonResponse({
                    'status': 'info',
                    'message': 'No user is currently logged in'
                }, status=200)
                
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Method not allowed. Use POST.'
    }, status=405)

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_user(request):
    """
    API endpoint for user login
    Expected: POST to /djangoapp/login with {"userName": "username", "password": "password"}
    Response: {"userName": "username", "status": "Authenticated"}
    """
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
            username = data.get('userName')  # Changed from 'username' to 'userName'
            password = data.get('password')
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'userName': username,
                    'status': 'Authenticated'
                }, status=200)
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Invalid credentials'
                }, status=401)
                
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON format'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Method not allowed. Use POST.'
    }, status=405)

from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def logout_user(request):
    """
    API endpoint for user logout
    Expected: GET to /djangoapp/logout
    Response: {"userName": ""}
    """
    if request.method == 'GET':
        try:
            # Get username before logout
            username = request.user.username if request.user.is_authenticated else ""
            
            # Perform logout
            logout(request)
            
            return JsonResponse({
                'userName': ''
            }, status=200)
                
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Method not allowed. Use GET.'
    }, status=405)
