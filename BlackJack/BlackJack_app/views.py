from django.shortcuts import render
from .models import shuffle, Participants, count_cards_value


def home(request):
    player = Participants.objects.get(pk=2)
    player.money = 100
    player.save()
    return render(request, 'home.html')


def place_bet(request):
    player = Participants.objects.get(pk=2)
    return render(request, 'place_bet.html', {'player': player})


def game(request):
    player_bet = int(request.POST["player_bet"])

    sh_deck = shuffle()
    request.session['sh_deck'] = sh_deck

    participant = Participants.objects.all()
    for part in participant:
        if part.name != 'Croupier':
            part.name = 'Robert'
        part.participant_hand = []
        part.hand_value = 0
        part.stand = False
        part.participant_hand.append(sh_deck[0])
        del sh_deck[0]
        part.participant_hand.append(sh_deck[1])
        del sh_deck[1]
        if part.name == 'Croupier':
            part.hand_value = count_cards_value(part.participant_hand[:-1], part.hand_value)
        else:
            part.hand_value = count_cards_value(part.participant_hand, part.hand_value)
        if part.name == 'Robert':
            part.bet = player_bet
        part.save()

    croupier = Participants.objects.get(pk=1)
    player = Participants.objects.get(pk=2)

    return render(request, 'game.html', {'total': participant, 'player': player,
                  'croupier': croupier})


def player_hit(request):

    player = Participants.objects.get(pk=2)
    sh_deck = request.session.get('sh_deck')
    player.participant_hand.append(sh_deck[0])
    del sh_deck[0]
    player.hand_value = count_cards_value(player.participant_hand[-1:], player.hand_value)

    player.save()
    request.session['sh_deck'] = sh_deck
    participant = Participants.objects.all()

    croupier = Participants.objects.get(pk=1)
    return render(request, 'game.html', {'total': participant, 'player': player,
                  'croupier': croupier})


def stand(request):

    croupier = Participants.objects.get(pk=1)
    sh_deck = request.session.get('sh_deck')
    croupier.hand_value = count_cards_value(croupier.participant_hand[-1:], croupier.hand_value)
    while croupier.hand_value <= 16:
        croupier.participant_hand.append(sh_deck[0])
        del sh_deck[0]
        croupier.hand_value = count_cards_value(croupier.participant_hand[-1:], croupier.hand_value)

    croupier.stand = True
    croupier.save()
    request.session['sh_deck'] = sh_deck
    participant = Participants.objects.all()

    player = Participants.objects.get(pk=2)
    return render(request, 'game.html', {'total': participant, 'player': player,
                  'croupier': croupier})


def lost_round(request):
    player = Participants.objects.get(pk=2)
    player.money -= player.bet
    player.save()
    return render(request, 'place_bet.html', {'player': player})


def won_round(request):
    player = Participants.objects.get(pk=2)
    player.money += player.bet
    player.save()
    return render(request, 'place_bet.html', {'player': player})


def blackjack(request):
    player = Participants.objects.get(pk=2)
    player.money = player.money + 1.5*player.bet
    player.save()
    return render(request, 'place_bet.html', {'player': player})


def end_game(request):
    return render(request, 'home.html')
