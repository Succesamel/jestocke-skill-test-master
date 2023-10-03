# Register your models here.
from django.contrib import admin
from market_place.models import StorageBox
from market_place.forms import AvailabilityFilterForm


def set_storage_to_unavailable():
    """
    function to set attribute is_available to false
    """
    for box in StorageBox.objects.all():

        box.is_available = False
        box.save()


def filter_boxes_by_availability(self, request, queryset):
    """
    function to filter storageboxes by availibility
    """
    # pass all data to not available
    set_storage_to_unavailable()

    form = AvailabilityFilterForm(request.POST)
    # verify if form is valid
    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')

        if start_date and end_date:
            # Filter the queryset whit range date
            filtered_storage_boxes = queryset.exclude(
                booking__start_date__lte=end_date,
                booking__end_date__gte=start_date
            )
            #Set attribute result of query
            for box in filtered_storage_boxes:
                box.is_available = True
                box.save()

            self.message_user(request, f"Filtered {filtered_storage_boxes.count()} storages boxes by availability.")
    else:
        # Handle form validation errors if any
        self.message_user(request, "Form is not valid")


@admin.register(StorageBox)
class StorageBoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_available', 'title', 'storage_type', 'surface', 'monthly_price', 'owner')
    list_filter = ['storage_type', ('owner', admin.RelatedOnlyFieldListFilter)]
    list_editable = ('is_available',)
    search_fields = ('title', 'description', 'owner__first_name', 'owner__last_name', 'owner__email')
    ordering = ('-id',)  # Show latest boxes at the top of the list
    actions = [filter_boxes_by_availability]
    action_form = AvailabilityFilterForm
    filter_boxes_by_availability.short_description = "Filter by Availability"

    def changelist_view(self, request, extra_context=None):
        # Add a custom filter form to the change list view
        self.list_filter = ('surface', 'storage_type',
            ('booking__start_date', admin.DateFieldListFilter),
        )
        return super().changelist_view(request, extra_context=extra_context)

