from django.shortcuts import render
import requests

def GetMovie(request):
    if request.method=='POST':
        movie_name=request.POST["mv"]  
        rsp=requests.get(f'https://hrmoviesapi.herokuapp.com/mv/?search={movie_name}').json()
        src_mov=requests.get(f'https://hrmoviesapi.herokuapp.com/mv/?').json()
        return render(request,'show.html',{'mvs':rsp,'atc':src_mov})


    else:
        src_mov=requests.get(f'https://hrmoviesapi.herokuapp.com/mv/?').json()
        return render(request,'show.html',{'atc':src_mov})
