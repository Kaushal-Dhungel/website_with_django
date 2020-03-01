from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .forms import UserForm , CustomForm
from .models import mydatabase
from django.db.models import Q
# Create your views here.

def mainbody (request):
    return render(request, 'mainbody.html')
    
def mainaboutus (request):
    return render (request, 'mainaboutus.html')

#def newsignup (request):
   # return render (request, 'newsignup.html')

#def profile(request):
 #   return render(request, 'profile.html')

#def enterlogin(request):
 #   return render(request, 'login.html')

    
    
    
def profile(request):
    #mydb = mydatabase.objects.all()
    
    #context = {
     #   'location': mydb.location,
     #   'b_group': mydb.b_group
   # }
    
    return render(request, 'profile.html') 
    
    
def login(request):
    
    if request.method == "POST":
        username = request.POST['phone']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request, user)
            print ("registered")
            return redirect('/profile')
        
        else:
            print("invalid")
            messages.info(request, 'Invalid Username/Password')
            return redirect('/login')
    else:
        return render (request,'login.html')


def newsignup(request):
    
    #context = RequestContext(request)

    

    if request.method == 'POST':
    
        user_form = UserForm(data=request.POST)
        profile_form = CustomForm(data=request.POST)
    
        registered = False
        if user_form.is_valid() and profile_form.is_valid():
        
            user = user_form.save()
        
        
            user.set_password(user.password)
            user.save()
      
            profile = profile_form.save(commit=False)
            profile.user = user
        
            profile.save()
            
            return render (request, 'aftersignup.html')

        else:
            
            return redirect('/newsignup')
            
    else:
        #return render (request, 'newsignup.html')

    #return render( 
    # 'newsignup.html',
    # {'user_form': user_form, 'profile_form': profile_form, 'registered':registered}, 
    # context)  
        user_form = UserForm()
        profile_form = CustomForm()
    
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'newsignup.html', context)

#def register(request):
 #   pass

def logout(request):
    auth.logout(request)
    return redirect('/')



#def profile(request):
    #db = User.objects.all()
   # idd = User.id
   # mydb = mydatabase.objects.get(user_id = 1)
    #context = {
    #    'location': mydb.location,
    #    'b_group': mydb.b_group
   # }
    
    #return render(request, 'profile.html', context) 
    
    
    
def searchresult(request):
    srch1 = request.POST['bgrp']
    srch2 = request.POST['address']
    
    if srch1 and srch2:
        
        match = mydatabase.objects.filter(Q(b_group__iexact = srch1) , Q(location__iexact = srch2))
        
        if match:
            return render(request, 'searchresult.html',{'srch': match})
        else:
            print ("not found")
            messages.info(request, 'Search unsuccessful. No match found.')
            return redirect('/mainbody')
            
    else:
        return redirect('/mainbody')
    
#def searchresult(request):
 #   return render(request, 'searchresult.html')
                                         