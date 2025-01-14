from DiceGame import DiceGame

# execution
game = DiceGame()
while game.get_is_playing():
  game.play_game()
  if not game.get_is_playing():
    print('Game is over.')
    break

  game.set_many_dices()
  game.set_dice_highest_number()
  for i in range(int(game.get_many_dices())):
    game.roll_dice()
