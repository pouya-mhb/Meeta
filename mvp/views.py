from django.shortcuts import render
from django.http import HttpResponse
from mvp.models import Meeting
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def meetings(request):

    if request.method == 'POST':
        pass
    else:
        meetings = Meeting.objects.all()
        users = User.objects.all()
        context = {
            users: users,
            meetings: meetings
        }

        return render(
            request, 'meetings.html', context
        )
