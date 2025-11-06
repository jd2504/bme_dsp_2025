# Biomedical Signal Processing helpers
Joel Deerwester
CCNY BME (Lucas Parra, 2025)

## Links and resources
ParraLab, BME DSP [site](https://www.parralab.org/teaching/biomed-dsp/)
EPFL DSP course [Coursera](https://www.coursera.org/specializations/digital-signal-processing)
MIT OpenCourseWare [resources](https://ocw.mit.edu/courses/res-6-008-digital-signal-processing-spring-2011/)
MathWorks CVE [course](https://www.coursera.org/professional-certificates/mathworks-computer-vision-engineer)
Bruce [text](https://www.amazon.com/Biomedical-Signal-Processing-Modeling/dp/0471345407)

## A few biomed DSP helper functions

### Import
```
import os
import sys

bme_repo = "https://github.com/jd2504/bme_dsp_2025.git"
repo_name = bme_repo.split('/')[-1].replace('.git', '')
!git clone {bme_repo}
repo_path = os.path.join(os.getcwd(), repo_name)
sys.path.append(repo_path)

import bmedsp_helpers as bme
```

### Methods

- `bme.grab_mat()`
- `bme.grab_wav`
- `gaborfir(fc, fs, Q)`

E.g.:
```
file_input = bme.grab_mat('spike.mat')
x = file_input['x']
```
