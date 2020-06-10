from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('Analysis',views.chart,name = 'chart'),
    path('Contact',views.contact),
    path('About',views.about),
    path('Graph',views.graph),
    path('Animated_Graph',views.tableau),
    path('Live_Chart',views.dataflow),
    path('Prediction',views.prediction),
    path('Cont',views.cont)
]
