#!/bin/bash
#Trust the notebooks
trustn=$(find . -not -path *.ipynb_checkpoints/*   -name *.ipynb); for i in $trustn; do jupyter trust $i; done
#jupyter notebook --allow-root --no-browser --NotebookApp.iopub_data_rate_limit=100000000
#To run a terminal comment Jupyter and add
/bin/bash
