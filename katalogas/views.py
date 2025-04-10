from django.shortcuts import render
from django.db.models import Count, Avg, Max
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
from .models import Item
from .forms import ItemForm
from django.core.paginator import Paginator


def item_list(request):
    items = Item.objects.all()

    category = request.GET.get('kategorija')
    name = request.GET.get('pavadinimas')

    if category:
        items = items.filter(category__name__icontains=category)
    if name:
        items = items.filter(name__icontains=name)

    paginator = Paginator(items, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'katalogas/item_list.html', {
        'page_obj': page_obj,
        'kategorija': category or '',
        'pavadinimas': name or '',
    })

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

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'katalogas/item_form.html'
    success_url = reverse_lazy('item_list')