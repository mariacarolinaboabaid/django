from django.urls import path, reverse_lazy
from .views import Public, Homepage, DetailsMovie, Search, EditProfile, CreateAccount
from django.contrib.auth import views as auth_views

app_name = 'movie'

urlpatterns = [
    # url -  view
    path('', Public.as_view(), name='public'),
    path('movies/', Homepage.as_view(), name='homepage'),
    path('movies/<int:pk>', DetailsMovie.as_view(), name='detailsMovie'),
    path('search/', Search.as_view(), name='search'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('editProfile/<int:pk>', EditProfile.as_view(), name='editProfile'),
    path('createAccount/', CreateAccount.as_view(), name='createAccount'),
    path('changePassword/', auth_views.PasswordChangeView.as_view(template_name='editProfile.html',
                                                                 success_url = reverse_lazy('movie:homepage')), name='changePassword')
]

