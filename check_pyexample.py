import sys
import matplotlib
matplotlib.use('agg')

import pyexample
status = pyexample.test(*sys.argv[1:])
sys.exit(status)
