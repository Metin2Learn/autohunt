#Under:
import uiScriptLocale
#Add:
import uiautohunt



#Under:
		del self.dlgRefineNew
#Add:
		del self.dlgAutohunt



#Under:
		if self.dlgRefineNew:
			self.dlgRefineNew.Destroy()
#Add:
		if self.dlgAutohunt:
			self.dlgAutohunt.Destroy()




#Under:
		self.dlgRefineNew = uiRefine.RefineDialogNew()
		self.dlgRefineNew.Hide()
#Add:
		self.dlgAutohunt = uiautohunt.AutoHunt()
		self.dlgAutohunt.Hide()




#Under:
	def AppendMaterialToRefineDialog(self, vnum, count):
		self.dlgRefineNew.AppendMaterial(vnum, count)
#Add:
	def OpenAutohuntWindow(self):
		self.dlgAutohunt.Open()

	def AutohuntRemoveSkillSlot(self, slot):
		self.dlgAutohunt.AutohuntRemoveSkillSlot(slot)

	def AutohuntRemoveItemSlot(self, slot):
		self.dlgAutohunt.AutohuntRemoveItemSlot(slot)