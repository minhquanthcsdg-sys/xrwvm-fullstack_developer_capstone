from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from djangoapp.views import (
    login_user, 
    logout_user,
    fetch_dealer_reviews,
    fetch_all_dealers,
    fetch_dealer_by_id,
    get_all_dealers, 
    get_dealer_by_id, 
    get_dealers_by_state,
    get_all_car_makes,
    get_car_make_by_id,
    get_car_models_by_make,
    analyze_review_sentiment
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="Home.html")),
    path('about/', TemplateView.as_view(template_name="About.html")),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
    path('djangoapp/login/', login_user, name='login'),
    path('djangoapp/logout/', logout_user, name='logout'),
    path('fetchReviews/dealer/<int:dealer_id>/', fetch_dealer_reviews, name='fetch_reviews'),
    path('fetchDealers/', fetch_all_dealers, name='fetch_all_dealers'),
    path('fetchDealer/<int:dealer_id>/', fetch_dealer_by_id, name='fetch_dealer_by_id'),  # New endpoint
    path('api/dealers/', get_all_dealers, name='all_dealers'),
    path('api/dealer/<int:dealer_id>/', get_dealer_by_id, name='dealer_by_id'),
    path('api/dealers/state/<str:state>/', get_dealers_by_state, name='dealers_by_state'),
    path('api/carmakes/', get_all_car_makes, name='all_car_makes'),
    path('api/carmake/<int:make_id>/', get_car_make_by_id, name='car_make_by_id'),
    path('api/carmake/<str:make_name>/models/', get_car_models_by_make, name='car_models_by_make'),
    path('api/analyze/', analyze_review_sentiment, name='analyze_sentiment'),
]
