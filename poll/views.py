from django.shortcuts import get_object_or_404, redirect, render
from .models import Question, Choice
import json

def home(request):
    questions = Question.objects.all()
    return render(request, 'poll/home.html', {
        "questions": questions
    })

def vote(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    if request.method == "POST":
        try:
            choice_id = request.POST.get('choice')
            choice = q.choice_set.get(pk=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('poll:result', q_id)
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'poll/vote.html', {
                "question": q,
                "error_message": "Debes de elegir algo!! XDXDXDXDXD"
            })
    return render(request, 'poll/vote.html', {
        "question": q
    })

def result(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    choices = q.choice_set.all()
    choice_texts = json.dumps([choice.choice_text for choice in choices])
    votes = json.dumps([choice.votes for choice in choices])

    print(choice_texts, votes)  

    return render(request, 'poll/result.html', {
        "question": q,
        "choice_texts": choice_texts,
        "votes": votes
    })