#
#  GemUO
#
#  Copyright 2005-2020 Max Kellermann <max.kellermann@gmail.com>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; version 2 of the License.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#

from twisted.internet import reactor
from uo.entity import *
from gemuo.engine import Engine
from gemuo.target import Target, SendTarget
from gemuo.defer import deferred_nearest_reachable_item, deferred_find_item_in_backpack
from gemuo.engine.items import UseAndTarget

class CutCloth(Engine):
    def __init__(self, client):
        Engine.__init__(self, client)

        d = deferred_find_item_in_backpack(client,
                                           lambda x: x.item_id in (ITEMS_CLOTH + ITEMS_BOLT))
        d.addCallbacks(self._found_cloth, self._success)

    def _found_cloth(self, result):
        self.cloth = result

        client = self._client
        d = deferred_nearest_reachable_item(client,
                                            lambda x: x.item_id in ITEMS_SCISSORS)
        d.addCallbacks(self._found_scissors, self._failure)

    def _found_scissors(self, result):
        d = UseAndTarget(self._client, result, self.cloth).deferred
        d.addCallbacks(self._cutted, self._failure)

    def _cutted(self, success):
        reactor.callLater(1, self._success)

class CutAllCloth(Engine):
    def __init__(self, client):
        Engine.__init__(self, client)

        self._next()

    def _next(self):
        client = self._client
        d = deferred_find_item_in_backpack(client,
                                           lambda x: x.item_id in (ITEMS_CLOTH + ITEMS_BOLT))
        d.addCallbacks(self._found_cloth, self._success)

    def _found_cloth(self, result):
        d = CutCloth(self._client).deferred
        d.addCallbacks(self._cutted, self._failure)

    def _cutted(self, result):
        self._next()
