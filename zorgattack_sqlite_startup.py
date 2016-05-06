#!/bin/python

# voor nu, om het in ieder geval werktend te hebben
# ./zorgattack.py <parameter> <variabelen -> alleen met a(dd)
# parameters:
# a		- add (needs variabelen, 66 stuks)
# d		- delete something, moet ik nog maken
# s		- show something, ook nog te maken, per speler, locatie, grondstoffen gevonden, mijnen, defense of niet. 
# Mooi zou zijn als we iets kunnen denken dat het redelijk dynamisch is, dus bijv.
# ./zorgattack.py s speler:neusbeer 			of
# ./zorgattack,py a resources:1000000	(dus alle targets laten zien met 1mil aan gs te raiden), maar dan ook in combi
# ./zorgattack.py a resources:1000000,galaxy:5,inactive:true,timestamp:10 (days)

# ./zorgattack.py a  <variabelen> (of de variabelen als 2de argument, of een tekstfile verwijzing om in te lezen



import sqlite3
import sys
import os


sqlite_file = 'zorg_extreme.db'
	
def create_or_open_db(db_file):	
	try:
		db = sqlite3.connect(sqlite_file)
		cursor = db.cursor()
		# if table doesn't exist make it so.
		cursor.execute('''CREATE TABLE IF NOT EXISTS spy(coordinates TEXT, playername TEXT, timestamp INTEGER, moon INTEGER, player_status INTEGER, metal INTEGER, crystal INTEGER, deuterium INTEGER, solar INTEGER, fusion INTEGER, robot INTEGER, nanite INTEGER, yard INTEGER, storage_metal INTEGER, storage_crystal INTEGER, storage_deut INTEGER, lab INTEGER, terra INTEGER, depot INTEGER, silo INTEGER, lunarbase INTEGER, phalanx INTEGER, gate INTEGER, rocket_launcher INTEGER, light_laser INTEGER, heavy_laser INTEGER, gauss INTEGER, ion_weapon INTEGER, plasma_weapon INTEGER, small_shield INTEGER, large_shield INTEGER, anti_bal INTEGER, inter_miss INTEGER, espionage INTEGER, computer INTEGER, weapons INTEGER, shield INTEGER, armor INTEGER, energy INTEGER, hyperspace INTEGER, combustion INTEGER, impulse INTEGER, hyperspace_engine INTEGER, laser INTEGER, ion INTEGER, plasma INTEGER, intergalatic_reseach INTEGER, expedition INTEGER, physics INTEGER, graviton INTEGER, small_cargo INTEGER, large_cargo INTEGER, light_fighter INTEGER, heavy_fighter INTEGER, cruiser INTEGER, battleship INTEGER, colony_ship INTEGER, recycler INTEGER, espionage_ship INTEGER, bomber INTEGER, sats INTEGER, destroyer INTEGER, rips INTEGER, battlecruisers INTEGER, lunars INTEGER, ecargo INTEGER, erec INTEGER)''')
		db.commit()
	except Exception as e:
	# if anything happens bad happens when opening file, do rollback. just to be sure
		db.rollback()
		print 'error %s' % e
	finally:
		db.close()
	return db

def add_spy(coordinates, playername, timestamp, moon, player_status, metal, crystal, deuterium, solar, fusion, robot, nanite, yard, storage_metal, storage_crystal, storage_deut, lab, terra, depot, silo, lunarbase, phalanx, gate, rocket_launcher, light_laser, heavy_laser, gauss, ion_weapon, plasma_weapon, small_shield, large_shield, anti_bal, inter_miss, espionage, computer, weapons, shield, armor, energy, hyperspace, combustion, impulse, hyperspace_engine, laser, ion, plasma, intergalatic_reseach, expedition, physics, graviton, small_cargo, large_cargo, light_fighter, heavy_fighter, cruiser, battleship, colony_ship, recycler, espionage_ship, bomber, sats, destroyer, rips, battlecruisers, lunars, ecargo, erec):

	db = sqlite3.connect(sqlite_file)
	cursor = db.cursor()
	
	#looks more complicated than it is, insert into table spy, all the vars
	cursor.execute('''INSERT INTO spy(coordinates, playername, timestamp, moon, player_status, metal, crystal, deuterium, solar, fusion, robot, nanite, yard, storage_metal, storage_crystal, storage_deut, lab, terra, depot, silo, lunarbase, phalanx, gate, rocket_launcher, light_laser, heavy_laser, gauss, ion_weapon, plasma_weapon, small_shield, large_shield, anti_bal, inter_miss, espionage, computer, weapons, shield, armor, energy, hyperspace, combustion, impulse, hyperspace_engine, laser, ion, plasma, intergalatic_reseach, expedition, physics, graviton, small_cargo, large_cargo, light_fighter, heavy_fighter, cruiser, battleship, colony_ship, recycler, espionage_ship, bomber, sats, destroyer, rips, battlecruisers, lunars, ecargo, erec)
	VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (coordinates, playername, timestamp, moon, player_status, metal, crystal, deuterium, solar, fusion, robot, nanite, yard, storage_metal, storage_crystal, storage_deut, lab, terra, depot, silo, lunarbase, phalanx, gate, rocket_launcher, light_laser, heavy_laser, gauss, ion_weapon, plasma_weapon, small_shield, large_shield, anti_bal, inter_miss, espionage, computer, weapons, shield, armor, energy, hyperspace, combustion, impulse, hyperspace_engine, laser, ion, plasma, intergalatic_reseach, expedition, physics, graviton, small_cargo, large_cargo, light_fighter, heavy_fighter, cruiser, battleship, colony_ship, recycler, espionage_ship, bomber, sats, destroyer, rips, battlecruisers, lunars, ecargo, erec))
	
	db.commit()

	return db
	
#  uses main class, so doesn't execute/read everything but only needed for each function/def
if __name__ == "__main__":
	# check if db exists (only difference is Opening or Creating in the print statement ;))
	# It checks if table exists and creates it. db file is standard created after db.commit()
	db_is_new = not os.path.exists(sqlite_file)
	if db_is_new:
		print 'Creating database file : %s' % sqlite_file
		create_or_open_db(sqlite_file)
	else:
		print 'Opening database file : %s' % sqlite_file
		create_or_open_db(sqlite_file)

		
	# sloppy case for sys.argv, no checks.. 
	if sys.argv[1]=='a':
		print "Adding spy report to database"
		add_spy('5:405:5','Neusbeer',1462563035,1,1,36,35,36,36,11,16,10,21,6,4,5,16,2,2,5,0,0,0,8421,26059,4343,38,2000,68,1,1,0,25,15,19,18,18,18,15,9,18,17,13,14,10,14,7,6,5,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
	if sys.argv[1]=='d':
		print "Deleting spy report from database"
	if sys.argv[1]=='s':
		print "Showing spy report from database"

		
# moet alleen 1 belangrijk probleem oplossen nog ;)
# om duplicaten tegen te gaan, moet ik script nog wijzigen dat hij eerst gaat zoeken of hij al een spy rapport heeft
# van die locatie.   wordt lastig karweitje.. 