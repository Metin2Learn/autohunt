//Under:
PyObject * playerGetTargetVID(PyObject* poSelf, PyObject* poArgs)
{
	return Py_BuildValue("i", CPythonPlayer::Instance().GetTargetVID());
}
//Add:
PyObject * playerUpdateAutohunt(PyObject* poSelf, PyObject* poArgs)
{
	CPythonPlayer::Instance().UpdateAutohunt();
	return Py_BuildNone();
}



//Under:
		{ "GetTargetVID",				playerGetTargetVID,					METH_VARARGS },
//Add:
		{ "UpdateAutohunt",				playerUpdateAutohunt,					METH_VARARGS },


//Under:
	PyModule_AddIntConstant(poModule, "SLOT_TYPE_DRAGON_SOUL_INVENTORY",	SLOT_TYPE_DRAGON_SOUL_INVENTORY);
//Add:
	PyModule_AddIntConstant(poModule, "SLOT_TYPE_AUTOHUNT_SKILL",	SLOT_TYPE_AUTOHUNT_SKILL); 
	PyModule_AddIntConstant(poModule, "SLOT_TYPE_AUTOHUNT_ITEM",	SLOT_TYPE_AUTOHUNT_ITEM); 