from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from . import api

urlpatterns = [
    #test Form
    path("api",api.dhtser,name='json'),

    #Table temp et hum, date
    path('index/',views.table,name='table'),

    path('download_csv/', views.download_csv, name='download_csv'),
    path('myChart/',views.graphique,name='myChart'),
    path ('chart-data/',views.chart_data, name='chart-data'),
    path('chart-data-jour/',views.chart_data_jour,name='chart-data-jour'),
    path('chart-data-semaine/',views.chart_data_semaine,name='chart-data-semaine'),
    path('chart-data-mois/',views.chart_data_mois,name='chart-data-mois'),

    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
