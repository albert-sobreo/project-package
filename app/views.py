from django.shortcuts import render

# Create your views here.
def TestView(request):
    return render(request, 'test.html')

def TestNavView(request):
    return render(request, 'nav-sample.html')

def InventoryView(request):
    return render(request, 'merchinventory.html')

def DeliveriesView(request):
    return render(request, 'deliveries.html')

def SalesView(request):
    return render(request, 'sales-contract.html')

def OrderView(requests):
    return render(requests, 'purchase-order.html')

def NekoView(request):
    return render(request, 'blackcat.html')

def RequestView(request):
    return render(request, 'purchase-request.html')

def ReportView(request):
    return render(request, 'receiving-report.html')

def ReportlistView(request):
    return render(request, 'rr-list.html')

def SaleslistView(request):
    return render(request, 'so-list.html')

def SalesorderView(request):
    return render(request, 'sales-order.html')

def TransferView(request):
    return render(request, 'inventory-transfer.html')

def AdjustmentsView(request):
    return render(request, 'inventory-adjustments.html')