# -*- coding: utf-8 -*-
#
#   pyhwp : hwp file format parser in python
#   Copyright (C) 2010-2012 mete0r <mete0r@sarangbang.or.kr>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import with_statement
import logging


logger = logging.getLogger(__name__)

executable = 'xsltproc'
enabled = None


def xslt_reachable():
    from subprocess import Popen
    args = [executable, '--version']
    try:
        p = Popen(args)
    except:
        return False
    else:
        p.wait()
        return True


def is_enabled():
    global enabled
    if enabled is None:
        enabled = xslt_reachable()
    return enabled


def enable():
    global enabled
    enabled = True


def disable():
    global enabled
    enabled = False


def xslt(xsl_path, inp_path, out_path):
    from subprocess import Popen
    args = [executable, '-o', out_path, xsl_path, inp_path]
    p = Popen(args)
    p.wait()
    if p.returncode == 0:
        return dict()
    else:
        return dict(errors=[])
