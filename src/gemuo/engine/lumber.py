#
#  GemUO
#
#  (c) 2005-2010 Max Kellermann <max@duempel.org>
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
import uo.packets as p
from gemuo.engine import Engine
from gemuo.target import Target
from gemuo.error import *
from gemuo.engine.items import UseAndTarget

def find_axe(world):
    return world.equipped_item(world.player, 0x2) or world.equipped_item(world.player, 0x1)

class Lumber(Engine):
    def __init__(self, client, map, tree, exhaust_db):
        Engine.__init__(self, client)

        self.exhaust_db = exhaust_db
        self.exhausted = False
        self.tries = 5

        self.tree = tree

        self.axe = find_axe(client.world)
        if self.axe is None:
            self._failure(NoSuchEntity('No axe'))
            return

        self._begin_chop()

    def _begin_chop(self):
        player = self._client.world.player
        if player.mass_remaining() < 40:
            self._success()
            return

        d = UseAndTarget(self._client, self.axe, self.tree).deferred
        d.addCallbacks(self._chopped, self._target_failure)

    def _target_failure(self, fail):
        if self.exhausted:
            self._success()
            return

        self.tries -= 1
        if self.tries > 0:
            self._begin_chop()
        else:
            self._failure(fail)

    def _chopped(self, result):
        self.tries = 5
        if self.exhausted:
            self._success()
        else:
            reactor.callLater(1, self._begin_chop)

    def on_system_message(self, text):
        if 'not enough wood here' in text or \
               'That is too far away' in text or \
               'Target cannot be seen' in text:
            self.exhausted = True
            self.exhaust_db.set_exhausted(self.tree.x / 8, self.tree.y / 8)
        elif 'You broke your axe' in text:
            self.exhausted = True

    def on_localized_system_message(self, text):
        if text in (0x7a30d, # not enough wood
                    0x7a2de, # too far away
                    ):
            self.exhausted = True
            self.exhaust_db.set_exhausted(self.tree.x / 8, self.tree.y / 8)
