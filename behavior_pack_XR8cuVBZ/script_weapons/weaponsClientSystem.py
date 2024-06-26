# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()


class weaponsClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.namespace = clientApi.GetEngineNamespace()
        self.systemName =clientApi.GetEngineSystemName()
        self.ListenForEvent(self.namespace, self.systemName, "ClientItemTryUseEvent", self, self.ClientItemTryUseEvent)

    def ClientItemTryUseEvent(self, event):
        print(event)

    # 监听引擎OnScriptTickClient事件，引擎会执行该tick回调，1秒钟30帧
    def OnTickClient(self):
        """
        Driven by event, One tick way
        """
        pass

    # 被引擎直接执行的父类的重写函数，引擎会执行该Update回调，1秒钟30帧
    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        pass

    def Destroy(self):
        pass
