from django.urls import path
# from .views import PostList, PostDetail

app_name='blog_api'

urlpatterns=[
    # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    # path('', PostList.as_view(), name='listcreate'),
]
#our model is going to be a table in a database that is going to store all the post data
#our api is going to serve post data to the react application .