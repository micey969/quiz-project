from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import QuizModel
from .forms import *

# Create your views here.
def index(request):
    if request.method == "POST":
        questions = QuizModel.objects.all()
        score = 0
        correct = 0
        incorrect = 0
        total = 0
        for q in questions:
            total+=1
            if q.answer == request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                incorrect+=1
        context={
            'score': score,
            'correct': correct,
            'incorrect': incorrect,
            'total': total,
        }
        return render(request,'results.html',context)

    else:
        questions = QuizModel.objects.all()
        context = {'questions': questions}
        return render(request,'index.html',context)


@staff_member_required
def addQuestion(request):
    form = addQuestionForm()
    if request.method == 'POST':
        form = addQuestionForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect ('addQuestion')

    context = {'form':form}
    return render(request, 'questions.html',context)