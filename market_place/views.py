# Create your views here.
from django.shortcuts import render
from .models import StorageBox
from django.views.generic import ListView, CreateView


def storage_boxes_filter(request):
    """
    function to filter and sort area and street_number
    """
    # Retrieve all available storage boxes
    storage_boxes = StorageBox.objects.all()

    # Handle filtering and sorting based on user input
    filter_by = request.GET.get('filter_by')
    sort_by = request.GET.get('sort_by')

    if filter_by == 'street_number_lowest':
        # Filter by lowest Street_number
        storage_boxes = storage_boxes.order_by('street_number')
    elif filter_by == 'street_number_highest':
        # Filter by highest Street_number
        storage_boxes = storage_boxes.order_by('-street_number')
    elif filter_by == 'surface_area_smallest':
        # Filter by smallest surface
        storage_boxes = storage_boxes.order_by('surface')
    elif filter_by == 'surface_area_largest':
        # Filter by largest surface
        storage_boxes = storage_boxes.order_by('-surface')

    if sort_by == 'price_lowest':
        # Sort by lowest Street_number
        storage_boxes = storage_boxes.order_by('street_number')
    elif sort_by == 'price_highest':
        # Sort by highest Street_number
        storage_boxes = storage_boxes.order_by('-street_number')
    elif sort_by == 'surface_smallest':
        # Sort by smallest surface area
        storage_boxes = storage_boxes.order_by('surface')
    elif sort_by == 'surface_largest':
        # Sort by largest surface area
        storage_boxes = storage_boxes.order_by('-surface')

    context = {
        'storage_boxes': storage_boxes,
    }
    return render(request, 'storage_boxes_filter.html', context)


class StorageBoxListView(ListView):
    """
    Class to print all boxes
    """
    model = StorageBox
    template_name = 'storage_box_list.html'
    context_object_name = 'storage_boxes'
    queryset = StorageBox.objects.all()

    """
    def get_queryset(self):
        return StorageBox.objects.filter(surface=16)
    """


class StorageBoxCreateView(CreateView):
    """
    Class to create storesboxes
    """
    model = StorageBox
    template_name = 'storage_box_form.html'
    fields = '__all__'