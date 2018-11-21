from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html',{'question':Question.objects.order_by('-pub_date')})

def exibir(request,question_id):
    question=Question.objects.get(id=question_id)
    return render(request,'question.html',{'question':question})

def results(request,question_id):
    question=Question.objects.get(id=question_id)
    return render(request,'results.html',{'question':question})

def vote(request,question_id):
    question=Question.objects.get(id=question_id)
    question.question.add_vote()
    return redirect('index')

def exibir_questao_fechada(request):
    return render(request,'question_closed.html',{'question':Question.objects.order_by('-pub_date')})
    pass

def manage(request,question_id):
    return render(request,'manage.html')
    pass