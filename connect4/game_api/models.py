from django.db import models

class Game(models.Model):
    game_id = models.UUIDField(primary_key=True, editable=False)
    game_over = models.BooleanField(default=False)
    player = models.IntegerField(blank=False, default=1)
    board = models.BinaryField(blank=False)

    class Meta:
        managed = True

    def __str__(self):
        return str(self.game_id)


class Move(models.Model):
    game_id = models.ForeignKey(Game, related_name='moves', on_delete=models.CASCADE)
    player = models.IntegerField(blank=False)
    column = models.IntegerField(blank=False)

    class Meta:
        managed = True
