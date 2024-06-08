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
	
	# Update the save state of each key this object handles
	def update(self, keys: dict) -> None:
		for key in self.pressed_keys:
			self.pressed_keys[key]["pressed"] = keys[key]


	# Check if any key for the given action is pressed and ready to be used
	def state(self, action: str) -> bool:
		for key in actions[action]["keys"]:
			if not self.pressed_keys[key]["pressed"]: # If the key isn't pressed we reset that key but do nothign else
				self.pressed_keys[key]["reset"] = True
				return False
			
			if self.pressed_keys[key]["reset"]:
				self.pressed_keys[key]["reset"] = False  # Mark the key as not ready to be used again
				self.pressed_keys[key]["last use"] = time.time()
				return True
			elif ((self.pressed_keys[key]["reset on"] == "time") and (time.time() - self.pressed_keys[key]["last use"] > 0.2)):
				self.pressed_keys[key]["reset"] = True
		
		return False
