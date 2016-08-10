# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from schoolApp.models import *


def home(request):

    return render_to_response('index.html')

