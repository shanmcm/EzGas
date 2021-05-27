# Project Dashboard

The dashboard collects the key measures about the project.
To be used to control the project, and compare with others. These measures will not be used to graduate the project. <br>
We consider two phases: <br>
-New development: From project start (april 13) to delivery of version 1 fixed (june 9)  <br>
-Maintenance: implementation of CR4 and CR7 (june 9 to end)   <br>
Report effort figures from the timesheet or timesheetCR document, compute size from the source code.

## New development 
| Measure| Value |
|---|---|
|effort E (report here effort in person hours, for New development, from timesheet)  | 320 |
|size S (report here size in LOC of all code written, excluding test cases)  | 1800 |
|productivity = S/E | 5.6 |
|defects after release D (number of defects found running official acceptance tests and fixed in CR0) | 5 |
|defect density = D/S| 0.0027 |
| effort for non-quality ENQ (effort for CR0, or effort to fix defects found running official acceptance tests, from timesheetCR) | 12 |
| effort for non quality, relative = ENQ / E | 0.04 |

## Maintenance

| Measure | Value|
|---|---|
| size S_CR4 = only lines added for CR4 = total size with CR4 - S | 40 |
| actual effort (from timesheetCR) AE_CR4 | 5 |
| productivity P_CR4 = S_CR4/ EA_CR4 | 8 |
| estimated effort (from estimationCR) EE_CR4 | 3 |
|estimation accuracy CR4 = EE_CR4/AE_CR4  | 0.6 |
|||
| size S_CR7 =only lines added for CR7 = total size with CR7 - S | 10 |
| actual effort (from timesheetCR) AE_CR7 | 2 |
| productivity P_CR7 = S_CR7/ AE_CR7 | 5 |
| estimated effort (from estimationCR) EE_CR7 | 5 |
|estimation accuracy CR7 = EE_CR7/AE_CR7  | 2.5 |