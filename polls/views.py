from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse # 응답
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html") # polls에 있는 index.html 파일을 불러들인 것
    context = {
        "latest_question_list": latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question" : question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

#def index(request):
    #print('클라이언트의 요청을 받음')
   # input('요청을 처리하는 상태(완료하려면 엔터)')
    #return HttpResponse("Hello, world. You're at the polls index.") # 처리 된 객체를 response 객체로 만들어줌
    #응답 할 내용이 body에 들어감