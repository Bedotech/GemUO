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

from twisted.python import log
import uo.packets as p
from gemuo.engine import Engine
from gemuo.cliloc import lookup_cliloc

class PrintMessages(Engine):
    def __init__(self, client):
        Engine.__init__(self, client)

    def on_packet(self, packet):
        if isinstance(packet, p.AsciiMessage) and packet.type != 0x06 and \
           len(packet.text) > 0 and \
           (packet.text[0] != '[' or packet.text[-1] != ']'):
            log.msg("<%s> %s" % (packet.name, packet.text))
        elif isinstance(packet, p.UnicodeMessage) and packet.type != 0x06 and \
           len(packet.text) > 0 and \
           (packet.text[0] != '[' or packet.text[-1] != ']'):
            log.msg("<%s> %s" % (packet.name, packet.text))
        elif isinstance(packet, p.LocalizedMessage) and packet.type != 0x06:
            log.msg("<%s> %s" % (packet.name, lookup_cliloc(packet.text)))

class Parrot(Engine):
    def __init__(self, client):
        Engine.__init__(self, client)

    def on_packet(self, packet):
        if isinstance(packet, p.AsciiMessage):
            if packet.type == 0 and packet.serial != 0 and packet.serial != self._client.world.player.serial and \
               packet.serial != 0xffffffff and \
               len(packet.name) > 0 and packet.text != packet.name and packet.text[0] != '[':
                self._client.send(p.TalkAscii(type=packet.type, hue=packet.hue, font=packet.font, text=packet.text))
        elif isinstance(packet, p.UnicodeMessage):
            if packet.type == 0 and packet.serial != 0 and packet.serial != self._client.world.player.serial and \
               packet.serial != 0xffffffff and \
               packet.language != 'Eng' and \
               packet.text != '(bonded)' and \
               packet.text != '(tame)' and \
               packet.text != '(summoned)' and \
               packet.text[0] != '*' and \
               len(packet.name) > 0 and packet.text != packet.name and packet.text[0] != '[':
                self._client.send(p.TalkUnicode(text=packet.text, type=0x09, hue=packet.hue, font=packet.font))
