# Biomedical Signal Processing helpers

```
import numpy as np
from scipy import signal, stats
from matplotlib import pyplot as plt

import os
import sys

bme_repo = "https://github.com/jd2504/bme_dsp_2025.git"
repo_name = bme_repo.split('/')[-1].replace('.git', '')
!git clone {bme_repo}
repo_path = os.path.join(os.getcwd(), repo_name)
sys.path.append(repo_path)

import bmedsp_helpers as bme
```
