import pygame
import os
import random

pygame.init()

pygame.font.init()

#COLOR 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
    
#FPS
FPS = 60

#CONSTANT VARIABLE
WIDTH, HEIGHT = 600, 500  

#BG
BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "Background_image.jpg")), (WIDTH, HEIGHT))

#Icon size
icon_width, icon_height = 100, 100

#ICON
ROCK = pygame.transform.smoothscale(pygame.image.load(
    os.path.join("Assets", "Rock_icon.png")), (icon_width, icon_height))
PAPER = pygame.transform.smoothscale(pygame.image.load(
    os.path.join("Assets", "Paper_icon.png")), (icon_width, icon_height))
SCISSORS = pygame.transform.smoothscale(pygame.image.load(
    os.path.join("Assets", "Scissors_icon.png")), (icon_width, icon_height))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

#selection of choices
selection =  [ROCK,  PAPER, SCISSORS]

#Divide the screen into two part (Left and Right)
LEFT = pygame.Rect(0, 0, WIDTH// 2, HEIGHT)
RIGHT = pygame.Rect(WIDTH // 2, 0, WIDTH// 2, HEIGHT)

#FONT
font = pygame.font.SysFont("comicsans", 20)
conclu_font = pygame.font.SysFont("comicsans", 50)
menu_font = pygame.font.SysFont("comicsans", 25)

player_choice = ROCK

#Conclusion Text
won_text = conclu_font.render("You won!",1, BLACK)
lose_text = conclu_font.render("You lose.",1, BLACK)
tie_text = conclu_font.render("It is tie.",1, BLACK)




    

#take only screen element 
def draw_mainscreen():
    global player_choice
    #Background of the Windown 
    WIN.blit(BACKGROUND, (0,0))
    
    text = font.render("Please Select your move from the above selection.",
                       1, BLACK)
    
    selection_text = font.render("Rock (1). Paper (2). Scissors (3).",
                       1, BLACK)
    
    #Blit the text
    WIN.blit(text, (80, 470))
    WIN.blit(selection_text, (150, 440))

    
    #update the WIN
    pygame.display.update()
    
    
   
def computer_bot():
    return random.choice(selection)

def draw_computer(computer_choice):
    #Get the middle position of the RIGHT side of the screen for computer_bot
                      #find the starting point of icon, not the middle of RIGHT
    RIGHT_x = RIGHT.left + (RIGHT.width - computer_choice.get_width()) //2
    RIGHT_y = 0 + (RIGHT.height - computer_choice.get_height())//2
    
    #May variable na kukuha ng atake ng computer
    WIN.blit(computer_choice, (RIGHT_x, RIGHT_y))
    pygame.display.update()

def player_move():
    global player_choice
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_1]:
        player_choice = ROCK 
    elif keys_pressed[pygame.K_2]:
        player_choice = PAPER
    elif keys_pressed[pygame.K_3]:
        player_choice = SCISSORS
    
    draw_player()
    

def draw_player():
    global player_choice
    #SHOW the player choice
     
    # Get the rect of the icon image
    icon_rect = player_choice.get_rect()
    
    # Calculate the center of the RIGHT rectangle
    right_center = (LEFT.left + LEFT.width // 2, 
                    LEFT.top + LEFT.height // 2)
    
    # Calculate the position to blit the icon image to the center of the RIGHT rectangle
    icon_position = (right_center[0] - icon_rect.width // 2, right_center[1] - icon_rect.height // 2)
    
    # Blit the icon image onto the screen
    WIN.blit(player_choice, icon_position)


def game_logic(computer_choice):
    global player_choice
    #TRUE = player won; FALSE = Computer won 
    if player_choice == computer_choice:
        return None
    elif player_choice == ROCK:
        if computer_choice == PAPER:
            return False
        elif computer_choice == SCISSORS:
            return True
    elif player_choice == PAPER:
        if computer_choice == SCISSORS:
            return False
        elif computer_choice == ROCK:
            return True
    elif player_choice == SCISSORS:
        if computer_choice == ROCK:
            return False
        elif computer_choice == PAPER:
            return True
     
        
def game_conclusion(game_result):
    center_pos =  (215, 120)
    if game_result == None:
        WIN.blit(tie_text, center_pos)
    elif game_result == True:
        WIN.blit(won_text, center_pos)
    elif game_result == False:
        WIN.blit(lose_text, center_pos)
           
    pygame.display.update()
    
    
def main():
    global player_choice
    computer_choice = computer_bot()
    clock = pygame.time.Clock()
    draw_mainscreen()
    run = True    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                    #Main game
                    player_move()
                    game_result = game_logic(computer_choice)
                    draw_computer(computer_choice)
                    game_conclusion(game_result)
                    pygame.time.delay(5000)                    
                    pygame.quit()


        pygame.quit()
                   


if __name__ == "__main__":
   main()