from django.shortcuts import render
from django.db.models import Count, Avg, Max
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .models import Item
from .forms import ItemForm
from django.core.paginator import Paginator


def item_list(request):
    item_list = Item.objects.all()
    paginator = Paginator(item_list, 9)  # 9 elementai per puslapį
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'katalogas/item_list.html', {'page_obj': page_obj})

# Paieška pagal kategorija / pavadinima
    category = request.GET.get('kategorija')
    if category:
        items = items.filter(category__name__icontains=category)

    context = {
        'items': items,
    }
    return render(request, 'katalogas/item_list.html', context)

def stats(request):
    categories_stats = Item.objects.values('category__name').annotate(
        count=Count('id'),
        avg_price=Avg('price'),
        max_price=Max('price'),
    ).order_by('-count')

    context = {
        'categories_stats': categories_stats,
    }
    return render(request, 'katalogas/stats.html', context)

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'katalogas/item_form.html'
    success_url = reverse_lazy('item_list')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'katalogas/item_confirm_delete.html'
    success_url = reverse_lazy('item_list')