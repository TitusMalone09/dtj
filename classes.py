import pygame
import time

# Characters
class Sakura:
    def __init__(self, hp, max_hp, defense, attack):
        self.hp = hp
        self.max_hp = max_hp
        self.defense = defense
        self.attack = attack

class Lucien:
    def __init__(self, hp, max_hp, defense, attack):
        self.hp = hp
        self.max_hp = max_hp
        self.defense = defense
        self.attack = attack

class Aralis:
    def __init__(self, hp, max_hp, defense, attack):
        self.hp = hp
        self.max_hp = max_hp
        self.defense = defense
        self.attack = attack

class Embreth:
    def __init__(self, hp, max_hp, defense, attack):
        self.hp = hp
        self.max_hp = max_hp
        self.defense = defense
        self.attack = attack

class Mori:
    def __init__(self, hp, max_hp, defense, attack):
        self.hp = hp
        self.max_hp = max_hp
        self.defense = defense
        self.attack = attack

# Sakura Weapons
class Chakram:
    def __init__(self, x, y, direction):
        self.name = "Chakram"
        self.description = "A spinning disc that can be thrown at enemies."
        self.attack = 2
        self.frames = [
            pygame.image.load('graphics/map/chakram0.png'),
            pygame.image.load('graphics/map/chakram1.png'),
            pygame.image.load('graphics/map/chakram2.png'),
            pygame.image.load('graphics/map/chakram3.png')
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 4
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class NinjasChakram:
    def __init__(self, x, y, direction):
        self.name = "Ninja's Chakram"
        self.description = "A streamlined form of the chakram."
        self.attack = 3
        self.frames = [
            pygame.image.load('graphics/map/ninjas_chakram0.png'),
            pygame.image.load('graphics/map/ninjas_chakram1.png'),
            pygame.image.load('graphics/map/ninjas_chakram2.png'),
            pygame.image.load('graphics/map/ninjas_chakram3.png')
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 4
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class EliteChakram:
    def __init__(self, x, y, direction):
        self.name = "Elite Chakram"
        self.description = "A fully upgraded form of the chakram, only used by the greatest."
        self.attack = 4
        self.frames = [
            pygame.image.load('graphics/map/elite_chakram0.png'),
            pygame.image.load('graphics/map/elite_chakram1.png'),
            pygame.image.load('graphics/map/elite_chakram2.png'),
            pygame.image.load('graphics/map/elite_chakram3.png')
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 5
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class CrystalChakram:
    def __init__(self, x, y, direction):
        self.name = "Crystal Chakram"
        self.description = "A chakram made of crystal, fully sharpened to pierce through enemies."
        self.attack = 5
        self.frames = [
            pygame.image.load('graphics/map/crystal_chakram0.png'),
            pygame.image.load('graphics/map/crystal_chakram1.png'),
            pygame.image.load('graphics/map/crystal_chakram2.png'),
            pygame.image.load('graphics/map/crystal_chakram3.png')
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 5
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class MasterChakram:
    def __init__(self, x, y, direction):
        self.name = "Master Chakram"
        self.description = "A chakram so powerful, that none has had the ability to wield it."
        self.attack = 6
        self.frames = [
            pygame.image.load('graphics/map/master_chakram0.png'),
            pygame.image.load('graphics/map/master_chakram1.png'),
            pygame.image.load('graphics/map/master_chakram2.png'),
            pygame.image.load('graphics/map/master_chakram3.png')
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 6
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class AncientChakram:
    def __init__(self, x, y, direction):
        self.name = "Ancient Chakram"
        self.description = "A chakram that has been sealed away for millenia, only to be unleashed once again in full power."
        self.attack = 8
        self.frames = [
            pygame.image.load('graphics/map/ancient_chakram0.png'),
            pygame.image.load('graphics/map/ancient_chakram1.png'),
            pygame.image.load('graphics/map/ancient_chakram2.png'),
            pygame.image.load('graphics/map/ancient_chakram3.png')
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 7
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
# Lucien Weapons
class Katana:
    def __init__(self, direction):
        self.name = "Katana"
        self.description = "A classic katana."
        self.attack = 3
        self.range = 3
        self.direction = direction
        self.speed = 3
        self.last_update = time.time()

class RedKatana:
    def __init__(self, direction):
        self.name = "Red Katana"
        self.description = "A special kind of katana with a blood-red blade."
        self.attack = 4
        self.range = 3
        self.direction = direction
        self.speed = 3
        self.last_update = time.time()

class SerratedKatana:
    def __init__(self, direction):
        self.name = "Serrated Katana"
        self.description = "An extremely sharp katana with serrated edges."
        self.attack = 5
        self.range = 3
        self.direction = direction
        self.speed = 4
        self.last_update = time.time()

class SoulReaperKatana:
    def __init__(self, direction):
        self.name = "Soul Reaper Katana"
        self.description = "An infamous katana known for cutting not only the body, but the soul as well."
        self.attack = 6
        self.range = 4
        self.direction = direction
        self.speed = 4
        self.last_update = time.time()

class ThousandLayerKatana:
    def __init__(self, direction):
        self.name = "Thousand-Layer Katana"
        self.description = "A katana forged from a million layers of steel, producing a beautiful damascus pattern."
        self.attack = 7
        self.range = 4
        self.direction = direction
        self.speed = 5
        self.last_update = time.time()

class AncientKatana:
    def __init__(self, direction):
        self.name = "Ancient Katana"
        self.description = "An ancient katana of immense power, trapped in the castle for countless years."
        self.attack = 9
        self.range = 5
        self.direction = direction
        self.speed = 6
        self.last_update = time.time()

# Aralis Weapons
class Bow:
    def __init__(self, x, y, direction):
        self.name = "Bow"
        self.description = "A simple bow."
        self.attack = 2
        self.frames = pygame.image.load('graphics/map/arrow0.png')
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 4
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class ElvenBow:
    def __init__(self, x, y, direction):
        self.name = "Elven Bow"
        self.description = "A bow made from the wood of the elven forest."
        self.attack = 2
        self.frames = pygame.image.load('graphics/map/arrow0.png')
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 5
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class MarbleBow:
    def __init__(self, x, y, direction):
        self.name = "Marble Bow"
        self.description = "Marble of the most durable type comprises this bow."
        self.attack = 3
        self.frames = pygame.image.load('graphics/map/arrow0.png')
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 6
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class GoldenBow:
    def __init__(self, x, y, direction):
        self.name = "Golden Bow"
        self.description = "The most beautiful of all bows, this bow is made from the purest of gold."
        self.attack = 4
        self.frames = pygame.image.load('graphics/map/arrow0.png')
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 6
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class EmeraldBow:
    def __init__(self, x, y, direction):
        self.name = "Emerald Bow"
        self.description = "This extremely fast bow is composed of the most beautiful of emeralds."
        self.attack = 4
        self.frames = pygame.image.load('graphics/map/arrow0.png')
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 7
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class AncientBow:
    def __init__(self, x, y, direction):
        self.name = "Ancient Bow"
        self.description = "This bow, crafted by the great blacksmith Balf, was sealed away in the depths of the castle ages ago."
        self.attack = 6
        self.frames = pygame.image.load('graphics/map/arrow0.png')
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 8
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect

# Embreth Weapons
class Staff:
    def __init__(self, x, y, direction):
        self.name = "Staff"
        self.description = "A simple staff that can be used to cast fire spells."
        self.attack = 3
        self.frames = [
            pygame.image.load('graphics/map/fireball0.png'),
            pygame.image.load('graphics/map/fireball1.png'),
            pygame.image.load('graphics/map/fireball2.png'),
            pygame.image.load('graphics/map/fireball3.png')
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 3
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class ObsidianStaff:
    def __init__(self, x, y, direction):
        self.name = "Obsidian Staff"
        self.description = "A staff made from the darkest of obsidian."
        self.attack = 3
        self.frames = [
            pygame.image.load('graphics/map/fireball0.png'),
            pygame.image.load('graphics/map/fireball1.png'),
            pygame.image.load('graphics/map/fireball2.png'),
            pygame.image.load('graphics/map/fireball3.png')
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 4
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class RubyStaff:
    def __init__(self, x, y, direction):
        self.name = "Ruby Staff"
        self.description = "The firey ruby that composes this staff is said to have been forged in the heart of a volcano in the center of the world."
        self.attack = 4
        self.frames = [
            pygame.image.load('graphics/map/fireball0.png'),
            pygame.image.load('graphics/map/fireball1.png'),
            pygame.image.load('graphics/map/fireball2.png'),
            pygame.image.load('graphics/map/fireball3.png')
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 4
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class WretchedStaff:
    def __init__(self, x, y, direction):
        self.name = "Wretched Staff"
        self.description = "This magical staff has been feared by many for the evil that lurks within."
        self.attack = 6
        self.frames = [
            pygame.image.load('graphics/map/fireball0.png'),
            pygame.image.load('graphics/map/fireball1.png'),
            pygame.image.load('graphics/map/fireball2.png'),
            pygame.image.load('graphics/map/fireball3.png')
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 5
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class HolyStaff:
    def __init__(self, x, y, direction):
        self.name = "Holy Staff"
        self.description = "Only the pure in heart are able to wield this staff."
        self.attack = 5
        self.frames = [
            pygame.image.load('graphics/map/fireball0.png'),
            pygame.image.load('graphics/map/fireball1.png'),
            pygame.image.load('graphics/map/fireball2.png'),
            pygame.image.load('graphics/map/fireball3.png')
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 6
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect
    
class AncientStaff:
    def __init__(self, x, y, direction):
        self.name = "Ancient Staff"
        self.description = "The wielder of this staff has mastered the power of fire and has become one with the flames."
        self.attack = 7
        self.frames = [
            pygame.image.load('graphics/map/fireball0.png'),
            pygame.image.load('graphics/map/fireball1.png'),
            pygame.image.load('graphics/map/fireball2.png'),
            pygame.image.load('graphics/map/fireball3.png')
        ]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 7
        self.last_update = time.time()
        self.frame_rate = 0.1

    def move(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen, camera_x, camera_y):
        if time.time() - self.last_update > self.frame_rate:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.last_update = time.time()
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

    def get_rect(self):
        return self.rect

# Mori Weapons
class Bamboo:
    def __init__(self, direction):
        self.name = "Bamboo"
        self.description = "A simple bamboo staff, grown in Bloodmoor's ruins."
        self.attack = 3
        self.range = 4
        self.direction = direction
        self.speed = 3
        self.last_update = time.time()

class ToughBamboo:
    def __init__(self, direction):
        self.name = "Tough Bamboo"
        self.description = "A hearty stick of tried-and-true bamboo. (Nifty rhyme, huh?)"
        self.attack = 4
        self.range = 4
        self.direction = direction
        self.speed = 3
        self.last_update = time.time()

class UnbreakableBamboo:
    def __init__(self, direction):
        self.name = "Unbreakable Bamboo"
        self.description = "This bamboo staff is regarded as the toughest among them."
        self.attack = 4
        self.range = 5
        self.direction = direction
        self.speed = 4
        self.last_update = time.time()

class SharpBamboo:
    def __init__(self, direction):
        self.name = "Sharp Bamboo"
        self.description = "A bamboo staff that has been sharpened to an extremely fine edge."
        self.attack = 6
        self.range = 5
        self.direction = direction
        self.speed = 4
        self.last_update = time.time()

class WildBamboo:
    def __init__(self, direction):
        self.name = "Wild Bamboo"
        self.description = "WILD."
        self.attack = 6
        self.range = 5
        self.direction = direction
        self.speed = 5
        self.last_update = time.time()

class AncientBamboo:
    def __init__(self, direction):
        self.name = "Ancient Bamboo"
        self.description = "The bamboo staff of the ancient pandas. It is said to be the most feared natural weapon in the world."
        self.attack = 7
        self.range = 6
        self.direction = direction
        self.speed = 6
        self.last_update = time.time()

# Map
class VerticalPlatform:
    def __init__(self, x, y, width, height, min_y, max_y, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.min_y = min_y
        self.max_y = max_y
        self.speed = speed
        self.direction = 1
        self.last_direction = 1

    def update(self):
        old_y = self.rect.y

        self.rect.y += self.speed * self.direction

        if self.rect.top <= self.min_y or self.rect.bottom >= self.max_y:
            self.direction *= -1

    def draw(self, screen, camera_x, camera_y):
        screen.blit(pygame.image.load('graphics/map/vertical platform.png'), (self.rect.x - camera_x, self.rect.y - camera_y))

# Enemies
class Spider:
    def __init__(self, x, y, speed):
        self.image = pygame.image.load('graphics/map/spider.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.direction = 1

    def move(self, collision_rects, map_width):
        self.rect.x += self.speed * self.direction
        if self.rect.left < 0 or self.rect.right > map_width or check_collision(self.rect, collision_rects):
            self.direction *= -1

    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

class Frog:
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/map/frog.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.jump_height = 64
        self.jump_interval = 2
        self.last_jump_time = time.time()
        self.damage = 3

    def update(self):
        current_time = time.time()
        if current_time - self.last_jump_time >= self.jump_interval:
            self.jump()
            self.last_jump_time = current_time

    def jump(self):
        self.rect.y -= self.jump_height
        pygame.time.set_timer(pygame.USEREVENT + 1, 500)

    def land(self):
        self.rect.y += self.jump_height

    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            player.health -= self.damage

    def destroy(self):
        self.kill()

# Other
class DialogBox:
    def __init__(self, text, font, color, x, y, width, height, image=None):
        self.text = text
        self.font = font
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.current_text = ''
        self.index = 0
        self.last_update = time.time()
        self.update_interval = 0.03
        self.active = True
        self.complete = False
        self.lines = self.wrap_text(text, font, width - 20)
        self.current_line = 0
        self.image = image

    def wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)
        return lines

    def update(self):
        if self.active and self.current_line < len(self.lines):
            if time.time() - self.last_update > self.update_interval:
                if self.index < len(self.lines[self.current_line]):
                    self.current_text += self.lines[self.current_line][self.index]
                    self.index += 1
                    text_sfx = pygame.mixer.Sound('audio/text.mp3')
                    text_sfx.set_volume(0.4)
                    text_sfx.play()
                else:
                    self.current_text = ''
                    self.index = 0
                    self.current_line += 1
                self.last_update = time.time()
        elif self.current_line >= len(self.lines):
            self.complete = True

    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, (0, 0, 0), self.rect)
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
            y_offset = 10
            if self.image:
                screen.blit(self.image, (self.rect.x + 10, self.rect.y + 10))
                text_x = self.rect.x + 20 + self.image.get_width()
            else:
                text_x = self.rect.x + 10
            for i in range(self.current_line):
                text_surface = self.font.render(self.lines[i], True, self.color)
                screen.blit(text_surface, (text_x, self.rect.y + y_offset))
                y_offset += self.font.get_height()
            if self.current_line < len(self.lines):
                text_surface = self.font.render(self.current_text, True, self.color)
                screen.blit(text_surface, (text_x, self.rect.y + y_offset))

def check_collision(rect, collision_rects):
    for collision_rect in collision_rects:
        if rect.colliderect(collision_rect):
            return True
    return False