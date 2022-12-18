from django.shortcuts import render
from django.http import HttpResponseRedirect
from web.models import Console, Domain, Game, Cheat
from web.forms import GameForm, CheatForm


def index(request):
    console_num = Console.objects.all().count()
    domain_num = Domain.objects.all().count()
    game_num = Game.objects.all().count()
    cheat_num = Cheat.objects.all().count()
    context = {
        "console_num": console_num,
        "domain_num": domain_num,
        "game_num": game_num,
        "cheat_num": cheat_num,
    }
    return render(request, "index.html", context)


def console_list(request):
    console_objs = Console.objects.all()
    context = {
        "consoles": console_objs,
    }
    return render(request, "console_list.html", context)


def domain_info(request, pk):
    console_obj = Console.objects.get(pk=pk)
    domain_objs = Domain.objects.filter(console_id=console_obj.id)
    context = {
        "domains": domain_objs,
        "consoles": console_obj,
    }
    return render(request, "domain_info.html", context)

def push_data(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GameForm(request.POST)
        form.save()
        form = GameForm()
    else:
        form = GameForm()
    return render(request, 'push_data.html', {'form': form})

def push_data_2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CheatForm(request.POST)
        form.flag_data = {}
        form.save()
        form = CheatForm()
    else:
        form = CheatForm()
    return render(request, 'push_data_2.html', {'form': form})