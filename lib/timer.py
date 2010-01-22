# TAMkin is a post-processing toolkit for thermochemistry and kinetics analysis.
# Copyright (C) 2008-2010 Toon Verstraelen <Toon.Verstraelen@UGent.be>,
# Matthias Vandichel <Matthias.Vandichel@UGent.be> and
# An Ghysels <An.Ghysels@UGent.be>, Center for Molecular Modeling (CMM), Ghent
# University, Ghent, Belgium; all rights reserved unless otherwise stated.
#
# This file is part of TAMkin.
#
# TAMkin is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# In addition to the regulations of the GNU General Public License,
# publications and communications based in parts on this program or on
# parts of this program are required to cite the following five articles:
#
# "Vibrational Modes in partially optimized molecular systems.", An Ghysels,
# Dimitri Van Neck, Veronique Van Speybroeck, Toon Verstraelen and Michel
# Waroquier, Journal of Chemical Physics, Vol. 126 (22): Art. No. 224102, 2007
# DOI:10.1063/1.2737444
#
# "Cartesian formulation of the Mobile Block Hesian Approach to vibrational
# analysis in partially optimized systems", An Ghysels, Dimitri Van Neck and
# Michel Waroquier, Journal of Chemical Physics, Vol. 127 (16), Art. No. 164108,
# 2007
# DOI:10.1063/1.2789429
#
# "Calculating reaction rates with partial Hessians: validation of the MBH
# approach", An Ghysels, Veronique Van Speybroeck, Toon Verstraelen, Dimitri Van
# Neck and Michel Waroquier, Journal of Chemical Theory and Computation, Vol. 4
# (4), 614-625, 2008
# DOI:10.1021/ct7002836
#
# "Mobile Block Hessian approach with linked blocks: an efficient approach for
# the calculation of frequencies in macromolecules", An Ghysels, Veronique Van
# Speybroeck, Ewald Pauwels, Dimitri Van Neck, Bernard R. Brooks and Michel
# Waroquier, Journal of Chemical Theory and Computation, Vol. 5 (5), 1203-1215,
# 2009
# DOI:10.1021/ct800489r
#
# "Normal modes for large molecules with arbitrary link constraints in the
# mobile block Hessian approach", An Ghysels, Dimitri Van Neck, Bernard R.
# Brooks, Veronique Van Speybroeck and Michel Waroquier, Journal of Chemical
# Physics, Vol. 130 (18), Art. No. 084107, 2009
# DOI:10.1063/1.3071261
#
# TAMkin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --

import time, sys

__all__ = ["Timer"]

class Timer(object):
    """ Timer object which serves to keep track of timings.
    When sampling:
    - CPU times are obtained with time.time()
    - WALL times are obtained with time.clock()
    - a label can be added
    """
    def __init__(self):
        self.cpu_times = []
        self.wall_times = []
        self.labels = []

    def sample(self,label):
        self.cpu_times.append(time.clock())
        self.wall_times.append(time.time())
        self.labels.append(label)

    def dump(self, f=sys.stdout):
        """Dump the logfile with timing information, to screen or to a file stream.
        Optional argument:
             f  --  the stream to write to. [default=sys.stdout]
        """
        print >> f, "-------------------"
        print >> f, "Printing LOG jobtimer"
        print >> f, '%12s %12s %21s %16s %30s' %("cpu times [s]", "diff [s]", "wall times [s]", "diff [s]", "labels" )
        for i,label in enumerate(self.labels[:-1]):
            print >> f, '%12.3f %12.3f %21.3f %16.3f %30s' %(self.cpu_times[i],
                                         self.cpu_times[i+1]-self.cpu_times[i],
                                         self.wall_times[i],
                                         self.wall_times[i+1]-self.wall_times[i],
                                         label)
        print >> f, '%12.3f %12s %21.3f %16s %30s' %(self.cpu_times[-1], "",
                                         self.wall_times[-1], "",
                                         self.labels[-1])
        print >> f, "-------------------"

    def write_to_file(self, filename):
        """Write the logfile with timing information to filename."""
        f = file(filename, 'w')
        self.dump(f)
        f.close()
