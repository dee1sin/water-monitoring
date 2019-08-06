from django.shortcuts import render
from django.views.generic.base import TemplateView


class DashboardView(TemplateView):
    def get(self,request,**kwargs):
        return render(request,'dashboard/board.html')

class WaterStateView(TemplateView):
    def get(self,request,**kwargs):
        return render(request,'dashboard/waterstate.html')