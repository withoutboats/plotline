#plotline 1.0

plotline is a simple tool for visualizing data as a line graph. Several times
I have had some data that I just wanted to see plotted; wrather than wrangling
with gnuplot every time, I wrote this simple script.

plotline can open any number of files or data can be piped into it. It will
display up to sixteen lines labelled by their column number from left to right.
These are displayed however matplotlib.pyplot's show function displays data
from your editing environment (from my xterm console, it opens a new window).

###Example

> ping 8.8.8.8 -c 100 | head -101 | tail -100 | cut -d "=" -f 4 | plotline

This will ping 8.8.8.8 one hundred times and then display the value of ping's
time field as a line graph.

###Input format

plotline does very little input validation. It treats space-separated values
as numeric data; if it cannot convert them to floats, it replaces them with 0s.
plotline will fill 0s in columns which do not cover the same range as the
longest column; if input is given from multiple files, it will assume that each
file's first lines should be aligned.

If all the values in a column are zero (most likely because it contained
non-numeric data), that column will not be included in the output.

###Other Notes

plotline is written in Python 3 and dependent on matplotlib; it is licensed
under the GNU General Public License, version 3+.
