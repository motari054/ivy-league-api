from django.urls import path, include
from . import views

test_patterns = [
    path('', views.index),
    path('oauth/success', views.oauth_success),
    path('stk-push/success', views.stk_push_success),
]

urlpatterns = [
    path('', views.PaymentView.as_view()),
    path('tests/', include(test_patterns)),
]
