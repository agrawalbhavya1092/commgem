from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = DepartmentSetup
        fields=()
    content = forms.CharField(widget=CKEditorUploadingWidget())

class MailingListForm(forms.Form):
    # class Meta:
        # model = Person
        # fields = ('name', 'birthdate', 'country', 'city')

    entity = forms.ModelChoiceField(queryset=DepartmentSetup.objects.all().values('source').distinct())
    p1_department = forms.ModelMultipleChoiceField(queryset=DepartmentSetup.objects.all().values('m1_department_id','m1_department_name').distinct())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['p1_department'].queryset = DepartmentSetup.objects.none()

        if 'source' in self.data:
            try:
                source = int(self.data.get('source'))
                self.fields['m1_department_id'].queryset = DepartmentSetup.objects.filter(source=source).order_by()
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
            # self.fields['m1_department_id'].queryset = self.order_by('name')
            # self.fields['p1_department_id'].queryset = self.instance.country.city_set.order_by('name')

class LocationSetup1Form(forms.ModelForm):
    class Meta:
        model = LocationSetup1
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = Region.objects.none()

        if 'country' in self.data:
            print("data..............",self.data)
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')


