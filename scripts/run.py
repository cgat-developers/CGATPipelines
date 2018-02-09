#!/bin/env python
'''run.py - wrapper around command line
====================================


Purpose
-------

This script is a generic wrapper for tools with a command line
interface.  The wrapper records execution times and logs successfull
completion of the command.

Usage
-----

For example, typing::

   python run.py ls

will output the results of running the command with an additional header and footer.
Both are prefixed by ``#`` to mark them as comments::

  # output generated by ../scripts/run.py ls
  # job started at Mon Sep 14 17:00:05 2015 on cgat150.anat.ox.ac.uk -- 1bbb4ad7-c20b-4259-9dee-df2ad69d197f
  # pid: 4477, system: Linux 2.6.32-573.3.1.el6.x86_64 #1 SMP Mon Aug 10 09:44:54 EDT 2015 x86_64
  # loglevel                                : 1
  # random_seed                             : None
  # short_help                              : None
  # stderr                                  : <open file \'<stderr>\', mode \'w\' at 0x2b681cafa1e0>
  # stdin                                   : <open file \'<stdin>\', mode \'r\' at 0x2b681cafa0c0>
  # stdlog                                  : <open file \'<stdout>\', mode \'w\' at 0x2b681cafa150>
  # stdout                                  : <open file \'<stdout>\', mode \'w\' at 0x2b681cafa150>
  # timeit_file                             : None
  # timeit_header                           : None
  # timeit_name                             : all
  BuildingPipelines.rst  InstallingPipelines.rst  PipelineReports.rst      Reference.rst  UsingPipelines.rst  _static     cgatreport.log  conf.py       images     modules      out           pipelinemodules  plots   scripts
  CGATPipelines.rst      Makefile                 PipelinesBackground.rst  Release.rst    _build              _templates  collect.py      glossary.rst  index.rst  modules.rst  pipeline.log  pipelines        python  scripts.rst
  # job finished in 0 seconds at Mon Sep 14 17:00:05 2015 --  0.06  0.05  0.00  0.01 -- 1bbb4ad7-c20b-4259-9dee-df2ad69d197f

The header contains information about:

* the command line of the job
* the time when the job was started (``Thu Mar 29 13:06:33 2012``)
* the location it was executed (``cgat150.anat.ox.ac.uk``)
* a unique job id (``e1c16e80-03a1-4023-9417-f3e44e33bdcd``)
* the pid of the job (``16649``)
* the system specification (``Linux 2.6.32-220.7.1.el6.x86_64 #1
      SMP Fri Feb 10 15:22:22 EST 2012 x86_64``)

The footer contains information about:

* the job has finished (``job finished``)
* the time it took to execute (``11 seconds``)
* when it completed (``Thu Mar 29 13:06:44 2012``)
* some benchmarking information (``11.36 0.45 0.00 0.01``) which is
  ``user time``, ``system time``, ``child user time``, ``child system
  time``.
* the unique job id (``e1c16e80-03a1-4023-9417-f3e44e33bdcd``)

The unique job id can be used to easily retrieve matching information
from a concatenation of log files.

Type::

   python run.py --help

for command line help.

Command line options
--------------------

'''

import os
import sys
import subprocess
import CGATCore.Experiment as E


def main(argv=None):
    """script main.

    parses command line options in sys.argv, unless *argv* is given.
    """

    if argv is None:
        argv = sys.argv

    parser = E.OptionParser(version="%prog version: $Id$",
                            usage=globals()["__doc__"])

    # stop parsing options at the first argument
    parser.disable_interspersed_args()

    (options, args) = E.Start(parser,
                              add_pipe_options=True)

    if len(args) > 0:

        cmd = args[0]
        if len(args) > 1:
            cmd += " '" + "' '".join(args[1:]) + "'"

        s = subprocess.Popen(cmd,
                             shell=True,
                             cwd=os.getcwd(),
                             close_fds=True)

        (out, err) = s.communicate()
        returncode = s.returncode
    else:
        returncode = 0

    E.Stop()

    sys.exit(returncode)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
