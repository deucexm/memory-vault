from django.shortcuts import render
from web.models import Console, Domain, Game, Cheat


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
