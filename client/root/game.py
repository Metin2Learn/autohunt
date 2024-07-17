#Under:
			if player.SLOT_TYPE_QUICK_SLOT == attachedType:
				player.RequestDeleteGlobalQuickSlot(attachedItemSlotPos)
#Add:
			if player.SLOT_TYPE_AUTOHUNT_ITEM == attachedType:
				self.interface.AutohuntRemoveItemSlot(attachedItemSlotPos)

			if player.SLOT_TYPE_AUTOHUNT_SKILL == attachedType:
				self.interface.AutohuntRemoveSkillSlot(attachedItemSlotPos)