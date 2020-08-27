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

from uo.skills import *

T2A = True

def skill_delay(skill):
    if skill in (SKILL_HERDING, SKILL_MUSICIANSHIP):
        return 1

    if skill in (SKILL_HIDING, SKILL_PEACEMAKING):
        return 11

    if skill in (SKILL_BEGGING,):
        return 13

    if T2A:
        return 11

    return 1.5
