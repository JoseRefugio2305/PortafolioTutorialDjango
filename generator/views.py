from django.shortcuts import render
import random
#from django.http import HttpResponse 

def about(request):
    #return HttpResponse('Hola mundo')#Formateamos la cadena a un Http response
    return render(request, 'about.html')

def home(request):
    #return HttpResponse('Hola mundo')#Formateamos la cadena a un Http response
    return render(request, 'home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_pass=''
    length_pass=int(request.GET.get('length'))

    if(request.GET.get('uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if(request.GET.get('special')):
        characters.extend(list('-_!#@$%^&*()/?=+[]{}'))
    if(request.GET.get('numbers')):
        characters.extend(list('1234567890'))
    if(request.GET.get('use_n')):
        characters.extend(list('ñÑ'))

    for x in range(length_pass):
        generated_pass+=random.choice(characters)
    return render(request,'password.html',{'password':generated_pass})