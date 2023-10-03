# Register your models here.
from django.contrib import admin, messages
from booking.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    actions = ("latest_created", "lowercase")  # Necessary
    list_display = ('id', 'created_on', 'get_tenant', 'storage_box', 'start_date', 'end_date' )
    list_filter = ()
    search_fields = ('storage_box__title', 'storage_box__description', 'tenant__first_name')
    ordering = ('-created_on',)  # show the lastest boxes

    # date_hierarchy = 'created_at'
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # You might need some logic to filter the boxes based on their availability
        # by checking against the `Booking` model for bookings that overlap with the desired date range.
        # This is a simple version:
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            qs = qs.exclude(start_date__lte=date_to, end_date__gte=date_from)
            print(qs)
        return qs

    @admin.display(ordering='booking__tenant', description='Tenant')
    def get_tenant(self, obj):
        return obj.tenant.first_name
