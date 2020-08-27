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

from twisted.python.failure import Failure
from twisted.internet import reactor, defer
from gemuo.entity import *
from gemuo.error import *
from gemuo.engine.items import OpenContainer
from gemuo.engine.player import QuerySkills

def deferred_find_item_in(client, parent, func):
    i = client.world.find_item_in(parent, func)
    if i is not None:
        return defer.succeed(i)

    d = defer.Deferred()
    e = OpenContainer(client, parent).deferred

    def second_lookup():
        i = client.world.find_item_in(parent, func)
        if i is not None:
            d.callback(i)
        else:
            d.errback(NoSuchEntity())

    def callback(result):
        reactor.callLater(1, second_lookup)
        return result

    def errback(fail):
        d.errback(fail)
        return fail

    e.addCallbacks(callback, errback)
    return d

def deferred_find_item_in_recursive(client, parent, func):
    containers = []
    d = defer.Deferred()

    def callback(result):
        d.callback(result)

    def errback(fail, parent, containers):
        for i in client.world.items_in(parent):
            if i.item_id in ITEMS_CONTAINER:
                containers.append(i)

        if len(containers) == 0:
            d.errback(fail)
            return

        parent, containers = containers[0], containers[1:]

        e = deferred_find_item_in(client, parent, func)
        e.addCallback(callback)
        e.addErrback(errback, parent, containers)

    e = deferred_find_item_in(client, parent, func)
    e.addCallback(callback)
    e.addErrback(errback, parent, containers)
    return d

def deferred_find_item_in_backpack(client, func):
    backpack = client.world.backpack()
    if backpack is None:
        return defer.fail(NoSuchEntity('No backpack'))

    return deferred_find_item_in(client, backpack, func)

def deferred_amount_in(client, parent, func):
    d = defer.Deferred()
    e = OpenContainer(client, parent).deferred

    def count():
        total = 0
        for i in client.world.items_in(parent):
            if func(i):
                total += i.amount
        d.callback(total)

    def callback(result):
        reactor.callLater(1, count)
        return result

    def errback(fail):
        d.errback(fail)
        return fail

    e.addCallbacks(callback, errback)
    return d

def deferred_amount_in_backpack(client, func):
    backpack = client.world.backpack()
    if backpack is None:
        return defer.fail(NoSuchEntity('No backpack'))

    return deferred_amount_in(client, backpack, func)

def deferred_nearest_reachable_item(client, func):
    i = client.world.nearest_reachable_item(func)
    if i is not None:
        return defer.succeed(i)

    return deferred_find_item_in_backpack(client, func)

def deferred_find_player_item(client, func):
    i = client.world.find_player_item(func)
    if i is not None:
        return defer.succeed(i)

    return deferred_find_item_in_backpack(client, func)

def deferred_skills(client):
    skills = client.world.player.skills
    if skills is not None:
        return defer.succeed(skills)

    d = defer.Deferred()
    e = QuerySkills(client).deferred

    def callback(result):
        skills = client.world.player.skills
        if skills is not None:
            d.callback(skills)
        else:
            defer.errback(NoSkills())
        return result

    def errback(fail):
        d.errback(fail)
        return fail

    e.addCallbacks(callback, errback)
    return d

def deferred_skill(client, skill):
    d = defer.Deferred()
    e = deferred_skills(client)

    def callback(result):
        if skill in result:
            d.callback(result[skill])
        else:
            defer.errback(NoSkills())
        return result

    def errback(fail):
        d.errback(fail)
        return fail

    e.addCallbacks(callback, errback)
    return d
