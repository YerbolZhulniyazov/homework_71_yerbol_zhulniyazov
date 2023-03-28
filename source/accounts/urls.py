from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, ProfileView, UserChangeView, SearchProfileView, \
    add_subscriptions, SubscriptionsView, SubscribersView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('profile/search', SearchProfileView.as_view(), name='search'),
    path('profile/add_subscriptions/<int:pk>', add_subscriptions, name='add_subscriptions'),
    path('profile/subsriptions/<int:pk>', SubscriptionsView.as_view(), name='subscriptions'),
    path('profile/subscribers/<int:pk>', SubscribersView.as_view(), name='subscribers'),
]
