# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django.shortcuts import render
from django.conf import settings


def index(request):
	return render(request, 'index.html',locals())

def Login(request):
	if request.method == 'POST':
		print(request.POST)
	else:
		print ("this request is get")
	return render(request,'basicInfo.html',locals())

def NumberMan(request):
    user_name = "nemo"
    return render(request, 'NumberMan.html', locals())


def basicInfo(request):
    return render(request, 'basicInfo.html', locals())


def customer(request):
    return render(request, 'customer.html', locals())


def records(request):
    return render(request, 'records.html', locals())

def bill(request):
    return render(request, 'bill.html', locals())


def reset(request):
    return render(request, 'reset.html', locals())

def consump(request):
	return render(request, 'consump.html', locals())