from django.shortcuts import render, redirect
from .models import Search
from .forms import SearchForm
import folium
import geocoder
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

from .models import Search
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import requests
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as poi

import numpy as np




def map(request):
    if request.method =='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map.html')
    else:
        form =SearchForm()
    address = Search.objects.all().last()
    #address = request.POST.get('address')
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country

    #Create Map Object
    m = folium.Map(location=[51.312711, 9.479746], zoom_start=6)
    folium.Marker([50.922423, 6.363912], tooltip='Click for more', popup='Jülich').add_to(m)


    folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
    #Get HTML Representation of Ma Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form':form,
    }
    return render(request,'map.html', context )

