from django.shortcuts import render
from .models import menuItem, booking
from .forms import bookingForm
# Create your views here.
def menuItemView(request):
    context = {
        'menu': menuItem.objects.all().order_by('name'),
    }
    return render(request, 'menu.html', context)

def itemView(request, id):
    if id:
        context = {
            'item': menuItem.objects.get(pk = id),
        }
    return render(request, 'menu_item.html', context)

def indexView(request):
    return render(request, 'index.html')

def form_view(request):
    form = bookingForm()
    if request.method == 'POST':
        form = bookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'booking.html', context)

def aboutView(request):
    return render(request, 'about.html')