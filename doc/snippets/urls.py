# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [

    path('snippets/', views.SnippetList.as_view()),
    path('create_snippets/', views.CreateSnippet.as_view()),
    path('get_one/<int:pk>/', views.GetSnippetDetails.as_view()),
    path('delete/<int:pk>/', views.DeleteSnippetDetail.as_view()),
    path('update/<int:pk>/', views.UpdateSnippetDetail.as_view()),
    path('affinda/', views.AffindaNER.as_view()),

#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)  #API will be able to handle URls such as http://example.com/api/items/4.json rather than just http://example.com/api/items/4.b