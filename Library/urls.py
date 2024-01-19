from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login, name='login'),
    path('add-blog',views.addblog,name='add-blog'),
    path('allposts',views.allposts,name='allposts'),
    path('post/<id>',views.post, name='post'),
    path('add-book',views.addbook,name='add-book'),
    path('get-book/<str:title>',views.getbook,name='get-book'),
    path('download-book/<str:title>',views.download,name='download-book'),
    path('all-books',views.allbooks,name='all-books'),
    path('logout',views.logout,name='logout'),
    path('contact',views.contact,name='contact'),
    path('thanks',views.thanks,name='thanks'),
    path('search',views.search,name='search'),
    path('search-results/<str:title>',views.search_results, name='search-results')
]
# 
