# The Good Sleeper Scale-15 items: a questionnaire for the standardised assessment of good sleepers

>*by Manners, J., Appleton, S. L., Reynolds, A. C., Melaku, Y. A., Gill, T. K., Lovato, N., Sweetman, A., Bickley, K., Adams, R., Lack, L., and Scott, H.*

This repository contains scoring codes for the Good Sleeper Scale-15 items. </br>

The manuscript can be found at [doi.org/10.1111/jsr.13717](https://doi.org/10.1111/jsr.13717). </br>
The open-source questionnaire and scoring guide can be found on [osf.io/na6jt](https://osf.io/na6jt/). </br>

---
## Requirements

Requirements can be found in 'requirements.txt', but main packages used are:
- Python 3 
- pandas
- sv-ttk

If you have python installed already, run 'install_requirements.sh' or with the below code to create a virtual environment and install required packages. 
```sh
pip install -r requirements.txt
```

## Usage

Scripts and tkinter GUI has been included to simplify usage. 
If you wish to omit the GUI or implement yourself, the scoring code for GSS-15 can be found in 'python_scoring/gss.py'.

Run using the included 'run.sh' or with the below.
```sh
python python_scoring/python_main.py
```

If you have not already, select 'Create Template' to create a template csv file to input your data and fill this in with your exported data.
The expected format can be found in the section below.

> ### Scoring

Once you have filled in the 'data.csv' template, attach this using 'Select Datafile'.
The window will promptly close and your scored data should be in the same file. New columns will have been added to represent the subdomain and total scores.

> ### Data Formatting

| **px_id**       | **q_1** | **q_2**          | **q_3**          | **q_4**       | **q_5**          | **q_6**          | **q_7**       | **q_8** | **q_9** | **q_10** | **q_11** | **q_12** | **q_13** | **q_14** | **q_15** |
| ----------------- | --------- | ------------------ | ------------------ | --------------- | ------------------ | ------------------ | --------------- | --------- | --------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| _Input Guide_ | _0-2_   | _24H Time (HH:MM)_ | _24H Time (HH:MM)_ | _Hours (HH:MM)_ | _24H Time (HH:MM)_ | _24H Time (HH:MM)_ | _Hours (HH:MM)_ | _0-5_   | _0-3_   | _0-4_    | _0-3_    | _0-3_    | _0-3_    | _0-3_    | _0-3_    |
| exampleid001    | 2       | 21:00            | 7:00             | 9:00          | 22:00            | 8:00             | 8:00          | 1       | 0       | 3        | 0        | 0        | 0        | 0        | 0        |

Where values are integers (e.g., 0-2), it is expected that these coincide with the order of responses in the GSS-15 from top to bottom or left to right.

```python
# For example for question 1 ("Do you think you have a sleep problem?"):
- Yes = 0
- No = 1
- Maybe = 2
```

```python
# Or question 10 ("In general, how often do you get enough sleep to feel your best the next day?"):
- Never = 0
- Rarely = 1
- Sometimes = 2
- Often = 3
- Always = 4
```

## Licence

All source code is made available under a BSD 3-clause license. You may freely use and modify this code, without warranty, so long as you provide attribution to the authors. The manuscript text is not open source. The article's content has been published in the [Journal of Sleep Research](https://onlinelibrary.wiley.com/journal/13652869).

## Citation

> Manners, J., Appleton, S. L., Reynolds, A. C., Melaku, Y. A., Gill, T. K., Lovato, N., Sweetman, A., Bickley, K., Adams, R., Lack, L., & Scott, H. (2022). The Good Sleeper Scale-15 items: a questionnaire for the standardised assessment of good sleepers. Journal of Sleep Research, e13717. https://doi.org/10.1111/jsr.13717