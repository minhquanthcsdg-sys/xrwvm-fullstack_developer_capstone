from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from djangoapp.views import (
    login_user, 
    logout_user,
    get_dealer_reviews, 
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
    path('api/login/', login_user, name='login'),
    path('api/logout/', logout_user, name='logout'),
    path('api/dealer/<int:dealer_id>/reviews/', get_dealer_reviews, name='dealer_reviews'),
    path('api/dealers/', get_all_dealers, name='all_dealers'),
    path('api/dealer/<int:dealer_id>/', get_dealer_by_id, name='dealer_by_id'),
    path('api/dealers/state/<str:state>/', get_dealers_by_state, name='dealers_by_state'),
    path('api/carmakes/', get_all_car_makes, name='all_car_makes'),
    path('api/carmake/<int:make_id>/', get_car_make_by_id, name='car_make_by_id'),
    path('api/carmake/<str:make_name>/models/', get_car_models_by_make, name='car_models_by_make'),
    path('api/analyze/', analyze_review_sentiment, name='analyze_sentiment'),
]
