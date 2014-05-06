#   pyLogMerge is a program that merges log files that can be easily adapted
#   to fit any style log files. It is just a proof of concept and an easy program
#   that I wrote to teach myself python
#
#   the default log format is as follows:
#   MODE YEAR MONTH DAY TIMESTAMP USER ACTION OPCOST
#
#   Copyright (C) 2014  Cameron M Brock
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from logger import *

def main():
    log1 = readLog(sys.argv[1])
    log2 = readLog(sys.argv[2])
    log3 = mergeLogs(log1,log2)
    printLog(log3)
    printCost(log3)
    return

main()
