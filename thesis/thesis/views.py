from django.shortcuts import render, redirect
from django.http import HttpResponse

import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd

from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

def index(request):
    x_data = [0,1,2,3,4,5,6,7,8]
    y_data = [x*2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data, mode='Carpet', name='test', opacity=0.5, marker_color='green')],output_type='div')
    return render(request, 'test_plotly.html', context={'plot_div': plot_div})




# Create your views here.
def index(request):
      #HttpResponse "Hello World"
      return render(request, 'index.html')
      #return HttpResponse("<h1> The Record exists in the database! " )

def page2(request):

    return render(request,'page2.html' )

def sfh2(request):

    return render(request,'sfh2.html' )
def mfh2(request):

    return render(request,'mfh2.html' )
def commercial(request):

    return render(request,'commercial.html' )
def page1(request):

    return render(request,'page1.html' )

def page21(request):

    return render(request,'page21.html' )
def tos(request):

    return render(request,'tos.html' )
def photo(request):

    return render(request,'photo.html' )

def pump(request):

    return render(request,'pump.html' )
def battery(request):

    return render(request,'battery.html' )
def comb(request):

    return render(request,'comb.html' )
def gas(request):

    return render(request,'gas.html' )
def electric(request):

    return render(request,'electric.html' )
def hydro(request):

    return render(request,'hydro.html' )

def test(request):

    return render(request,'test_plotly.html' )




def page3(request):
    return render(request, 'page3.html')



