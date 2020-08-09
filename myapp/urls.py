from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('trail/',views.trial,name="Trial"),
    path('profile/',views.profile,name="profile"),
    path('fact/<f>',views.fact,name='fact'),
    path('child/',views.child,name="child"),

]