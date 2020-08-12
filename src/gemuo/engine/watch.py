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
from uo.skills import *
from uo.stats import *
import uo.packets as p
from uo.entity import *
from gemuo.engine import Engine

class Watch(Engine):
    """Watch skills and stats for changes."""

    def __init__(self, client):
        Engine.__init__(self, client)

        self.player = client.world.player
        self.skills = None
        self.stats = None

        # get current stat & skill values
        client.send(p.MobileQuery(0x04, self.player.serial))
        client.send(p.MobileQuery(0x05, self.player.serial))

        self.update()

    def update(self):
        stats = self.player.stats
        if stats is None:
            self.stats = None
        elif self.stats is None:
            for i, name in enumerate(STAT_NAMES):
                log.msg("Stat '%s' = %d" % (name, stats[i]))
        else:
            for i, name in enumerate(STAT_NAMES):
                if stats[i] != self.stats[i]:
                    log.msg("Stat '%s': %d -> %d" % (name, self.stats[i], stats[i]))

        self.stats = stats

        skills = self.player.skills
        if skills is None:
            self.skills = None
        else:
            skill_list = [x for x in iter(skills.values()) if x.base > 0]
            skill_list.sort(key=lambda x: x.base, reverse=True)

            total = 0
            down = 0
            change = self.skills is None
            for x in skill_list:
                if x.lock == SKILL_LOCK_DOWN:
                    down += x.base

                if self.skills is None or x.id not in self.skills:
                    log.msg("Skill '%s': %d" % (SKILL_NAMES[x.id], x.base))
                    change = True
                elif x.base != self.skills[x.id].base:
                    log.msg("Skill '%s': %d -> %d" % (SKILL_NAMES[x.id], self.skills[x.id].base, x.base))
                    change = True

                total += x.base
            if change:
                log.msg("Skills total=%u down=%u" % (total, down))

        if skills is not None:
            self.skills = skills.copy()
        else:
            self.skills = None

    def on_mobile_status(self, mobile):
        self.update()

    def on_skill_update(self, skills):
        self.update()
