from typing import Tuple, Union, List
from char.i_char import IChar
from config import Config
from logger import Logger
from pather import Location, Pather
from typing import Union
from item.pickit import PickIt
from template_finder import TemplateFinder
from town.town_manager import TownManager
from ui import UiManager
from utils.misc import wait
from dataclasses import dataclass
from chest import Chest
from screen import Screen
import read_mem
from utils.misc import wait, rotate_vec, unit_vector
import math
import numpy as np
import keyboard
import random
from utils.custom_mouse import mouse

class LowerKurast:
	def __init__(
		self,
		screen: Screen,
		template_finder: TemplateFinder,
		pather: Pather,
		town_manager: TownManager,
		ui_manager: UiManager,
		char: IChar,
		pickit: PickIt,
	):
		self._config = Config()
		self._template_finder = template_finder
		self._pather = pather
		self._town_manager = town_manager
		self._ui_manager = ui_manager
		self._char = char
		self._pickit = pickit
		self._chest = Chest(screen, self._char, self._template_finder, 'lowerkurast')
		self._screen = screen



	def approach(self, start_loc: Location) -> Union[bool, Location]:
		Logger.info("Run LowerKurast")
		if not self._char.can_teleport():
			raise ValueError("LK requires teleport")
		if not self._town_manager.open_wp(start_loc):
			return False
		wait(0.4)
		if self._ui_manager.use_wp(3, 4):
			return Location.A3_LK_START
		return False

	def tele_k(self, cast_pos_abs: Tuple[float, float], spray: int = 30):
		keyboard.send('capslock', do_release=False)
		
		keyboard.send('f6')
		for _ in range(15):
			x = cast_pos_abs[0] + (random.random() * 2*spray - spray)
			y = cast_pos_abs[1] + (random.random() * 2*spray - spray)
			cast_pos_monitor = self._screen.convert_abs_to_monitor((x, y))
			mouse.move(*cast_pos_monitor)
			mouse.press(button="right")
			wait(0.0123, 0.071)
			mouse.release(button="right")

		keyboard.send('capslock', do_press=False)


	def chest_3(self):


		roi = [0,0,1280,720]

		img = self._screen.grab()
		template_match = self._template_finder.search(
			["LK_3"],
			img,
			threshold=0.3,
			roi=roi,
			normalize_monitor=True
		)
		if template_match.valid:
			pos = template_match.position
			pos = (pos[0], pos[1] )
			
			for i in range(2):
				mouse.move(*pos, randomize=6, delay_factor=[0.9, 1.1])
				wait(0.08, 0.15)
				keyboard.send('capslock', do_release=False)
				keyboard.send('f6')
				mouse.click(button="right")
				Logger.debug("chest_3")
				keyboard.send('capslock', do_press=False)

	def chest_2(self):


		roi = [0,0,1280,720]

		img = self._screen.grab()
		template_match = self._template_finder.search(
			["LK_2"],
			img,
			threshold=0.35,
			roi=roi,
			normalize_monitor=True
		)
		if template_match.valid:
			pos = template_match.position
			pos = (pos[0], pos[1] )
			
			for i in range(2):
				mouse.move(*pos, randomize=6, delay_factor=[0.9, 1.1])
				wait(0.08, 0.15)
				keyboard.send('capslock', do_release=False)
				keyboard.send('f6')
				mouse.click(button="right")
				Logger.debug("chest_3")
				keyboard.send('capslock', do_press=False)


	def chest_11(self):


		roi = [0,0,1280,720]

		img = self._screen.grab()
		template_match = self._template_finder.search(
			["LK_11","LK_02"],
			img,
			threshold=0.45,
			roi=roi,
			normalize_monitor=True
		)
		if template_match.valid:
			pos = template_match.position
			pos = (pos[0], pos[1] )
			
			for i in range(5):
				mouse.move(*pos, randomize=6, delay_factor=[0.9, 1.1])
				wait(0.08, 0.15)
				keyboard.send('capslock', do_release=False)
				keyboard.send('f6')
				mouse.click(button="right")
				Logger.debug("chest_3")
				keyboard.send('capslock', do_press=False)

	def chest_1(self):


		roi = [0,0,1280,720]

		img = self._screen.grab()
		template_match = self._template_finder.search(
			["LK_1"],
			img,
			threshold=0.3,
			roi=roi,
			normalize_monitor=True
		)
		if template_match.valid:
			pos = template_match.position
			pos = (pos[0], pos[1] )
			
			for i in range(5):
				mouse.move(*pos, randomize=6, delay_factor=[0.9, 1.1])
				wait(0.08, 0.15)
				keyboard.send('capslock', do_release=False)
				keyboard.send('f6')
				mouse.click(button="right")
				Logger.debug("chest_3")
				keyboard.send('capslock', do_press=False)


	def chest_00(self):


		roi = [0,0,1280,720]

		img = self._screen.grab()
		template_match = self._template_finder.search(
			["LK_00","LK_01"],
			img,
			threshold=0.45,
			roi=roi,
			normalize_monitor=True
		)
		if template_match.valid:
			pos = template_match.position
			pos = (pos[0], pos[1] )
			
			for i in range(2):
				mouse.move(*pos, randomize=6, delay_factor=[0.9, 1.1])
				wait(0.08, 0.15)
				keyboard.send('capslock', do_release=False)
				keyboard.send('f6')
				mouse.click(button="right")
				Logger.debug("chest_3")
				keyboard.send('capslock', do_press=False)

	def chest_0(self):


		roi = [0,0,1280,720]

		img = self._screen.grab()
		template_match = self._template_finder.search(
			["LK_0"],
			img,
			threshold=0.3,
			roi=roi,
			normalize_monitor=True
		)
		if template_match.valid:
			pos = template_match.position
			pos = (pos[0], pos[1] )
			
			for i in range(2):
				mouse.move(*pos, randomize=6, delay_factor=[0.9, 1.1])
				wait(0.08, 0.15)
				keyboard.send('capslock', do_release=False)
				keyboard.send('f6')
				mouse.click(button="right")
				Logger.debug("chest_3")
				keyboard.send('capslock', do_press=False)



	def battle(self, do_pre_buff: bool) -> Union[bool, tuple[Location, bool]]:
		self._char.pre_buff()

		picked_up_items = False
		self.used_tps = 0

		#get new starting offsets
		d2 = read_mem.d2r_proc()
		#find our player
		try:
			d2.get_player_offset(128)
		except:
			log = ("!! Unable to find player, are you at the title screen?")
			print(colored(log, 'red'))
			exit()
		d2.find_info()
		d2.get_ppos()
		#d2.get_map_json(str(d2.map_seed))
		#d2.get_map_d2api(d2.map_seed)
		d2.get_map_json(d2.map_seed)
		#d2.find_objects()
		

		target_x = d2.chests[0]['x']
		target_y = d2.chests[0]['y']
		target1_x = d2.chests[1]['x'] +5
		target1_y = d2.chests[1]['y'] -2
		#print('target vector ->' +str(target))
		target2_x = d2.chests[2]['x'] - d2.map_ox
		target2_y = d2.chests[2]['y'] - d2.map_oy

		print('target pos = '+str(target_x)+'< >'+str(target_y))
		d2.get_ppos()
		player_x = d2.x_pos
		player_y = d2.y_pos
		odist = math.dist([target_x,target_y],[player_x,player_y])


		moves = 0
		while odist >16:
			print('odist + '+ str(odist))
			d2.get_ppos()
			player_x = d2.x_pos 
			player_y = d2.y_pos 
			target_x =(d2.chests[1]['x']+d2.chests[2]['x'])/2.0
			target_y =(d2.chests[1]['y']+d2.chests[2]['y'])/2.0
			grid_x = (target_x-player_x)-(target_y-player_y)
			grid_y = (target_x-player_x)+(target_y-player_y)
			o_pos_x = (grid_x)*20
			o_pos_y = (grid_y)*10
			if odist < 100:
				o_pos_x = (grid_x)*(odist/5)
				o_pos_y = (grid_y)*(odist/5)

			pos_m = self._pather._adjust_abs_range_to_screen([o_pos_x,o_pos_y-10])
			zero = self._screen.convert_abs_to_monitor(pos_m)
			self._char.pre_move()
			self._char.move(zero)
			odist = math.dist([target_x,target_y],[player_x,player_y])
			moves+=1
			if moves>120:
				break

		target_x =(d2.chests[0]['x']+d2.chests[1]['x'])/2.0
		target_y =(d2.chests[0]['y']+d2.chests[1]['y'])/2.0

		odist = math.dist([target2_x,target2_y],[player_x,player_y])
		moves = 0
		wait(.5)
		moves = 0
		while odist >4.7:
			print('odist + '+ str(odist))
			d2.get_ppos()
			player_x = d2.x_pos 
			player_y = d2.y_pos 
			target_x =(d2.chests[0]['x']+d2.chests[1]['x'])/2.0
			target_y =(d2.chests[0]['y']+d2.chests[1]['y'])/2.0
			grid_x = (target_x-player_x)-(target_y-player_y)
			grid_y = (target_x-player_x)+(target_y-player_y)
			o_pos_x = (grid_x)*20
			o_pos_y = (grid_y)*10
			if odist < 100:
				o_pos_x = (grid_x)*20*.35
				o_pos_y = (grid_y)*10*.35

			pos_m = self._pather._adjust_abs_range_to_screen([o_pos_x,o_pos_y-10])
			zero = self._screen.convert_abs_to_monitor(pos_m)
			self._char.pre_move()
			self._char.move(zero)
			odist = math.dist([target_x,target_y],[player_x,player_y])
			moves+=1
			if moves>120:
				break


		target_x = d2.chests[0]['x']
		target_y = d2.chests[0]['y']
		target1_x = d2.chests[1]['x']
		target1_y = d2.chests[1]['y']
		#print('target vector ->' +str(target))
		target2_x = d2.chests[2]['x']
		target2_y = d2.chests[2]['y']

		d2.get_ppos()
		player_x = d2.x_pos
		player_y = d2.y_pos
		grid_x = (target_x-player_x)-(target_y-player_y)
		grid_y = (target_x-player_x)+(target_y-player_y)
		o_pos_x = (grid_x)*20
		o_pos_y = (grid_y)*10
		pos_m = self._pather._adjust_abs_range_to_screen([o_pos_x,o_pos_y-10])
		self.tele_k(pos_m)


		d2.get_ppos()
		player_x = d2.x_pos
		player_y = d2.y_pos
		grid_x = (target1_x-player_x)-(target1_y-player_y)
		grid_y = (target1_x-player_x)+(target1_y-player_y)
		o_pos_x = (grid_x)*20
		o_pos_y = (grid_y)*10
		pos_m = self._pather._adjust_abs_range_to_screen([o_pos_x,o_pos_y-10])
		self.tele_k(pos_m)


		picked_up_items = self._pickit.pick_up_items(self._char)

		d2.chest_dist()
		player_x = d2.x_pos
		player_y = d2.y_pos
		#picked_up_items |= self._pickit.pick_up_items(self._char)

		odist = math.dist([target2_x,target2_y],[player_x,player_y])
		moves = 0

		while odist >5:
			print('odist + '+ str(odist))
			d2.get_ppos()
			player_x = d2.x_pos
			player_y = d2.y_pos 
			target2_x = d2.chests[2]['x']-5
			target2_y = d2.chests[2]['y']-2
			grid_x = (target2_x-player_x)-(target2_y-player_y)
			grid_y = (target2_x-player_x)+(target2_y-player_y)
			o_pos_x = (grid_x)*20*.5
			o_pos_y = (grid_y)*10*.5
			if odist < 150:
				o_pos_x = (grid_x)*20*.35
				o_pos_y = (grid_y)*10*.35
			if odist < 20:
				o_pos_x = (grid_x)*20*.2
				o_pos_y = (grid_y)*10*.2
			pos_m = self._pather._adjust_abs_range_to_screen([o_pos_x,o_pos_y-10])
			zero = self._screen.convert_abs_to_monitor(pos_m)
			self._char.pre_move()
			self._char.move(zero)
			odist = math.dist([target2_x,target2_y],[player_x,player_y])
			moves+=1
			if moves>120:
				break

		#pos_m = self._screen.convert_abs_to_monitor([-40,0])
		#self._char.move(pos_m)


		target2_x = d2.chests[2]['x']
		target2_y = d2.chests[2]['y']

		d2.get_ppos()
		player_x = d2.x_pos
		player_y = d2.y_pos
		grid_x = (target2_x-player_x)-(target2_y-player_y)
		grid_y = (target2_x-player_x)+(target2_y-player_y)
		o_pos_x = (grid_x)*20
		o_pos_y = (grid_y)*10
		#zero = self._screen.convert_abs_to_monitor([0,0])
		#mouse.move(*zero,delay_factor=[0.3, .6])
		#wait(.2)
		#mouse.move(*[o_pos_x,o_pos_y],delay_factor=[0.3, .6], absolute=False)
		pos_m = self._pather._adjust_abs_range_to_screen([o_pos_x,o_pos_y-15])
		#zero = self._screen.convert_abs_to_monitor(pos_m)
		self.tele_k(pos_m)



		self.chest_2()
		self.chest_3()
		self.chest_11()
		
		#self._cast_circle(cast_dir=[-.5,-1],cast_start_angle=-22.5,cast_end_angle=2.5,cast_div=3,cast_v_div=3,cast_spell='f6',offset=1.1,delay=1.6)

		picked_up_items = self._pickit.pick_up_items(self._char)
		
		return (Location.A3_LK_END, picked_up_items)


if __name__ == "__main__":
	from screen import Screen
	import keyboard
	from game_stats import GameStats
	import os
	keyboard.add_hotkey('f12', lambda: os._exit(1))
	keyboard.wait("f11")
	from config import Config
	from ui import UiManager
	from bot import Bot
	config = Config()
	screen = Screen(config.general["monitor"])
	game_stats = GameStats()
	bot = Bot(screen, game_stats, False)
	#bot._arcane._find_summoner([(500, 40)])
