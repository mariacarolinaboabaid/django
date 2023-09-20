from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from .models import Movie, Trailer, User
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateAccountForm, FormPublic

class Public(FormView):
    template_name = 'public.html'
    form_class = FormPublic
    
    #  Adding the views
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('movie:homepage')
        else:
            return super(Public, self).get(request, *args, **kwargs) # Go to url
    
    # Method access 
    def get_success_url(self):
        email = self.request.POST.get("email")
        user_find = User.objects.filter(email=email)
        if user_find:
            return reverse('movie:login')
        else:
            return reverse('movie:createAccount')
    
    
class Homepage(LoginRequiredMixin, ListView):
    template_name = 'homepage.html'
    model = Movie
    # object_list


class DetailsMovie(LoginRequiredMixin, DetailView):
    template_name = 'detailMovie.html'
    model = Movie
    # object

    #  Adding the views
    def get(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.views += 1
        movie.save()
        user = request.user
        user.seen_movies.add(movie)
        return super(DetailsMovie, self).get(request, *args, **kwargs) # Go to url
    
    # Related movies
    def get_context_data(self, **kwargs):
        context = super(DetailsMovie, self).get_context_data(**kwargs)
        relatedMovies = self.model.objects.filter(Q(category=self.get_object().category) & ~Q(title=self.get_object().title))
        context['relatedMovies'] = relatedMovies
        return context


class Search(LoginRequiredMixin, ListView):
    template_name = 'search.html'
    model = Movie
    
    def get_queryset(self):
        search_term = self.request.GET.get('query')
        if search_term:
            object_list = self.model.objects.filter(Q(title__icontains=search_term) | Q(category__icontains=search_term))
            return object_list
        else:
            return None        


class EditProfile(LoginRequiredMixin, UpdateView):
    template_name = 'editProfile.html'
    model = User
    fields = ['first_name', 'last_name', 'email']
    
    def get_success_url(self):
        return reverse('movie:homepage')
    
    
    
class CreateAccount(FormView):
    template_name = 'createAccount.html'
    form_class = CreateAccountForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('movie:login')
    