#Under:
				Type == player.SLOT_TYPE_MALL or\
#Add:
				Type == player.SLOT_TYPE_AUTOHUNT_ITEM or\




#This:
			elif Type == player.SLOT_TYPE_SKILL:
#Change to:
			elif Type == player.SLOT_TYPE_SKILL or Type == player.SLOT_TYPE_AUTOHUNT_SKILL: