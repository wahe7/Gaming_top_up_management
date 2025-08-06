from django.contrib import admin
from .models import Game, TopUpProduct

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
  list_display = ('name', 'game_id', 'is_active')
  search_fields = ('name', 'game_id')
  
@admin.register(TopUpProduct)
class TopUpProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'price', 'in_game_currency', 'game']
  search_fields = ['name', 'game__name']


