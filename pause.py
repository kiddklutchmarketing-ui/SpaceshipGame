import pygame

def pause_game(screen):
    paused = True
    font = pygame.font.SysFont("arial", 48)
    text = font.render("PAUSED", True, (255,255,255))

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = False

        screen.blit(text, (350,250))
        pygame.display.flip()


def handle_event(event, screen):
    """Call this from your main event loop to trigger pause on `P` press.

    Example:
        for event in pygame.event.get():
            handle_event(event, screen)
    """
    try:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pause_game(screen)
    except Exception:
        pass
