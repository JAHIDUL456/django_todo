from django.shortcuts import render,redirect


def signup(request):
    if request.method=='POST':
        fnm=request.POST.get('fmn')
        email=request.POST.get('email')
        psw=request.POST.get('pass')
        print(fnm, email,psw)
    
        
    return render(request,'signup.html')
