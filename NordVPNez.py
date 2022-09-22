#!/usr/bin/env python3

import os
import subprocess
import time
from simple_term_menu import TerminalMenu

def main():

	sys = os.system

	check = str(subprocess.check_output("nordvpn status | grep Connected | wc -l", shell=True))

	if check[2] == str(1):

		Options = ["Disconnect", "Quit"]

		sys('clear')
		sys('figlet Nord  VPN  ez | lolcat')
		sys('echo Liam Doocey 22.09.22 | lolcat')
		print('')

		sys('echo You are already connected to a server please disconnect first to choose a new one or you can exit the program! | lolcat ')
		print('')

		terminal_menu = TerminalMenu(Options)
		menu_entry_index = terminal_menu.show()
		Choice = Options[menu_entry_index]

		if Choice == "Disconnect":
			sys('nordvpn disconnect')
			sys('clear')

			sys('figlet Nord  VPN  ez | lolcat')
			sys('echo Liam Doocey 22.09.22 | lolcat')
			print('')
			sys('echo Successfully disconnected! | lolcat')
			print('')
			sys('echo Would you like to connect to a new server? | lolcat')
			print('')

			YeNo = ["Yes", "No Thanks!"]

			terminal_menu_menu = TerminalMenu(YeNo)
			index = terminal_menu_menu.show()
			Choice = YeNo[index]

			if Choice == "Yes":
				sys('python3 NordVPNez.py')
			else:
				print('')
				sys('\n echo Thank you for using NordVPNez, App closing.... | lolcat')
				time.sleep(3)
		else:
			quitting = True
	else:

		Locations = []

		sys('clear')
		sys('figlet Nord  VPN  ez | lolcat')
		sys('echo Liam Doocey 22.09.22 | lolcat')
		print('')

		with open("Countries.txt", "r")as fp:
			for line in fp:
				x = line[:-1]
				Locations.append(x) 		

		terminal_menu = TerminalMenu(Locations, title="Locations \n")	
		menu_entry_index = terminal_menu.show()

		sys('figlet Nord  VPN  ez | lolcat')
		sys('echo Liam Doocey 22.09.22 | lolcat')
		print('')

		sys('echo Are you sure you want to connect to ' + str(Locations[menu_entry_index]) + '? | lolcat')
		print('')

		YeNo = ["Yes", "No thats the wrong server!"]

		terminal_menu_menu = TerminalMenu(YeNo)
		index = terminal_menu_menu.show()
		Choice = YeNo[index]

		if Choice == "Yes":
			sys('clear')
	
			cmd = 'nordvpn connect ' + str(Locations[menu_entry_index])
			sys(cmd)
			sys('clear')

			sys('figlet Nord  VPN  ez | lolcat')
			sys('echo Liam Doocey 22.09.22 | lolcat')
			print('')

			sys('echo You are now connected to ' + str(Locations[menu_entry_index]) + '| lolcat')
			print('')
			sys('echo Thank you for using NordVPNez, App closing.... | lolcat')
			time.sleep(3)

		else: 
			sys('python3 NordVPNez.py')


if __name__ == "__main__":
	main()