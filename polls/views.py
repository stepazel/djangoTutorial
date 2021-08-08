from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404

from polls.models import Question


def index(request) -> HttpResponse:
    latestQuestionList = Question.objects.order_by('-publishedDate')[:5]
    context = {
        'latestQuestionList': latestQuestionList
    }
    return render(request, 'polls/index.html', context)


def detail(request: HttpRequest, questionId: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=questionId)
    return render(request, 'polls/detail.html', {'question': question})


def results(request: HttpRequest, questionId: int) -> HttpResponse:
    return HttpResponse("You're looking at the results of question %s." % questionId)


def vote(request: HttpRequest, questionId: int) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % questionId)
