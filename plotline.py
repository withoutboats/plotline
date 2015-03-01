"""
plotline plots a simple line graph of tabular input data from files or stdin. It
will plot up to 16 lines. See the readme for more information.

LICENSE NOTICE:

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import sys
from itertools import chain

import matplotlib.pyplot as plot

def float_or_0(val):
    """Returns the float of val or 0.0 if float(val) raises an error."""
    try: return float(val)
    except: return 0.0

def parse(data):
    """Parses readlines() data into a table of float values."""
    lines = [list(map(float_or_0, line.split())) for line in data]
    return extend(lines)

def extend(lines):
    """Makes all lists in a list of lists the same length."""
    length = max(map(len, lines))
    fill = [0.0] * len(lines[0][0]) if type(lines[0][0]) is list else 0.0
    return [line + [fill] * (length - len(line)) for line in lines]

#Build a table of floats from stdin and files.
if len(sys.argv) > 1:
    file_data = []
    for name in sys.argv[1:]:
        with open(name) as f:
            file_data.append(parse(f.readlines()))
    data = [list(chain(*row)) for row in zip(*extend(file_data))]
else:
    data = parse(sys.stdin.readlines())

#Rotate & filter out lines that contain only zeroes.
data = filter(lambda l: not 0 == max(l) == min(l), zip(*data))

#Plot the table as a table of lines.
colors = ('k', 'b', 'g', 'r')
dashes = ('-', '--', ':', '-.')
styles = chain(*[[c+d for c in colors] for d in dashes])
for n, (line, style) in enumerate(zip(data, styles)):
    plot.plot(line, style, label='Col ' + str(n)) 
plot.legend()
plot.show()
