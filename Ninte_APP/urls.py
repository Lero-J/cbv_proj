from django.urls import path

from Ninte_APP.views import MainPage, MainView2, PostListView, PostDetailView, PostCreateView, PostUpdateView, \
    PostDeleteView

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('template_view/', MainView2.as_view(), name='template_view'),
    path('list/',PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
