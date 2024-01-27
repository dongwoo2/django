from django.shortcuts import get_object_or_404, render
#from django.http import Http404

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect # 응답
#from django.template import loader
from django.urls import reverse
from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html") # polls에 있는 index.html 파일을 불러들인 것
    context = {
        "latest_question_list": latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)

 #def detail(request, question_id):
 #  try:
 #       question = Question.objects.get(pk=question_id)
 #   except Question.DoesNotExist:
 #      raise Http404("Question does not exist")
 #   return render(request, "polls/detail.html", {"question" : question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question":question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

#def index(request):
    #print('클라이언트의 요청을 받음')
   # input('요청을 처리하는 상태(완료하려면 엔터)')
    #return HttpResponse("Hello, world. You're at the polls index.") # 처리 된 객체를 response 객체로 만들어줌
    #응답 할 내용이 body에 들어감