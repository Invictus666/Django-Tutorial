from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic

# Create your views here.

def main_output(request):
        num_visits = request.session.get('num_visits', 0) + 1
        request.session['num_visits'] = num_visits
        if num_visits > 4 : del(request.session['num_visits'])
        resp = HttpResponse('view count='+str(num_visits))
        resp.set_cookie('dj4e_cookie', '07bba581', max_age=1000)
        return resp
