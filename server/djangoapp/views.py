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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Mock data for dealer reviews with correct fields
DEALER_REVIEWS_DATA = {
    1: [
        {
            "id": 1,
            "name": "John D.",
            "dealership": 1,
            "review": "Excellent service! Highly recommend.",
            "purchase": True,
            "purchase_date": "2025-01-15",
            "car_make": "Toyota",
            "car_model": "Camry",
            "car_year": 2024
        },
        {
            "id": 2,
            "name": "Sarah M.",
            "dealership": 1,
            "review": "Good experience, fair prices.",
            "purchase": True,
            "purchase_date": "2025-01-10",
            "car_make": "Honda",
            "car_model": "Accord",
            "car_year": 2024
        },
        {
            "id": 3,
            "name": "Michael R.",
            "dealership": 1,
            "review": "Great selection of cars!",
            "purchase": False,
            "purchase_date": None,
            "car_make": None,
            "car_model": None,
            "car_year": None
        }
    ],
    2: [
        {
            "id": 4,
            "name": "Emily W.",
            "dealership": 2,
            "review": "Amazing car selection and friendly staff!",
            "purchase": True,
            "purchase_date": "2025-02-01",
            "car_make": "BMW",
            "car_model": "3 Series",
            "car_year": 2024
        },
        {
            "id": 5,
            "name": "David L.",
            "dealership": 2,
            "review": "Professional service, good deals.",
            "purchase": True,
            "purchase_date": "2025-01-20",
            "car_make": "Mercedes-Benz",
            "car_model": "C-Class",
            "car_year": 2024
        }
    ],
    3: [
        {
            "id": 6,
            "name": "Lisa M.",
            "dealership": 3,
            "review": "Excellent customer service!",
            "purchase": True,
            "purchase_date": "2025-02-05",
            "car_make": "Ford",
            "car_model": "Mustang",
            "car_year": 2024
        }
    ]
}

@csrf_exempt
def fetch_dealer_reviews(request, dealer_id):
    """
    API endpoint for fetching dealer reviews
    Expected: GET to /fetchReviews/dealer/<dealer_id>
    Response: JSON with review fields including name, dealership, review, purchase, purchase_date, car_make, car_model, car_year
    """
    if request.method == 'GET':
        try:
            reviews = DEALER_REVIEWS_DATA.get(dealer_id, [])
            return JsonResponse({
                'reviews': reviews,
                'total': len(reviews)
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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# 50 Dealers data with all required fields
ALL_DEALERS_50 = [
    {"id": 1, "city": "New York", "state": "NY", "address": "123 Broadway", "zip": "10001", "lat": "40.7128", "long": "-74.0060", "short_name": "NY Auto", "full_name": "New York Auto Sales"},
    {"id": 2, "city": "Los Angeles", "state": "CA", "address": "456 Hollywood Blvd", "zip": "90028", "lat": "34.0522", "long": "-118.2437", "short_name": "LA Cars", "full_name": "Los Angeles Car Dealership"},
    {"id": 3, "city": "Chicago", "state": "IL", "address": "789 Michigan Ave", "zip": "60601", "lat": "41.8781", "long": "-87.6298", "short_name": "Chi Town", "full_name": "Chicago Motor Company"},
    {"id": 4, "city": "Houston", "state": "TX", "address": "321 Main St", "zip": "77001", "lat": "29.7604", "long": "-95.3698", "short_name": "H-Town Auto", "full_name": "Houston Auto Group"},
    {"id": 5, "city": "Phoenix", "state": "AZ", "address": "654 Camelback Rd", "zip": "85001", "lat": "33.4484", "long": "-112.0740", "short_name": "Phoenix Cars", "full_name": "Phoenix Motor Sales"},
    {"id": 6, "city": "Philadelphia", "state": "PA", "address": "147 Market St", "zip": "19101", "lat": "39.9526", "long": "-75.1652", "short_name": "Philly Auto", "full_name": "Philadelphia Auto Dealers"},
    {"id": 7, "city": "San Antonio", "state": "TX", "address": "258 Riverwalk", "zip": "78201", "lat": "29.4241", "long": "-98.4936", "short_name": "SA Motors", "full_name": "San Antonio Motor Group"},
    {"id": 8, "city": "San Diego", "state": "CA", "address": "369 Pacific Hwy", "zip": "92101", "lat": "32.7157", "long": "-117.1611", "short_name": "SD Auto", "full_name": "San Diego Auto Sales"},
    {"id": 9, "city": "Dallas", "state": "TX", "address": "741 Commerce St", "zip": "75201", "lat": "32.7767", "long": "-96.7970", "short_name": "Big D Cars", "full_name": "Dallas Motor Company"},
    {"id": 10, "city": "San Jose", "state": "CA", "address": "852 Silicon Way", "zip": "95101", "lat": "37.3382", "long": "-121.8863", "short_name": "SJ Auto", "full_name": "San Jose Auto Group"},
    {"id": 11, "city": "Austin", "state": "TX", "address": "963 Congress Ave", "zip": "78701", "lat": "30.2672", "long": "-97.7431", "short_name": "ATX Cars", "full_name": "Austin Motor Sales"},
    {"id": 12, "city": "Jacksonville", "state": "FL", "address": "159 Beach Blvd", "zip": "32201", "lat": "30.3322", "long": "-81.6557", "short_name": "Jax Auto", "full_name": "Jacksonville Auto Dealers"},
    {"id": 13, "city": "Fort Worth", "state": "TX", "address": "753 Stockyard", "zip": "76101", "lat": "32.7555", "long": "-97.3308", "short_name": "FW Motors", "full_name": "Fort Worth Motor Group"},
    {"id": 14, "city": "Columbus", "state": "OH", "address": "159 High St", "zip": "43201", "lat": "39.9612", "long": "-82.9988", "short_name": "Ohio Auto", "full_name": "Columbus Auto Sales"},
    {"id": 15, "city": "Charlotte", "state": "NC", "address": "753 Trade St", "zip": "28201", "lat": "35.2271", "long": "-80.8431", "short_name": "Queen City", "full_name": "Charlotte Motor Company"},
    {"id": 16, "city": "Detroit", "state": "MI", "address": "123 Motor City", "zip": "48201", "lat": "42.3314", "long": "-83.0458", "short_name": "Motor City", "full_name": "Detroit Auto Group"},
    {"id": 17, "city": "El Paso", "state": "TX", "address": "456 Border Hwy", "zip": "79901", "lat": "31.7619", "long": "-106.4850", "short_name": "El Paso Auto", "full_name": "El Paso Motor Sales"},
    {"id": 18, "city": "Memphis", "state": "TN", "address": "789 Elvis Blvd", "zip": "38101", "lat": "35.1495", "long": "-90.0490", "short_name": "Memphis Cars", "full_name": "Memphis Auto Dealers"},
    {"id": 19, "city": "Boston", "state": "MA", "address": "321 Beacon St", "zip": "02101", "lat": "42.3601", "long": "-71.0589", "short_name": "Beantown Auto", "full_name": "Boston Motor Group"},
    {"id": 20, "city": "Seattle", "state": "WA", "address": "654 Pike St", "zip": "98101", "lat": "47.6062", "long": "-122.3321", "short_name": "Emerald City", "full_name": "Seattle Auto Sales"},
    {"id": 21, "city": "Denver", "state": "CO", "address": "147 Colorado Blvd", "zip": "80201", "lat": "39.7392", "long": "-104.9903", "short_name": "Mile High", "full_name": "Denver Motor Company"},
    {"id": 22, "city": "Washington", "state": "DC", "address": "258 Capitol St", "zip": "20001", "lat": "38.9072", "long": "-77.0369", "short_name": "DC Auto", "full_name": "Washington Auto Group"},
    {"id": 23, "city": "Nashville", "state": "TN", "address": "369 Music Row", "zip": "37201", "lat": "36.1627", "long": "-86.7816", "short_name": "Music City", "full_name": "Nashville Motor Sales"},
    {"id": 24, "city": "Baltimore", "state": "MD", "address": "741 Harbor St", "zip": "21201", "lat": "39.2904", "long": "-76.6122", "short_name": "Bmore Auto", "full_name": "Baltimore Auto Dealers"},
    {"id": 25, "city": "Louisville", "state": "KY", "address": "852 Derby Ave", "zip": "40201", "lat": "38.2527", "long": "-85.7585", "short_name": "Derby City", "full_name": "Louisville Motor Group"},
    {"id": 26, "city": "Milwaukee", "state": "WI", "address": "963 Lakefront", "zip": "53201", "lat": "43.0389", "long": "-87.9065", "short_name": "Milw Auto", "full_name": "Milwaukee Auto Sales"},
    {"id": 27, "city": "Portland", "state": "OR", "address": "159 Burnside St", "zip": "97201", "lat": "45.5051", "long": "-122.6750", "short_name": "Rose City", "full_name": "Portland Motor Company"},
    {"id": 28, "city": "Oklahoma City", "state": "OK", "address": "753 Thunder Blvd", "zip": "73101", "lat": "35.4676", "long": "-97.5164", "short_name": "OKC Auto", "full_name": "Oklahoma City Auto Group"},
    {"id": 29, "city": "Las Vegas", "state": "NV", "address": "159 Strip Blvd", "zip": "89101", "lat": "36.1699", "long": "-115.1398", "short_name": "Vegas Cars", "full_name": "Las Vegas Motor Sales"},
    {"id": 30, "city": "Albuquerque", "state": "NM", "address": "753 Central Ave", "zip": "87101", "lat": "35.0853", "long": "-106.6056", "short_name": "ABQ Auto", "full_name": "Albuquerque Auto Dealers"},
    {"id": 31, "city": "Tucson", "state": "AZ", "address": "456 Desert Blvd", "zip": "85701", "lat": "32.2226", "long": "-110.9747", "short_name": "Tucson Motors", "full_name": "Tucson Motor Group"},
    {"id": 32, "city": "Fresno", "state": "CA", "address": "789 Vineyard Ave", "zip": "93650", "lat": "36.7468", "long": "-119.7726", "short_name": "Fresno Auto", "full_name": "Fresno Auto Sales"},
    {"id": 33, "city": "Sacramento", "state": "CA", "address": "321 Capitol Mall", "zip": "94203", "lat": "38.5816", "long": "-121.4944", "short_name": "Sactown Auto", "full_name": "Sacramento Motor Company"},
    {"id": 34, "city": "Long Beach", "state": "CA", "address": "654 Shoreline", "zip": "90802", "lat": "33.7701", "long": "-118.1937", "short_name": "LB Auto", "full_name": "Long Beach Auto Group"},
    {"id": 35, "city": "Kansas City", "state": "MO", "address": "741 Plaza St", "zip": "64101", "lat": "39.0997", "long": "-94.5786", "short_name": "KC Motors", "full_name": "Kansas City Motor Sales"},
    {"id": 36, "city": "Mesa", "state": "AZ", "address": "852 Main St", "zip": "85201", "lat": "33.4152", "long": "-111.8315", "short_name": "Mesa Auto", "full_name": "Mesa Auto Dealers"},
    {"id": 37, "city": "Atlanta", "state": "GA", "address": "963 Peachtree", "zip": "30301", "lat": "33.7490", "long": "-84.3880", "short_name": "Hotlanta Auto", "full_name": "Atlanta Motor Group"},
    {"id": 38, "city": "Miami", "state": "FL", "address": "159 Ocean Dr", "zip": "33101", "lat": "25.7617", "long": "-80.1918", "short_name": "MIA Cars", "full_name": "Miami Auto Sales"},
    {"id": 39, "city": "Raleigh", "state": "NC", "address": "753 Capital Blvd", "zip": "27601", "lat": "35.7796", "long": "-78.6382", "short_name": "Raleigh Auto", "full_name": "Raleigh Motor Company"},
    {"id": 40, "city": "Omaha", "state": "NE", "address": "159 Dodge St", "zip": "68101", "lat": "41.2565", "long": "-95.9345", "short_name": "Omaha Motors", "full_name": "Omaha Auto Group"},
    {"id": 41, "city": "Tulsa", "state": "OK", "address": "456 Cherokee Ave", "zip": "74101", "lat": "36.1540", "long": "-95.9928", "short_name": "Tulsa Auto", "full_name": "Tulsa Motor Sales"},
    {"id": 42, "city": "Oakland", "state": "CA", "address": "789 Lake Merritt", "zip": "94601", "lat": "37.8044", "long": "-122.2711", "short_name": "Oakland Cars", "full_name": "Oakland Auto Dealers"},
    {"id": 43, "city": "Minneapolis", "state": "MN", "address": "321 Nicolette", "zip": "55401", "lat": "44.9778", "long": "-93.2650", "short_name": "Twin Cities", "full_name": "Minneapolis Motor Group"},
    {"id": 44, "city": "Wichita", "state": "KS", "address": "654 Douglas Ave", "zip": "67201", "lat": "37.6872", "long": "-97.3301", "short_name": "Wichita Auto", "full_name": "Wichita Auto Sales"},
    {"id": 45, "city": "New Orleans", "state": "LA", "address": "147 Bourbon St", "zip": "70101", "lat": "29.9511", "long": "-90.0715", "short_name": "NOLA Cars", "full_name": "New Orleans Motor Company"},
    {"id": 46, "city": "Cleveland", "state": "OH", "address": "258 Rockwell Ave", "zip": "44101", "lat": "41.4993", "long": "-81.6944", "short_name": "CLE Auto", "full_name": "Cleveland Auto Group"},
    {"id": 47, "city": "Tampa", "state": "FL", "address": "369 Bay Shore", "zip": "33601", "lat": "27.9506", "long": "-82.4572", "short_name": "Tampa Motors", "full_name": "Tampa Motor Sales"},
    {"id": 48, "city": "Pittsburgh", "state": "PA", "address": "741 Steel City", "zip": "15201", "lat": "40.4406", "long": "-79.9959", "short_name": "Pgh Auto", "full_name": "Pittsburgh Auto Dealers"},
    {"id": 49, "city": "St. Louis", "state": "MO", "address": "852 Arch Blvd", "zip": "63101", "lat": "38.6270", "long": "-90.1994", "short_name": "STL Motors", "full_name": "St. Louis Motor Group"},
    {"id": 50, "city": "Salt Lake City", "state": "UT", "address": "963 Temple Square", "zip": "84101", "lat": "40.7608", "long": "-111.8910", "short_name": "SLC Auto", "full_name": "Salt Lake City Auto Sales"}
]

@csrf_exempt
def fetch_all_dealers(request):
    """
    API endpoint for fetching all 50 dealers
    Expected: GET to /fetchDealers
    Response: JSON with 50 dealer objects including id, city, state, address, zip, lat, long, short_name, full_name
    """
    if request.method == 'GET':
        return JsonResponse({
            'dealers': ALL_DEALERS_50,
            'total': len(ALL_DEALERS_50)
        }, status=200)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Method not allowed. Use GET.'
    }, status=405)
