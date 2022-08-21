from django.shortcuts import render
import requests

def GetMovie(request):
    if request.method=='POST':
        movie_name=request.POST["mv"]  
        if len(movie_name) is not 0:
            rsp=requests.get(f'https://hrmoviesapi.herokuapp.com/mv/?search={movie_name}').json()
            return render(request,'show.html',{'mvs':rsp})
        else:
            return render(request,'show.html')

    else:
        return render(request,'show.html')
