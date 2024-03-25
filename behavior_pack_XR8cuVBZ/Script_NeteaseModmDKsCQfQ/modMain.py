# -*- coding: utf-8 -*-

from mod.common.mod import Mod


@Mod.Binding(name="Script_NeteaseModmDKsCQfQ", version="0.0.1")
class Script_NeteaseModmDKsCQfQ(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModmDKsCQfQServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModmDKsCQfQServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModmDKsCQfQClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModmDKsCQfQClientDestroy(self):
        pass
