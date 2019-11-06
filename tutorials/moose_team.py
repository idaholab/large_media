#!/usr/bin/env python
#* This file is part of the MOOSE framework
#* https://www.mooseframework.org
#*
#* All rights reserved, see COPYRIGHT for full restrictions
#* https://github.com/idaholab/moose/blob/master/COPYRIGHT
#*
#* Licensed under LGPL 2.1, please see LICENSE for details
#* https://www.gnu.org/licenses/lgpl-2.1.html

from datetime import date, timedelta
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

REF_DATE = date(2008, 1, 1)

class Member(object):
    def __init__(self, name, start, end=date.today()):
        self.name = name
        self.start = start
        self.end = end
        self.days = (self.end - self.start).days
        self.offset = (self.start - REF_DATE).days

class Members(object):
    def __init__(self):
        self.__members = list()
    def __iter__(self):
        for m in self.__members:
            yield m
    def __len__(self):
        return len(self.__members)
    def __getitem__(self, index):
        return self.__members[index]
    def add(self, *args, **kwargs):
        self.__members.append(Member(*args, **kwargs))
    def names(self):
        return [m.name for m in self.__members]

if __name__ == '__main__':

    fig = plt.figure(figsize=(10,6), dpi=200)
    ax = fig.add_subplot(111)

    members = Members()
    members.add('Derek Gaston', date(2008, 3, 1))
    members.add('Cody Permann', date(2009, 1, 1))
    members.add(u'David Andr\u0161', date(2010, 4, 1))
    members.add('Jason Miller', date(2010, 6, 1))
    members.add('John Peterson', date(2011, 2, 1), date(2018, 12, 31))
    members.add('Andrew Slaughter', date(2013, 4, 8))
    members.add('Brian Alger', date(2015, 7, 1), date(2018, 10, 15))
    members.add('Fande Kong', date(2016, 5, 16))
    members.add('Joshua Hansel', date(2016,8,1))
    members.add('Robert Carlsen', date(2016, 9, 1))
    members.add('Alexander Lindsay', date(2017,8,1))

    for i, mem in enumerate(members):
        plt.barh(i, mem.days, left=mem.offset, zorder=3)

    ax.set_yticks(range(0, len(members)))
    ax.set_yticklabels(members.names())
    ax.tick_params('y', length=0)

    ax.set_xlim(0, (date.today() - REF_DATE).days)
    ax.set_xticks([(date(y, 1, 1) - REF_DATE).days for y in range(REF_DATE.year, date.today().year + 1)])
    ax.set_xticklabels(range(REF_DATE.year, date.today().year+1))

    ax.grid(True, axis='x', color=[0.75]*3, zorder=0)
    fig.tight_layout()
    fig.savefig('moose_team.png')
