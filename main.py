import pygame
import sys
import random

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 10, 10)
LIGHT_RED = (255, 100, 100)
BLUE = (10, 10, 255)
GREY = (200, 200, 200)

pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Papers Scissors")
clock = pygame.time.Clock()
FPS = 60




class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 36)
    
    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.is_hovered(mouse_pos)
        button_color = self.hover_color if is_hovered else self.color
        
        # Draw the button rectangle

        pygame.draw.rect(surface, button_color, (self.x, self.y, self.width, self.height))
        
        # Draw the text

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        surface.blit(text_surface, text_rect)
    
    def is_hovered(self, mouse_pos):
        return self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height
    
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            return self.is_hovered(pygame.mouse.get_pos())
        return False

class TextBox:
    def __init__(self, x, y, width, height, text, color, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 36)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        surface.blit(text_surface, text_rect)




# Create Class

rockButton = Button(50, 700 , 200, 60, "Rock", RED, LIGHT_RED)
paperButton = Button(300, 700 , 200, 60, "Paper", RED, LIGHT_RED)
scissorsButton = Button(550, 700 , 200, 60, "Scissors", RED, LIGHT_RED)

rockButtonAI = TextBox(50, 150, 200, 60, "Rock", BLUE)
paperButtonAI = TextBox(300, 150, 200, 60, "Paper", BLUE)
scissorsButtonAI = TextBox(550, 150, 200, 60, "Scissors", BLUE)

readyButton = Button(300, 350, 200, 60, "Ready", RED, LIGHT_RED)

ScoreText = TextBox(0, 0, WIDTH, 100, "Player: 0 | AI: 0", GREY)
timerText = TextBox(300, 350, 200, 60, "3", GREY)




playerChoice = None
aiChoice = None
playerPoints = 0
AIPoints = 0

def countdown():
    for i in range(2, 0, -1):
        timerText.text = str(i)
        screen.fill(WHITE)
        rockButton.draw(screen)
        paperButton.draw(screen)
        scissorsButton.draw(screen)
        rockButtonAI.draw(screen)
        paperButtonAI.draw(screen)
        scissorsButtonAI.draw(screen)
        ScoreText.draw(screen)
        timerText.draw(screen)
        pygame.display.flip()
        pygame.time.delay(1000)

while True:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if rockButton.is_clicked(event):
            print("Rock button clicked")
            playerChoice = 0

        if paperButton.is_clicked(event):
            print("Paper button clicked")
            playerChoice = 1
        
        if scissorsButton.is_clicked(event):
            print("Scissors button clicked")
            playerChoice = 2



        if readyButton.is_clicked(event):

            countdown()

            if playerChoice != None:
                aiChoice = random.randint(0, 2)

                print("AI choice is", aiChoice)
                if playerChoice == aiChoice:
                    print("Tie")
                elif playerChoice == 0 and aiChoice == 1:
                    print("AI wins")
                    AIPoints += 1
                elif playerChoice == 0 and aiChoice == 2:
                    print("Player wins")
                    playerPoints += 1
                elif playerChoice == 1 and aiChoice == 0:
                    print("Player wins")
                    playerPoints += 1
                elif playerChoice == 1 and aiChoice == 2:
                    print("AI wins")
                    AIPoints += 1
                elif playerChoice == 2 and aiChoice == 0:
                    print("AI wins")
                    AIPoints += 1
                elif playerChoice == 2 and aiChoice == 1:
                    print("Player wins")
                    playerPoints += 1
                playerChoice = None
    




    rockButton.draw(screen)
    paperButton.draw(screen)
    scissorsButton.draw(screen)

    rockButtonAI.draw(screen)
    paperButtonAI.draw(screen)
    scissorsButtonAI.draw(screen)

    ScoreText.text = f"Player: {playerPoints} | AI: {AIPoints}"
    ScoreText.draw(screen)

    if playerChoice != None:
        readyButton.draw(screen)



    pygame.display.flip()
    clock.tick(FPS)