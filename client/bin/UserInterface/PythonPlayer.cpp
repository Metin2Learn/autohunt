//ABOVE <-------------------------------------:
void CPythonPlayer::ExitParty()
//Add:
void CPythonPlayer::UpdateAutohunt()
{
	CPythonCharacterManager& rkChrMgr=CPythonCharacterManager::Instance();
	int nDistance = 3000;
	DWORD targetVID = 0;
	CInstanceBase* pkInstMain=rkChrMgr.GetMainInstancePtr();
	CPythonCharacterManager::CharacterIterator i;
	for(i = rkChrMgr.CharacterInstanceBegin(); i!=rkChrMgr.CharacterInstanceEnd(); ++i)
	{
		CInstanceBase* pkInstEach=*i;
		if (pkInstEach==pkInstMain)
			continue;
		if (!pkInstEach->IsEnemy() || pkInstEach->IsDead())
			continue;
		int iDistance = int(pkInstEach->NEW_GetDistanceFromDestInstance(*pkInstMain));
		if (iDistance < nDistance)
		{
			nDistance = iDistance;
			targetVID = pkInstEach->GetVirtualID();
		}
	}
	if (nDistance < 3000)
		m_dwAutoAttackTargetVID = targetVID;
}