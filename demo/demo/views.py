import json

from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.timezone import now
from rest_framework import serializers

from demoapp.models import Event, Calendar
from djgentelella.forms.forms import CustomForm
from djgentelella.widgets import core as genwidgets
from djgentelella.widgets import numberknobinput as knobwidget
from djgentelella.widgets.calendar import CalendarInput
from djgentelella.widgets.files import FileChunkedUpload
from djgentelella.widgets.timeline import UrlTimeLineInput
from djgentelella.widgets.storymap import GigaPixelStoryMapInput, MapBasedStoryMapInput


class ExampleForm(CustomForm):
    gigapixel_storymap_options = {
        "map_type": "zoomify",
        "map_background_color": "#333",
        "map_as_image": True,
        "calculate_zoom": False,
        "zoomify": {
            "path": "http://cdn.verite.co/maps/zoomify/seurat/",
            "width": 30000,
            "height": 19970,
            "tolerance": 0.9,
            "attribution": "<a href='http://www.google.com/culturalinstitute/asset-viewer/a-sunday-on-la-grande-jatte-1884/twGyqq52R-lYpA?projectId=art-project' target='_blank'>Google Art Project</a>"
        }
    }
    gigapixel_storymap = forms.CharField(widget=GigaPixelStoryMapInput(
        attrs={"data-url": reverse_lazy('examplestorymapgp-list'), "storymap_options": gigapixel_storymap_options}))

    timeline = forms.CharField(widget=UrlTimeLineInput(
        attrs={"data-url": reverse_lazy('exampletimeline-list'), 'style': "height: 500px;",
               "data-option_language": 'es'}))

    mapbased_storymap = forms.CharField(widget=MapBasedStoryMapInput(
        attrs={"data-url": reverse_lazy('examplestorymapmb-list')}))

    your_name = forms.CharField(label='Your name', max_length=100, widget=genwidgets.TextInput)
    your_age = forms.IntegerField(widget=genwidgets.NumberInput(attrs={'min_value': 2, 'max_value': 8}))
    your_email = forms.EmailField(widget=genwidgets.EmailInput)
    your_email_mask = forms.EmailField(widget=genwidgets.EmailMaskInput)
    your_url = forms.URLField(widget=genwidgets.URLInput)
    your_pass = forms.CharField(widget=genwidgets.PasswordInput)

    your_file = forms.FileField(widget=genwidgets.FileInput)
    your_trunk = forms.FileField(widget=FileChunkedUpload)
    your_area = forms.CharField(widget=genwidgets.Textarea, max_length=50)
    your_date = forms.DateField(widget=genwidgets.DateInput)
    your_datetime = forms.DateTimeField(widget=genwidgets.DateTimeInput)
    your_daterange = forms.CharField(widget=genwidgets.DateRangeInput)
    #
    #
    your_time = forms.TimeField(widget=genwidgets.TimeInput(attrs={'arrow': True}))
    your_check = forms.BooleanField(widget=genwidgets.CheckboxInput)
    #
    #
    #  your_nullboolean = forms.NullBooleanField(widget=genwidgets.NullBooleanSelect)
    #
    #  your_choice = forms.ChoiceField(choices=(
    #      ('enero', 'Enero'),
    #      ('febrero', 'Febrero'),
    #      ('marzo', 'abril')
    #  ), widget=genwidgets.Select)
    #
    #  your_test = forms.ChoiceField(choices=(
    #      ('enero', 'Enero'),
    #      ('febrero', 'Febrero'),
    #      ('marzo,abril', 'Marzo,Abril')
    #  ), widget=genwidgets.Select)
    #
    #  your_multiple = forms.ChoiceField(choices=(
    #      ('enero', 'Enero'),
    #      ('febrero', 'Febrero'),
    #      ('marzo,abril', 'Marzo,Abril')
    #  ), widget=genwidgets.SelectMultiple)
    #

    your_radio = forms.ChoiceField(choices=(
        ('enero', 'Enero'),
        ('febrero', 'Febrero'),
        ('marzo,abril', 'Marzo,Abril')
    ), widget=genwidgets.RadioHorizontalSelect)
    your_radio_vertical = forms.ChoiceField(choices=(
        ('enero', 'Enero'), ('febrero', 'Febrero'),
        ('marzo', 'Marzo'), ('abril', 'Abril')
    ), widget=genwidgets.RadioVerticalSelect)
    #
    #  your_checkbox = forms.ChoiceField(choices=(
    #      ('enero', 'Enero'),
    #      ('febrero', 'Febrero'),
    #      ('marzo,abril', 'Marzo,Abril')
    #  ), widget=genwidgets.CheckboxSelectMultiple)
    #
    #  #your_date = forms.DateField(widget=DateInput)
    #  #your_hiddendatime=forms.DateTimeField(widget=SplitHiddenDateTimeWidget)
    #  #your_SplitDateTimeWidget = forms.DateTimeField(widget=SplitDateTimeWidget)
    #
    #  your_selectdate = forms.DateTimeField(widget=genwidgets.SelectDateWidget)
    #
    #  def __init__(self, *args, **kwargs):
    #      kwargs['initial'] = {'your_name': "BINGO", 'your_age': 4,
    #                           'your_SplitDateTimeWidget': now(),
    #                           'your_selectdate': now(),
    #                           'your_time': now(), 'your_nullboolean': True}
    #
    #      super().__init__(*args, **kwargs)

    your_phone = forms.CharField(widget=genwidgets.PhoneNumberMaskInput)
    your_boolean = forms.BooleanField(
        widget=genwidgets.YesNoInput(attrs={'rel': ['#id_your_radio_vertical', 'your_datemask', 'you_emailmask']}))
    your_datemask = forms.DateField(widget=genwidgets.DateMaskInput)
    your_datetimeMask = forms.DateTimeField(widget=genwidgets.DateTimeMaskInput)
    you_emailmask = forms.EmailField(widget=genwidgets.EmailMaskInput)
    # your_daterangeinput = forms.CharField(widget=genwidgets.DateRangeInput)
    # your_knobinput = forms.IntegerField(widget=genwidgets.NumberKnobInput(
    #    attrs={ 'max_value':300, 'min_value': 200,
    #            'data-width': 100, 'data-height': 100,
    #            'data-displayPrevious': "true",
    #            'data-fgColor': "#26B99A",
    #            'data-cursor': "true",
    #            'data-thickness': '.3'
    #            } ))
    #
    # your_test = forms.ChoiceField(choices=(
    #     ('enero', 'Enero'),
    #     ('febrero', 'Febrero'),
    #     ('marzo,abril', 'Marzo,Abril')
    # ), widget=genwidgets.SelectMultipleAdd(
    #     attrs={'add_url': reverse_lazy('add_view_select')}
    # ))
    #
    # your_multiple = forms.ChoiceField(choices=(), widget=genwidgets.SelectWithAdd(
    #     attrs={'add_url': reverse_lazy('add_view_select')}))

    # your_wysiwyg = forms.CharField(widget=genwidgets.TextareaWysiwyg)

    # text_6 = forms.CharField(
    #     widget=ColorInput
    # )
    # text_7 = forms.CharField(
    #     widget=ColorInput
    # )

    your_age = forms.IntegerField(
        widget=knobwidget.NumberKnobInput(attrs={"value": 5, "data-min": 1, "data-max": 10}))

    calendar = forms.CharField(
        required=False,
        widget=CalendarInput(
            calendar_attrs={'initialView': 'timeGridWeek'},
            events=Event.objects.all().values('title', 'start', 'end')
        )
    )


def home(request):
    form = ExampleForm()
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        form.is_valid()
        #print(form.cleaned_data)
    return render(request, 'gentelella/index.html', {'form': form})


@login_required
def logeado(request):
    return HttpResponse("Wiii")


def add_view_select(request):
    if request.method == 'POST':
        return JsonResponse({'ok': True, 'id': 2, 'text': 'Data example'})
        return JsonResponse({'ok': False,
                             'title': "Esto no dice nada",
                             'message': 'Esto es un errror'})
    data = {
        'ok': True,
        'title': 'Formulario de ejemplo',
        'message': """
        <form method="post" action="/add_view_select">
            <textarea name="description" > </textarea>
            <input type="text" name="name" />
            <select name="bingo">
               <option value="Nada">Nada</option><option value="otro">Otro</option>
            </select>
        </form>
        """
    }
    return JsonResponse(data)
