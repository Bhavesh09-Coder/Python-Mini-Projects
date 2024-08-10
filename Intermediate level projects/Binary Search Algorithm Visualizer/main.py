## Binary Search Algorithm Visualizer :
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Binary Search Visualizer")

# Fonts
font = pygame.font.Font(None, 36)

def draw_array(array, low, mid, high):
    screen.fill(WHITE)
    for i, value in enumerate(array):
        color = BLACK
        if i == mid:
            color = BLUE
        elif i < low or i > high:
            color = RED
        elif i >= low and i <= high:
            color = GREEN
        
        pygame.draw.rect(screen, color, (i * 40 + 10, SCREEN_HEIGHT // 2, 30, -value * 5))
        value_text = font.render(str(value), True, BLACK)
        screen.blit(value_text, (i * 40 + 10, SCREEN_HEIGHT // 2 + 10))
    pygame.display.flip()

def binary_search_visualized(array, target):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        draw_array(array, low, mid, high)
        pygame.time.wait(1000)
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        
    return -1

def main():
    array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        prompt_text = font.render("Press any key to start the binary search visualization", True, BLACK)
        screen.blit(prompt_text, (SCREEN_WIDTH // 2 - prompt_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        pygame.display.flip()
        
        if event.type == pygame.KEYDOWN:
            result = binary_search_visualized(array, target)
            screen.fill(WHITE)
            if result != -1:
                result_text = font.render(f"Element {target} found at index {result}", True, BLACK)
            else:
                result_text = font.render(f"Element {target} not found", True, BLACK)
            screen.blit(result_text, (SCREEN_WIDTH // 2 - result_text.get_width() // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
