from django.shortcuts import render

# Create your views here.
def TestView(request):
    return render(request, 'test.html')

def TestNavView(request):
    return render(request, 'nav-sample.html')

def InventoryView(request):
    return render(request, 'merchinventory.html')