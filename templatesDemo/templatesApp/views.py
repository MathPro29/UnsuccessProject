from django.shortcuts import render

def renderTemplate(request):
    myDict = {"id": 6604101371,"name": "Methat Phornwisut"}
    return render(request, 'templatesApp/firstTemplate.html', context=myDict)

def renderEmployee(request):
    myDict = {"id": 6604101371, "name": "Methat Phornwisut", "sal": 999999}
    return render(request, 'templatesApp/employeeTemplate.html', context=myDict)
