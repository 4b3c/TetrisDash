import pygame
import time

# Key bindings for various actions
actions = {
	"up": {"keys": (pygame.K_w, pygame.K_UP), "reset on": "key up"},
	"left": {"keys": (pygame.K_a, pygame.K_LEFT), "reset on": "time"},
	"down": {"keys": (pygame.K_s, pygame.K_DOWN), "reset on": "time"},
	"right": {"keys": (pygame.K_d, pygame.K_RIGHT), "reset on": "time"},
	"drop": {"keys": (pygame.K_SPACE,), "reset on": "key up"},
	"pause": {"keys": (pygame.K_ESCAPE,), "reset on": "key up"}
}

class UserInput:

	# Initialize the state for each key specified in the actions
	def __init__(self) -> None:
		self.pressed_keys = {
			key: {
				"pressed": False, # Whether the key is currently pressed
				"reset": True, # Whether the key is ready to be pressed again
				"last use": time.time(), # Last time the key was used
				"reset on": actions[setting]["reset on"] # Reset condition for the key
			} for setting in actions for key in actions[setting]["keys"]
		}
	
	# Update the state of each key
	def update(self, keys: dict) -> None:
		for key in self.pressed_keys:
			self.pressed_keys[key]["pressed"] = keys[key]
			# If the key is reset on release and it is not pressed, reset it
			# If the key is reset after a time period and the time has passed, reset it
			if ((self.pressed_keys[key]["reset on"] == "key up") and (not self.pressed_keys[key]["pressed"])) or \
			   ((self.pressed_keys[key]["reset on"] == "time") and (time.time() - self.pressed_keys[key]["last use"] > 0.2)):
				self.pressed_keys[key]["reset"] = True
				self.pressed_keys[key]["last use"] = time.time()

	# Check if any key for the given action is pressed and ready to be used
	def state(self, action: str) -> bool:
		for key in actions[action]["keys"]:
			if self.pressed_keys[key]["pressed"] and self.pressed_keys[key]["reset"]:
				self.pressed_keys[key]["reset"] = False  # Mark the key as not ready to be used again
				return True
		return False
