import driver as d
from mpi4py import MPI
import predictor as p
import numpy as np
import pandas as pd

comm = MPI.COMM_WORLD
groups = ["zlib", "rp", "ppmd", "zlib_rp_ppmd"]
filename = "m4c_quarterly_data.txt"
results = d.forecast_multialphabet_from_file(comm, filename, groups, sparse=2, quants_count=16,
                                             difference=1, smooth_func=d.smooth_m3c)

if comm.Get_rank() == 0:
    print(filename)
    for group in groups:
        print('-'*20 + ' ' + group + ' ' + '-'*20 + '\n')
        for result in results:
            print(str(result[0]) + ' ' + ' '.join(map(str, result[1][group])))
