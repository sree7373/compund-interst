from django.shortcuts import render

# Create your views here.
def calculate_interest(request):
    if request.method == 'POST':
        principal = float(request.POST['principal'])
        time = float(request.POST['time'])
        rate = float(request.POST['rate'])
        compound_interest = principal * (pow((1 + rate / 100), time))
        context = {'compound_interest': round(compound_interest, 2)}
        return render(request, 'result.html', context)
    return render(request, 'index.html')