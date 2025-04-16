from django.shortcuts import render
# Create your views here.
def homepage(request):
    return render(request,'testapp/home.html')

from .models import Movies
def listmovies(request):
    movies=Movies.objects.all()
    return render(request, 'testapp/list.html', {'movies':movies})

from .forms import MovieForm
def movieinfosubmit(request):
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    form = MovieForm()
    return render(request,'testapp/info.html', {'form':form})
