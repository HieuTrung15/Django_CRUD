from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', context)


def employee_update(request, id_emp=0):
    if request.method == 'GET':
        if id_emp == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(id=id_emp)
            form = EmployeeForm(employee)
        return render(request, 'employee_register/employee_form.html', {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request):
    return
