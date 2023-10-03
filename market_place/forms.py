from django import forms


class AvailabilityFilterForm(forms.Form):
    action = forms.ChoiceField(
        label="Action",
        choices=[('filter_boxes_by_availability', 'Filter by Availability')],
        widget=forms.Select(attrs={'class': 'action-select'})
    )

    # Add the "select_across" field
    select_across = forms.BooleanField(
        required=False,
        initial=0,  # Set initial value as needed
        widget=forms.HiddenInput,
    )

    start_date = forms.DateField(label="Start Date", widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label="End Date", widget=forms.DateInput(attrs={'type': 'date'}))
