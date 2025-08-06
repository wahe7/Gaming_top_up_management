from django.db import models

class Game(models.Model):
  name = models.CharField(max_length=100)
  game_id = models.CharField(max_length=50)
  is_active = models.BooleanField(default=True)
  
  def __str__(self):
    return self.name
  
class TopUpProduct(models.Model):
  game = models.ForeignKey(Game, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  in_game_currency = models.CharField(max_length=100)
  
  def __str__(self):
    return f"{self.name} ({self.game.name})"     
    
    