"The Storming of Bloodmoor Castle"

import pygame
from variables import *

# Main
def run():
    # Variables
    running = True
    character_x, character_y = 32, 544
    is_paused, is_jump, is_knockback = False, False, False
    current_dialog, blink_timer, damage_cooldown, knockback_timer = 0, 0, 0, 0
    pause_start_time, total_pause_duration = 0, 0
    camera_x, camera_y, camera_width, camera_height = 0, 0, 800, 640
    character_velocity, jump_height, jump_speed, gravity, fall_speed, step_size = 2.5, 48, 8, 0.5, 6, 4
    character_hp, last_chakram_time = 30, 0
    character_facing_right = True
    chakrams = []
    current_map, spider = map0, None

    # Settings
    pygame.init()
    pygame.display.set_caption('The Storming of Bloodmoor Castle')
    pygame.display.set_icon(bloodmoor_castle_image)
    pygame.mixer.music.load('audio/entrance.mp3')
    pygame.mixer.music.play(loops = -1)
    clock = pygame.time.Clock()

    # Functions
    def update_camera(character_x, character_y, map_width, map_height):
        global camera_x, camera_y
   
        target_x = character_x - camera_width // 2
        target_y = character_y - camera_height // 2
    
        camera_x = max(0, min(target_x, map_width - camera_width))
        camera_y = max(0, min(target_y, map_height - camera_height))

    def draw_pause_menu(screen):
        screen_width, screen_height = screen.get_size()
        vertical_line_x = screen_width // 4
        menu_font = pygame.font.Font(None, 54)
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height))
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, screen_width, screen_height), 2)
        pygame.draw.line(screen, (255, 255, 255), (0, screen_height * 3 // 4), (screen_width, screen_height * 3 // 4), 2)
        pygame.draw.line(screen, (255, 255, 255), (vertical_line_x, 0), (vertical_line_x, screen_height * 3 // 4), 2)
        sakura_text = menu_font.render('Sakura', True, (255, 255, 255))
        hp_text = menu_font.render(f'HP: {character_hp}', True, (255, 255, 255))
        screen.blit(sakura_text, (35, 35 + sakura_dialog_image.get_height() + 10))
        screen.blit(hp_text, (35, 35 + sakura_dialog_image.get_height() + 10 + sakura_text.get_height() + 5))
        screen.blit(sakura_dialog_image, (35, 35))
        draw_map(screen, map_layout)

    def update_visited_rooms(color, map_layout, target_row, target_col):
        color = color
        if 0 <= target_row < len(map_layout) and 0 <= target_col < len(map_layout[0]):
            map_layout[target_row][target_col] = 1

    def draw_map(screen, map_layout):
        tile_size = 16
        map_surface = pygame.Surface((27 * tile_size, 27 * tile_size))
        for y, row in enumerate(map_layout):
            for x, tile in enumerate(row):
                color = (0, 0, 0)
                if tile == 1:
                    color = blue
                elif tile == 2:
                    color = orange
                elif tile == 3:
                    color = pink
                elif tile == 4:
                    color = light_blue
                elif tile == 5:
                    color = yellow
                elif tile == 6:
                    color = gray
                elif tile == 7:
                    color = purple
                elif tile == 8:
                    color = red
                pygame.draw.rect(map_surface, color, (x * tile_size, y * tile_size, tile_size, tile_size))
        screen.blit(map_surface, (250, 3))

    def check_collision(rect, collision_rects, platforms):
        for collision_rect in collision_rects:
            if rect.colliderect(collision_rect):
                return True
        for platform in platforms:
            if rect.colliderect(platform.rect):
                return True
        return False

    def draw_hp(screen, hp):
        font = pygame.font.Font(None, 36)
        hp_text = font.render(f'HP: {hp}', True, (255, 255, 255))
        text_rect = hp_text.get_rect()
        text_rect.topleft = (24, 24)
        pygame.draw.rect(screen, (0, 0, 0), (text_rect.x - 10, text_rect.y - 5, text_rect.width + 20, text_rect.height + 10))
        pygame.draw.rect(screen, (255, 255, 255), (text_rect.x - 10, text_rect.y - 5, text_rect.width + 20, text_rect.height + 10), 2)
        screen.blit(hp_text, text_rect.topleft)
    
    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    is_paused = not is_paused
                    if is_paused:
                        pause_start_time = time.time()
                    else:
                        total_pause_duration += time.time() - pause_start_time

            if is_paused:
                draw_pause_menu(screen)
                pygame.display.flip()
                continue

            if event.type == pygame.KEYDOWN and not is_paused:
                if event.key == pygame.K_UP and not is_jump and is_on_ground and (current_dialog >= len(dialogs0) or not dialogs0[current_dialog].active):
                    is_jump = True
                    jump_speed = 16
                    jump_sfx = pygame.mixer.Sound('audio/jump.mp3')
                    jump_sfx.set_volume(0.4)
                    jump_sfx.play()
                
                if event.key == pygame.K_SPACE:
                    if current_dialog < len(dialogs0) and dialogs0[current_dialog].complete:
                        dialogs0[current_dialog].active = False
                        current_dialog += 1
                        if current_dialog < len(dialogs0):
                            dialogs0[current_dialog].active = True
                    elif current_dialog >= len(dialogs0) or not dialogs0[current_dialog].active:
                        if time.time() - last_chakram_time - total_pause_duration > 1:
                            direction = 1 if character_facing_right else -1
                            chakram = Chakram(character_x, character_y + 16, direction)
                            chakrams.append(chakram)
                            last_chakram_time = time.time() - total_pause_duration

        if is_paused:
            draw_pause_menu(screen)
            pygame.display.flip()
            continue

        keys = pygame.key.get_pressed()
        new_x, new_y = character_x, character_y

        if current_dialog >= len(dialogs0) or not dialogs0[current_dialog].active:
            if keys[pygame.K_LEFT]:
                new_x -= character_velocity
                character_facing_right = False
            if keys[pygame.K_RIGHT]:
                new_x += character_velocity
                character_facing_right = True

        is_falling = not is_jump
        is_on_ground = False

        for _ in range(step_size):
            new_rect_x = pygame.Rect(new_x, character_y, 32, 32)
            if not check_collision(new_rect_x, current_map.collision_rects, [platform0]):
                character_x = new_x
            else:
                break

        if is_jump:
            if jump_speed > -jump_height // gravity:
                for _ in range(step_size):
                    new_y -= jump_speed / step_size
                    if check_collision(pygame.Rect(character_x, new_y, 32, 32), current_map.collision_rects, [platform0]):
                        new_y += jump_speed / step_size
                        is_jump = False
                        break
                jump_speed -= gravity
            else:
                is_jump = False

        for _ in range(step_size):
            new_rect_y = pygame.Rect(character_x, new_y, 32, 32)
            if not check_collision(new_rect_y, current_map.collision_rects, [platform0]):
                character_y = new_y
            else:
                if is_falling:
                    character_y = new_rect_y.top // current_map.tile_size * current_map.tile_size - 32
                    is_on_ground = True
                is_jump = False
                jump_speed = 16
                break

        # Map transitions
        if character_x >= 784 and current_map == map0:
            chakrams.clear()
            current_map = map1
            character_x = -15
            spider = Spider(400, 544, 2)
            update_visited_rooms(red, map_layout, target_row = 26, target_col = 1)
        elif character_x < -16 and current_map == map1:
            chakrams.clear()
            current_map = map0
            character_x = 785
        elif character_x > 784 and current_map == map1:
            chakrams.clear()
            current_map = map2
            character_x = -15
            update_visited_rooms(blue, map_layout, target_row = 26, target_col = 2)
        elif character_x < -16 and current_map == map2:
            chakrams.clear()
            current_map = map1
            character_x = 785
            spider = Spider(400, 544, 2)
        elif character_y <= -16 and current_map == map2:
            chakrams.clear()
            current_map = map3
            character_y = 1904

        if character_x < 0 and current_map == map0:
            character_x = 0

        character_rect = pygame.Rect(character_x, character_y, 32, 32)

        if not check_collision(character_rect, current_map.collision_rects, [platform0]):
            for _ in range(step_size):
                character_y += fall_speed / step_size
                if check_collision(pygame.Rect(character_x, character_y, 32, 32), current_map.collision_rects, [platform0]):
                    character_y -= fall_speed / step_size
                    is_on_ground = True
                    break

        current_map.draw(screen)

        if current_map == map1 and spider:
            spider.move(current_map.collision_rects, current_map.width)
            spider.draw(screen, camera_x, camera_y)
            if character_rect.colliderect(spider.rect) and time.time() > damage_cooldown:
                character_hp -= 4
                damage_cooldown = time.time() + 3
                blink_timer = time.time() + 3
                knockback_distance = 40
                knockback_jump_height = 25
                is_knockback = True
                knockback_timer = time.time() + 0.2
                if spider.direction < 0:
                    character_x -= knockback_distance
                else:
                    character_x += knockback_distance
                character_y -= knockback_jump_height

        if current_map == map2:
            platform0.draw(screen, camera_x, camera_y)
            platform0.update()

            if character_rect.colliderect(platform0.rect):
                if not is_jump:
                    character_y = platform0.rect.top - 32
                    is_on_ground = True
                    jump_speed = 16

        if is_knockback:
            if time.time() < knockback_timer:
                character_y += gravity
            else:
                is_knockback = False

        if time.time() < blink_timer:
            if int(time.time() * 10) % 2 == 0:
                screen.blit(character_image, (character_x - camera_x, character_y - camera_y))
        else:
            screen.blit(character_image, (character_x - camera_x, character_y - camera_y))

        if current_dialog >= len(dialogs0) or not dialogs0[current_dialog].active:
            draw_hp(screen, character_hp)

        if current_dialog < len(dialogs0) and dialogs0[current_dialog].active:
            dialogs0[current_dialog].update()
            dialogs0[current_dialog].draw(screen)

        for chakram in chakrams:
            chakram.move()
            chakram.draw(screen, camera_x, camera_y)
            if spider and chakram.get_rect().colliderect(spider.rect):
                chakrams.remove(chakram)
                spider = None

        update_camera(character_x, character_y, map_width = current_map.width, map_height = current_map.height)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

run()