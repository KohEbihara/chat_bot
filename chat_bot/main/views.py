from django.shortcuts import render
from datetime import datetime


def index(request):
    return render(request, "main/index.html")


from django.shortcuts import  redirect, render  
from .forms import  TalkForm  
from .models import Talk , Q_A

def talk_room(request):

    talks = Talk.objects.all()
    
    if request.method == "GET":
        form = TalkForm()

        
    elif request.method == "POST":
        form = TalkForm(request.POST)
        if form.is_valid():
            
            
            new_talk = form.save(commit=False)
            new_talk.save()
            answer_texts = Q_A.objects.filter(
                question_text__icontains = new_talk.message
            )
            for answer in answer_texts:
                Talk.objects.create(
                    message = answer.answer_text,
                    send_bot = True,
                    time = datetime.now()
                )
            talks = Talk.objects.all()
            return redirect("talk_room")


    context = {
        "form": form,
        "talks": talks,
    }
    return render(request, "main/index.html", context)