import pygame
import sys

pygame.init()
pygame.display.set_caption("Rylan Kinnie")
screen = pygame.display.set_mode((500,500))

while True:
    # Here's another loop inside of the first loop. Notice the indentation,
    # moving one tab width into the while loop makes this statement part of the
    # loop instead of outside of it.
    for event in pygame.event.get():
        print(event)

        # we must allow our users to quit the game right? I mean not everyone
        # wants to play forever.
        # This is a conditional statement, i.e., the line sys.exit() will ONLY
        # execute when event.type is equal to pygame.QUIT (this is what ==
        # means). 
        if event.type == pygame.QUIT:
            sys.exit()

        # Additional interactions with events

    screen.fill(pygame.Color("Gray"))

    pygame.draw.circle(screen, pygame.Color("blue"), (50,50), 25)
    pygame.draw.circle(screen, pygame.Color(255,0,0),(screen.get_width()/2,screen.get_height()/2), 100,  )
    pygame.draw.circle(screen, pygame.Color(255,255,0), (0,screen.get_height()), 100 )

    pygame.display.update()
