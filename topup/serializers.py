from rest_framework import serializers
from .models import TopUpOrder, Game, TopUpProduct

class TopUpOrderSerializer(serializers.ModelSerializer):
  gamename = serializers.CharField(write_only=True)
  game_id = serializers.CharField(write_only=True)
  product_name = serializers.CharField(write_only=True)
  product_id = serializers.IntegerField()
  product_price = serializers.DecimalField(max_digits=10, decimal_places=2)
  
  class Meta:
    model = TopUpOrder
    fields = ['user_email', 'status', 'gamename', 'game_id', 'product_name', 'product_id', 'product_price']

  def validate(self, data):
    try:
      game = Game.objects.get(name=data['gamename'], game_id=data['game_id'], is_active=True)
    except Game.DoesNotExist:
      raise serializers.ValidationError("Game not found or inactive.")

    try:
      product = TopUpProduct.objects.get(
        id=data['product_id'], name=data['product_name'], price=data['product_price'], game=game
      )
    except TopUpProduct.DoesNotExist:
      raise serializers.ValidationError("Product not found for this game or price mismatch.")

    data['product'] = product  # include for save()
    return data

  def create(self, validated_data):
    validated_data.pop('gamename')
    validated_data.pop('game_id')
    validated_data.pop('product_name')
    validated_data.pop('product_id')
    validated_data.pop('product_price')
    return TopUpOrder.objects.create(**validated_data)
