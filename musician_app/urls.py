from django.urls import path
from . import views
urlpatterns = [
    # ('signup/',views.)
    path('', views.Home.as_view(), name="home"),
    path('add_musian/', views.AddMusian.as_view(), name="add_musian"),
    path('add_album/', views.AddAlbum.as_view(), name="add_album"),
    path('delete_row/<int:id>/', views.DeleteFromTable.as_view(), name="delete_row"),
    path('edit_album/<int:id>/', views.EditAlbum.as_view(), name='edit_album'),
    path('edit_musician/<int:id>/',
         views.EditMusician.as_view(), name='edit_musician'),
]
