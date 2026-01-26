import sys
import time
import os
import random

# Ensure project root on sys.path so `import sound` resolves to project `sound.py`
proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_root not in sys.path:
	sys.path.insert(0, proj_root)

try:
	import pygame
	from pygame.locals import *
except Exception:
	pygame = None

import sound


WIDTH, HEIGHT = 640, 480


def run_text_test():
	print('pygame not available — playing test sound')
	sound.sound.play('shoot')
	time.sleep(0.8)


def main():
	if not pygame:
		run_text_test()
		return

	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Spaceship — Mini Game')
	font = pygame.font.Font(None, 28)
	clock = pygame.time.Clock()

	# start background music
	try:
		sound.sound.play_music(loop=True)
	except Exception:
		pass
	# load sprites if available
	player_img = None
	enemy_img = None
	bullet_img = None
	try:
		# prefer PNGs, fall back to BMP
		ppath = os.path.join('assets', 'player.png') if os.path.exists(os.path.join('assets', 'player.png')) else os.path.join('assets', 'player.bmp')
		epath = os.path.join('assets', 'enemy.png') if os.path.exists(os.path.join('assets', 'enemy.png')) else os.path.join('assets', 'enemy.bmp')
		bpath = os.path.join('assets', 'bullet.png') if os.path.exists(os.path.join('assets', 'bullet.png')) else os.path.join('assets', 'bullet.bmp')
		if os.path.exists(ppath):
			player_img = pygame.image.load(ppath).convert_alpha()
		if os.path.exists(epath):
			enemy_img = pygame.image.load(epath).convert_alpha()
		if os.path.exists(bpath):
			bullet_img = pygame.image.load(bpath).convert_alpha()
	except Exception:
		player_img = enemy_img = bullet_img = None

	# player
	player = pygame.Rect(WIDTH // 2 - 20, HEIGHT - 60, 40, 40)
	speed = 6

	bullets = []  # list of rects
	bullet_speed = -10
	shoot_cooldown = 0

	enemies = []
	enemy_spawn = 0
	particles = []

	score = 0

	running = True
	while running:
		dt = clock.tick(60)
		for ev in pygame.event.get():
			if ev.type == QUIT:
				running = False
			elif ev.type == KEYDOWN:
				if ev.key == K_ESCAPE:
					running = False
				elif ev.key == K_m:
					# toggle mute
					try:
						sound.sound.toggle_mute()
					except Exception:
						pass
				elif ev.key == K_PLUS or ev.key == K_EQUALS:
					# increase volume
					try:
						curr = getattr(sound.sound, 'volume', 1.0)
						sound.sound.set_volume(min(1.0, curr + 0.1))
					except Exception:
						pass
				elif ev.key == K_MINUS:
					# decrease volume
					try:
						curr = getattr(sound.sound, 'volume', 1.0)
						sound.sound.set_volume(max(0.0, curr - 0.1))
					except Exception:
						pass
				elif ev.key == K_b:
					# toggle music on/off
					try:
						# if music playing, stop; else start
						import pygame as _pg
						if _pg.mixer.get_init() and _pg.mixer.music.get_busy():
							sound.sound.stop_music()
						else:
							sound.sound.play_music(loop=True)
					except Exception:
						pass
				elif ev.key == K_RIGHTBRACKET:
					# increase music volume
					try:
						mv = PER_SOUND_VOLUME.get('music', 0.7)
						sound.sound.set_music_volume(min(1.0, mv + 0.05))
					except Exception:
						pass
				elif ev.key == K_LEFTBRACKET:
					# decrease music volume
					try:
						mv = PER_SOUND_VOLUME.get('music', 0.7)
						sound.sound.set_music_volume(max(0.0, mv - 0.05))
					except Exception:
						pass

		keys = pygame.key.get_pressed()
		if keys[K_LEFT] or keys[K_a]:
			player.x -= speed
		if keys[K_RIGHT] or keys[K_d]:
			player.x += speed

		player.x = max(0, min(WIDTH - player.width, player.x))

		# shooting
		if keys[K_SPACE] and shoot_cooldown <= 0:
			b = pygame.Rect(player.centerx - 3, player.top - 8, 6, 10)
			bullets.append(b)
			shoot_cooldown = 14
			try:
				sound.sound.play('shoot')
			except Exception:
				pass

		if shoot_cooldown > 0:
			shoot_cooldown -= 1

		# update bullets
		for b in bullets[:]:
			b.y += bullet_speed
			if b.bottom < 0:
				bullets.remove(b)

		# spawn enemies (faster as score increases)
		enemy_spawn += 1
		spawn_rate = max(20, 60 - int(score * 0.8))
		if enemy_spawn > spawn_rate:
			enemy_spawn = 0
			ex = random.randint(0, WIDTH - 30)
			enemies.append(pygame.Rect(ex, -30, 30, 30))

		# update enemies
		for e in enemies[:]:
			e.y += 2 + score * 0.02
			if e.top > HEIGHT:
				running = False
			# collisions
			for b in bullets[:]:
				if e.colliderect(b):
					try:
						# play explosion sound on enemy hit
						sound.sound.play('explosion')
					except Exception:
						pass
					bullets.remove(b)
					try:
						enemies.remove(e)
					except ValueError:
						pass
					# spawn particles for explosion
					for _ in range(12):
						px = e.centerx + random.randint(-6, 6)
						py = e.centery + random.randint(-6, 6)
						ang = random.uniform(0, 2 * 3.14159)
						speedp = random.uniform(1.5, 4.0)
						vx = speedp * random.uniform(-1, 1)
						vy = speedp * random.uniform(-1, 1)
						particles.append({'x': px, 'y': py, 'vx': vx, 'vy': vy, 'life': random.uniform(0.5, 1.0)})
					score += 1
					break

		# draw - starfield background
		screen.fill((5, 5, 18))
		for i in range(40):
			sx = (i * 37 + (dt // 5)) % WIDTH
			sy = (i * 83 + score) % HEIGHT
			screen.set_at((sx, sy), (100, 100, 140))

		# update and draw particles
		for p in particles[:]:
			p['x'] += p['vx']
			p['y'] += p['vy']
			p['vy'] += 0.12  # gravity
			p['life'] -= dt / 1000.0
			if p['life'] <= 0:
				particles.remove(p)
				continue
			col = max(0, min(255, int(255 * (p['life']))))
			try:
				screen.set_at((int(p['x']) % WIDTH, int(p['y']) % HEIGHT), (col, col // 2, 30))
			except Exception:
				pass
		# player
		if player_img:
			screen.blit(player_img, player)
		else:
			pygame.draw.rect(screen, (100, 200, 250), player)
		# bullets
		for b in bullets:
			if bullet_img:
				screen.blit(bullet_img, b)
			else:
				pygame.draw.rect(screen, (255, 220, 120), b)
		# enemies
		for e in enemies:
			if enemy_img:
				screen.blit(enemy_img, e)
			else:
				pygame.draw.rect(screen, (240, 100, 120), e)

		hud = f'Score: {score}  (ESC to quit)'
		vol = getattr(sound.sound, 'volume', 1.0)
		muted = getattr(sound.sound, 'muted', False)
		aud = f"Volume: {int(vol*100)}% {'MUTED' if muted else ''}"
		txt = font.render(hud, True, (230, 230, 230))
		audiotxt = font.render(aud, True, (200, 200, 120))
		screen.blit(txt, (10, 10))
		screen.blit(audiotxt, (10, 36))

		pygame.display.flip()

	pygame.quit()


if __name__ == '__main__':
	main()

