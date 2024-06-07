import pygame
import time

actions = {
	"up": {"keys": (pygame.K_w, pygame.K_UP), "reset on": "key up"},
	"left": {"keys": (pygame.K_a, pygame.K_LEFT), "reset on": "time"},
	"down": {"keys": (pygame.K_s, pygame.K_DOWN), "reset on": "time"},
	"right": {"keys": (pygame.K_d, pygame.K_RIGHT), "reset on": "time"},
	"drop": {"keys": (pygame.K_SPACE,), "reset on": "key up"},
	"pause": {"keys": (pygame.K_ESCAPE,), "reset on": "key up"}
}

class UserInput:

	def __init__(self) -> None:
		self.pressed_keys = {
			key: {
				"pressed": False,
				"reset": True,
				"last use": time.time(),
				"reset on": actions[setting]["reset on"]
			} for setting in actions for key in actions[setting]["keys"]
		}
		for key in self.pressed_keys:
			print(str(key) + ": " + str(self.pressed_keys[key]))
	
	def update(self, keys):
		for key in self.pressed_keys:
			self.pressed_keys[key]["pressed"] = keys[key]
			if (self.pressed_keys[key]["reset on"] == "key up") and (not self.pressed_keys[key]["pressed"]):
				self.pressed_keys[key]["reset"] = True
			elif (self.pressed_keys[key]["reset on"] == "time") and (time.time() - self.pressed_keys[key]["last use"] > 0.2):
				self.pressed_keys[key]["reset"] = True
				self.pressed_keys[key]["last use"] = time.time()

	def state(self, action) -> bool:
		for key in actions[action]["keys"]:
			if self.pressed_keys[key]["pressed"] and self.pressed_keys[key]["reset"]:
				self.pressed_keys[key]["reset"] = False
				return True
		return False
