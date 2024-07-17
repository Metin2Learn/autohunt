#Under:
			chr.NEW_AFFECT_GOLD_BONUS : (localeInfo.TOOLTIP_MALL_GOLDBONUS_STATIC, "d:/ymir work/ui/skill/common/affect/gold_bonus.sub",),
#Add:
			chr.NEW_AFFECT_AUTOHUNT : (localeInfo.TOOLTIP_AUTO_SYSTEM_PRIMIUM, "d:/ymir work/ui/pattern/autohunt_mark.tga",),



#Under:
		if not self.AFFECT_DATA_DICT.has_key(affect):
			return
#Add:
		if type == chr.NEW_AFFECT_AUTOHUNT:
			import constInfo
			constInfo.autohunt_bonus = 1