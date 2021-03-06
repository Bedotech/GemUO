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
from twisted.python.failure import Failure
import uo.packets as p
from gemuo.error import *
from gemuo.engine import Engine

class NoSuchOption(Exception):
    def __init__(self, message='No such menu option'):
        Exception.__init__(self, message)

def select_option(menu, item):
    for i, option in enumerate(menu.options):
        if option.text[:len(item)] == item:
            return i + 1
    return None

class MenuResponse(Engine):
    def __init__(self, client, responses):
        Engine.__init__(self, client)

        assert len(responses) > 0
        self.responses = list(responses)

        self.call_id = reactor.callLater(5, self._timeout)

    def abort(self):
        Engine.abort(self)
        self.call_id.cancel()

    def on_packet(self, packet):
        if isinstance(packet, p.Menu):
            response, self.responses = self.responses[0], self.responses[1:]
            option = select_option(packet, response)
            if option is None:
                self.call_id.cancel()
                self._failure(NoSuchOption())
                return

            self._client.send(p.MenuResponse(packet.dialog_serial, option))

            if len(self.responses) == 0:
                self.call_id.cancel()
                self._success()

    def _timeout(self):
        # waiting for the menu to appear has taken too long; give up
        self._failure(Timeout('Menu timeout'))
