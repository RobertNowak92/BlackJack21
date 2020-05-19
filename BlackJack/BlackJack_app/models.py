from django.db import models
from django.db.models import CharField
from django_mysql.models import ListCharField
import random


class Participants(models.Model):
    name = models.CharField(max_length=100)
    money = models.IntegerField(default=100)
    hand_value = models.IntegerField(default=0)
    stand = models.BooleanField(default=False)
    bet = models.IntegerField(default=0)
    participant_hand = ListCharField(
        base_field=CharField(max_length=10),
        size=6,
        max_length=(6 * 11)
    )


def shuffle():
    deck = ['2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Wh', 'Dh', 'Kh', 'Aceh',
            '2t', '3t', '4t', '5t', '6t', '7t', '8t', '9t', '10t', 'Wt', 'Dt', 'Kt', 'Acet',
            '2b', '3b', '4b', '5b', '6b', '7b', '8b', '9b', '10b', 'Wb', 'Db', 'Kb', 'Aceb',
            '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Wd', 'Dd', 'Kd', 'Aced']

    random.shuffle(deck)
    return deck


def count_cards_value(temp_participant_hand, temp_hand_value):
    for i in range(len(temp_participant_hand)):
        if ('10' in temp_participant_hand[i] or
                'W' in temp_participant_hand[i] or
                'D' in temp_participant_hand[i] or
                'K' in temp_participant_hand[i]):
            temp_hand_value += 10
        elif 'Ace' not in temp_participant_hand[i]:
            temp_hand_value += int(temp_participant_hand[i][0])
        else:
            if temp_hand_value <= 10:
                temp_hand_value += 11
            else:
                temp_hand_value += 1
    return temp_hand_value

