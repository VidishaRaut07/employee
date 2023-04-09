from django.shortcuts import render
from .forms import EmployeeForm
from django.http import HttpResponse

# Create your views here.
def employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data added')

    template_name = 'add.html'
    context = {'form':form}
    return render(request, template_name, context)
