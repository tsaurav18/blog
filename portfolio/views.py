from django.shortcuts import render

# Create your view
def portfolio(request):
    return render(request,'portfolio.html')
