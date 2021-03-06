import Map
import pygame
import sys
import Command

# Make a new map object
m = Map.Map("UW")

# Display dimensions to 1600 x 1100
screen = pygame.display.set_mode((1600, 1100))

# Objects that will control fps
clock = pygame.time.Clock()
fps = 120

while True:
    # Loop fps times per second
    clock.tick(fps)

    for event in pygame.event.get():
        # Close if the exit button is pressed
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            inputKey = event.key  # The key that got pressed...

            # Zoom in if z is pressed
            if inputKey == pygame.K_z:  # If it's z, do this
                m.zoom_in()
                m.zoom_marker()

            # Zoom out if x is pressed
            elif inputKey == pygame.K_x:  # If it's x, do this
                m.zoom_out()
                m.zoom_marker()

            elif inputKey == pygame.K_0:
                m.get_mouse_lat_lng(pygame.mouse.get_pos())

            elif inputKey == pygame.K_END:
                screen.fill((0, 0, 0))
                pygame.display.flip()
                m.open_map()

            elif inputKey == pygame.K_c:
                Command.command(m)

        # Move the tiles if you're moving the mouse with left button down
        if event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:
                # clicked and moving
                rel = event.rel
                # Pass the dx and dy to the move_map function
                m.move_map(rel[0], rel[1])

    # Fill with black, display, and update
    screen.fill((0, 0, 0))
    m.display(screen)
    pygame.display.flip()
    pygame.event.pump()
