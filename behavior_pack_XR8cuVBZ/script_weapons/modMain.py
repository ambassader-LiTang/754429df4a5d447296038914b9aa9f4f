# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name="script_weapons", version="0.0.1")
class script_weapons(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def script_weaponsServerInit(self):
        serverApi.RegisterSystem("shaojiweapons","shaojiweapon_server",
                                 "script_weapons.weaponsServerSystem.weaponsServerSystem")
        pass

    @Mod.DestroyServer()
    def script_weaponsServerDestroy(self):
        pass

    @Mod.InitClient()
    def script_weaponsClientInit(self):
        clientApi.RegisterSystem("shaojiweapons", "shaojiweapon_client",
                                 "script_weapons.weaponsClientSystem.weaponsClientSystem")
        pass

    @Mod.DestroyClient()
    def script_weaponsClientDestroy(self):
        pass
