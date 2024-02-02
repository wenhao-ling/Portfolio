import pygame
from pygame.locals import QUIT
import time
import random

pygame.init()

logo = pygame.image.load("card back black.png")
pygame.display.set_icon(logo)
pygame.display.set_caption('Blackjack')
text_font = pygame.font.SysFont("Arial", 20) 

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DECK_WIDTH = 150
DECK_HEIGHT = 220
DECK_X = 300
DECK_Y = 130
HIT_WIDTH = 150
HIT_HEIGHT = 80
HIT_X = 100
HIT_Y = 450
SKIP_WIDTH = 150
SKIP_HEIGHT = 80
SKIP_X = 750
SKIP_Y = 450

cards = { # change the file path to your computer's download path for each file 
  1 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\2_of_clubs.png",   # r before the string in order to make the string raw (so the \ does not interfere with the image path)
  2 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\2_of_diamonds.png",
  3 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\2_of_hearts.png", 
  4 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\2_of_spades.png", 
  5 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\3_of_clubs.png",
  6 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\3_of_diamonds.png",
  7 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\3_of_hearts.png", 
  8 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\3_of_spades.png", 
  9 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\4_of_clubs.png",
  10 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\4_of_diamonds.png",
  11 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\4_of_hearts.png", 
  12 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\4_of_spades.png", 
  13 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\5_of_clubs.png",
  14 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\5_of_diamonds.png",
  15 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\5_of_hearts.png", 
  16 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\5_of_spades.png", 
  17 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\6_of_clubs.png",
  18 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\6_of_diamonds.png",
  19 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\6_of_hearts.png", 
  20 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\6_of_spades.png", 
  21 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\7_of_clubs.png",
  22 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\7_of_diamonds.png",
  23 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\7_of_hearts.png", 
  24 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\7_of_spades.png", 
  25 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\8_of_clubs.png",
  26 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\8_of_diamonds.png",
  27 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\8_of_hearts.png", 
  28 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\8_of_spades.png", 
  29 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\9_of_clubs.png",
  30 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\9_of_diamonds.png",
  31 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\9_of_hearts.png", 
  32 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\9_of_spades.png", 
  33 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\10_of_clubs.png",
  34 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\10_of_diamonds.png",
  35 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\10_of_hearts.png", 
  36 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\10_of_spades.png", 
  37 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\ace_of_clubs.png", 
  38 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\ace_of_diamonds.png",
  39 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\ace_of_hearts.png", 
  40 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\ace_of_spades.png",
  41 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\jack_of_clubs2.png",
  42 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\jack_of_diamonds2.png",
  43 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\jack_of_hearts2.png",
  44 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\jack_of_spades2.png",
  45 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\king_of_clubs2.png", 
  46 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\king_of_diamonds2.png",
  47 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\king_of_hearts2.png", 
  48 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\king_of_spades2.png",
  49 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\queen_of_clubs2.png",
  50 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\queen_of_diamonds2.png",
  51 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\queen_of_hearts2.png",
  52 : r"C:\Users\lingw\OneDrive\Documents\Visual Studio Code\Python VS\PNG-cards-1.3\queen_of_spades2.png",
}
index = len(cards[1]) - 14

cardlist = []
for i in range(len(cards)): 
  cardlist.append(i+1)

deck = pygame.image.load("card back black.png")
horizontaldeck = pygame.transform.rotate(deck, 90)
deck_rect = pygame.Rect(DECK_X, DECK_Y, DECK_WIDTH, DECK_HEIGHT)
hit_rect = pygame.Rect(HIT_X, HIT_Y, HIT_WIDTH, HIT_HEIGHT)
skip_rect = pygame.Rect(SKIP_X, SKIP_Y, SKIP_WIDTH, SKIP_HEIGHT)
colour_deck_rect = (255,255,255)

bot1 = 0
bot2 = 0
player = 0
bot1num = 0 # num of cards
bot2num = 0
playernum = 0
bot1ace = 0
bot2ace = 0
playerace = 0
bot1died = False
playerdied = False
bot2died = False
bot1hit = False
bot2hit = False
playercardlist = []
bot1skip = False
bot2skip = False
playerskip = False
bot1win = False

running = True
started = True
playerturn = False
lost = False
tied = False
won = False

def redrawScreen(): 
  screen.fill((255,255,255))
  
  pygame.draw.rect(screen,colour_deck_rect,deck_rect) # draw hitbox under door image
  screen.blit(pygame.transform.scale(deck,(DECK_WIDTH, DECK_HEIGHT)), (DECK_X,DECK_Y)) # draw door image

  pygame.draw.rect(screen,(64,137,255),hit_rect) # draw hitbox and rectangle of hit and subsequently skip buttons
  pygame.draw.rect(screen,(64,137,255),skip_rect)
  drawText("HIT", text_font, (0,0,0), 150, 480) # draw text for buttons
  drawText("SKIP", text_font, (0,0,0), 800, 480)

  if not bot1died: 
    y = 50
    for i in range(bot1num): 
      screen.blit(pygame.transform.scale(horizontaldeck,(DECK_HEIGHT,DECK_WIDTH)), (-100,y + i*50)) # draw bot1 cards (rotated)
  
  x = 350
  count = 0
  for i in playercardlist: 
    card = pygame.image.load(i)
    screen.blit(pygame.transform.scale(card,(DECK_WIDTH,DECK_HEIGHT)), (x + count*100,500)) # draw player cards
    count += 1

  if not bot2died: 
    y = 50
    for i in range(bot2num): 
      screen.blit(pygame.transform.scale(horizontaldeck,(DECK_HEIGHT,DECK_WIDTH)), (880,y + i*50)) # draw bot2 cards 
  
  pygame.display.update()

def drawText(text, font, colour, x, y): 
  img = font.render(text, True, colour)
  screen.blit(img, (x,y))

def gameover(): 
  screen.fill((255,255,255))
  drawText("GAME OVER U LOST", text_font, (0,0,0), 100, 100)
  drawText("press r to restart", text_font, (0,0,0), 100, 200)

def clickingHit(): 
  if pygame.mouse.get_pressed()[0] and hit_rect.collidepoint(pygame.mouse.get_pos()):
      return True
  
def clickingSkip(): 
  if pygame.mouse.get_pressed()[0] and skip_rect.collidepoint(pygame.mouse.get_pos()):
      return True

while running: 
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
  
  if not playerturn and not lost and not won and not tied:
    bot1card = random.randint(1,52)
    bot2card = random.randint(1,52)
    playercard = random.randint(1,52)

  if started: 
    print("Started")
    bot1num += 1
    bot1card = random.randint(1,52) 
    cardlist.remove(bot1card) # remove taken card from list
    playernum += 1
    while playercard not in cardlist: 
      playercard = random.randint(1,52) # get a card not previously taken
    cardlist.remove(playercard)
    bot2num += 1
    while bot2card not in cardlist: 
      bot2card = random.randint(1,52)
    cardlist.remove(bot2card)

    if cards[bot1card][index].isdigit() and not cards[bot1card][index+1].isdigit(): 
      bot1 += int(cards[bot1card][index])
    elif cards[bot1card][index] == "a": 
      bot1 += 11
      bot1ace += 1
    else: 
      bot1 += 10
    print("startingbot1", bot1)

    if cards[playercard][index].isdigit() and not cards[playercard][index+1].isdigit(): 
      player += int(cards[playercard][index])
    elif cards[playercard][index] == "a": 
      player += 11
      playerace += 1
    else: 
      player += 10

    if cards[bot2card][index].isdigit() and not cards[bot2card][index+1].isdigit(): 
      bot2 += int(cards[bot2card][index])
    elif cards[bot2card][index] == "a": 
      bot2 += 11
      bot2ace += 1
    else: 
      bot2 += 10

    playercardlist.append(cards[playercard])

    started = False
    time.sleep(0.5)

  else: 
    if not playerturn and not lost and not won and not tied and not bot1died and not bot1win: 
      print("bot1round")
      # bot1 turn
      if bot1 < 17: 
        bot1card = random.randint(1,52)
        bot1num += 1
        while bot1card not in cardlist: 
          bot1card = random.randint(1,52) # get a card not taken
        cardlist.remove(bot1card)
        if cards[bot1card][index].isdigit() and not cards[bot1card][index+1].isdigit(): 
          bot1 += int(cards[bot1card][index])
          print("bot1 took", int(cards[bot1card][index]))
        elif cards[bot1card][index] == "a": 
          bot1 += 11
          bot1ace += 1
          print("bot1 took ace")
        else: 
          bot1 += 10
          print("bot1 took 10")
      elif not bot1skip: # bot ai
        if bot1 < 20: 
          if random.randint(0,1) == 1: 
            bot1card = random.randint(1,52)
            bot1num += 1
            while bot1card not in cardlist: 
              bot1card = random.randint(1,52) # get a card not taken
            cardlist.remove(bot1card)
            if cards[bot1card][index].isdigit(): 
              bot1 += int(cards[bot1card][index])
              print("bot1 took", int(cards[bot1card][index]))
            elif cards[bot1card][index] == "a": 
              bot1 += 11
              bot1ace += 1
              print("bot1 took ace")
            else: 
              bot1 += 10
              print("bot1 took 10")
          else: 
            bot1skip = True
            print('bot1skip')
        else: 
          bot1skip = True
          print("bot1skip")

      if bot1ace > 0: # if bot1 has an ace and about to die
        if bot1 > 21:
          bot1 -= 10
          bot1ace -= 1
          print("bot1 used ace")
      if bot1 > 21: # if bot1 dead
        bot1died = True
        print("bot1died")
      redrawScreen()
      #time.sleep(0.5)
      
      if bot1 == 21: 
        bot1win = True
      else:
        playerturn = True

      print("bot1 value:", bot1)

      drawText("Your Turn!", text_font, (0,0,0), 500, 50) # for player round
      pygame.display.flip() 
      print("playerround")
    
    if bot1died: 
      playerturn = True

    # player turn
    if playerturn and not lost and not won and not tied and not bot1win: 
      if clickingHit(): 
        print("clicking hit")
        playercard = random.randint(1,52)
        playernum += 1
        while playercard not in cardlist: 
          playercard = random.randint(1,52)
        cardlist.remove(playercard)
        if cards[playercard][index].isdigit() and not cards[playercard][index+1].isdigit(): 
          player += int(cards[playercard][index])
        elif cards[playercard][index] == "a": 
          player += 11
          playerace += 1
        else:
          player += 10
        
        playercardlist.append(cards[playercard])
        playerturn = False
        time.sleep(0.5)
        redrawScreen()

      elif clickingSkip(): 
        print("clicking skip")
        playerskip = True
        playerturn = False
    
    if not playerturn and not lost and not won and not tied and not bot1win: 
      print("bot2round")
      # bot2 turn
      if bot2 < 17: 
        bot2card = random.randint(1,52)
        bot2num += 1
        while bot2card not in cardlist: 
          bot2card = random.randint(1,52)
        cardlist.remove(bot2card)
        if cards[bot2card][index].isdigit() and not cards[bot2card][index+1].isdigit(): 
          bot2 += int(cards[bot2card][index])
          print("bot2 took", int(cards[bot2card][index]))
        elif cards[bot2card][index] == "a": 
          bot2 += 11
          bot2ace += 1
          print("bot2 took ace")
        else: 
          bot2 += 10
          print("bot2 took 10")
      elif not bot2skip: # bot ai
        if bot2 < 20: 
          if random.randint(0,1) == 1: 
            bot2card = random.randint(1,52)
            bot2num += 1
            while bot2card not in cardlist: 
              bot2card = random.randint(1,52) # get a card not taken
            cardlist.remove(bot2card)
            if cards[bot2card][index].isdigit(): 
              bot2 += int(cards[bot2card][index])
              print("bot2 took", int(cards[bot2card][index]))
            elif cards[bot2card][index] == "a": 
              bot2 += 11
              bot2ace += 1
              print("bot2 took ace")
            else: 
              print("bot2 took 10")
          else: 
            bot2skip = True
            print('bot2skip')
        else: 
          bot2skip = True
          print('bot2skip')
      
      if bot2ace > 0: # if bot2 has an ace and about to die
        if bot2 > 21:
          bot2 -= 10
          bot2ace -= 1
          print("bot2 used ace")
      if bot2 > 21: # if bot2 dead
        bot2died = True
        print("bot2died")

      redrawScreen()
      #time.sleep(0.5)
  
  if not playerturn and not lost and not won and not tied: 
    print("-------------------------------------------------------------------------------------------------")

    if playerace > 0: 
      if player > 21:
        player -= 10
        playerace -= 1
    print("player value:",player)
    print("bot2 value:",bot2)

    if (bot1skip and playerskip and bot2skip) or (bot1died and playerskip and bot2skip) or (bot1skip and playerskip and bot2died) or (bot1died and bot2died and not lost) or bot1win or player == 21 or bot2 == 21: 
      if ((bot2died or bot2 < bot1) and bot1 == player) or ((bot1died and bot1 < bot2) and bot2 == player) or (player == bot1 and bot1 == bot2): 
        tied = True
      elif (bot1died and player > bot2) or (bot2died and player > bot1) or max(bot1, bot2, player) == player or (bot1died and bot2died):
        won = True
      else:  
        lost = True
  
  if not playerturn: 
    if player > 21: 
      lost = True
    if lost: 
      gameover()
    if tied: 
      screen.fill((255,255,255))
      drawText("GAME OVER TIED", text_font, (0,0,0), 100, 100)  
      drawText("press r to restart", text_font, (0,0,0), 100, 200)
    if won: 
      screen.fill((255,255,255))
      drawText("YOU WON!!!!!!!!!!!!!!!", text_font, (0,0,0), 100, 100)
      drawText("press r to restart", text_font, (0,0,0), 100, 200)
    # redrawScreen()
    if lost or won or tied: 
      drawText("bot1: " + str(bot1), text_font, (0,0,0), 300, 100)
      drawText("bot2: " + str(bot2), text_font, (0,0,0), 300, 200)
      pygame.display.flip()
      key = pygame.key.get_pressed()
      if key[pygame.K_r]:
        cardlist = []
        for i in range(len(cards)): 
          cardlist.append(i+1)
        bot1 = 0
        player = 0
        bot2 = 0
        bot1num = 0
        bot2num = 0
        playernum = 0
        bot1ace = 0
        bot2ace = 0
        playerace = 0
        bot1died = False
        playerdied = False
        bot2died = False
        lost = False
        won = False
        tied = False
        playercardlist = []
        started = True
        bot1skip = False
        bot2skip = False
        playerskip = False
        bot1win = False
        redrawScreen()

pygame.quit()
