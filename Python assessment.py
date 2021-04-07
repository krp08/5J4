1.Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution 
Source code:=
import numpy as np
rand_num = np.random.normal(0,1,15)
print("15 random numbers from a standard normal distribution:")
print(rand_num)

Output:=
15 random numbers from a standard normal distribution:
[ 0.42690788  1.81615544  0.36591912 -0.41417837 -1.13061369 -1.31777265
  0.03659045  0.60765805 -0.2148491   0.25934697 -0.89221431  0.33059367
 -0.59079163  0.29665161 -0.2753327 ]

2.Create an array of 20 linearly spaced points between 0 and 1 
Source Code:=

import numpy as np
 np.linspace(1, 10)

Output:=
array([ 1.        ,  1.18367347,  1.36734694,  1.55102041,  1.73469388,
        1.91836735,  2.10204082,  2.28571429,  2.46938776,  2.65306122,
        2.83673469,  3.02040816,  3.20408163,  3.3877551 ,  3.57142857,
        3.75510204,  3.93877551,  4.12244898,  4.30612245,  4.48979592,
        4.67346939,  4.85714286,  5.04081633,  5.2244898 ,  5.40816327,
        5.59183673,  5.7755102 ,  5.95918367,  6.14285714,  6.32653061,
        6.51020408,  6.69387755,  6.87755102,  7.06122449,  7.24489796,
        7.42857143,  7.6122449 ,  7.79591837,  7.97959184,  8.16326531,
        8.34693878,  8.53061224,  8.71428571,  8.89795918,  9.08163265,
        9.26530612,  9.44897959,  9.63265306,  9.81632653, 10.        ])



3. declare a numpy array of values from 1 to 100 and make it into a 10*10 matrix. 
Source Code:=
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr)

Output:=
[[  1   2   3   4   5   6   7   8   9  10]
 [ 11  12  13  14  15  16  17  18  19  20]
 [ 21  22  23  24  25  26  27  28  29  30]
 [ 31  32  33  34  35  36  37  38  39  40]
 [ 41  42  43  44  45  46  47  48  49  50]
 [ 51  52  53  54  55  56  57  58  59  60]
 [ 61  62  63  64  65  66  67  68  69  70]
 [ 71  72  73  74  75  76  77  78  79  80]
 [ 81  82  83  84  85  86  87  88  89  90]
 [ 91  92  93  94  95  96  97  98  99 100]]


4.using the previously defined matrix print rows 1,5,6 
Source Code:=
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr[1])
print(arr[5])
print(arr[6])

Output:=
[11 12 13 14 15 16 17 18 19 20]
[51 52 53 54 55 56 57 58 59 60]
[61 62 63 64 65 66 67 68 69 70]

5.using the previously defined matrix print elemnts from 3rd row to 10th row 
Source Code:=
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr[3:11])

Output:=
[[ 31  32  33  34  35  36  37  38  39  40]
 [ 41  42  43  44  45  46  47  48  49  50]
 [ 51  52  53  54  55  56  57  58  59  60]
 [ 61  62  63  64  65  66  67  68  69  70]
 [ 71  72  73  74  75  76  77  78  79  80]
 [ 81  82  83  84  85  86  87  88  89  90]
 [ 91  92  93  94  95  96  97  98  99 100]]

6.using the previously defined matrix print all elemtnts from 4th column to 8th column
Source Code:=
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr[4:9])

Output:=
[[41 42 43 44 45 46 47 48 49 50]
 [51 52 53 54 55 56 57 58 59 60]
 [61 62 63 64 65 66 67 68 69 70]
 [71 72 73 74 75 76 77 78 79 80]
 [81 82 83 84 85 86 87 88 89 90]]

7. using the same matrix print values from 3rd row 2nd coumn to 5th row 8th column 
Source Code:=
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr[3:6,2:9])

Output:=
[[33 34 35 36 37 38 39]
 [43 44 45 46 47 48 49]
 [53 54 55 56 57 58 59]]

8.write a code to generate a 1000 random numbers each in the range(0,1) such that the count of all random points like are almost
 same . 
Source Code:=
from random import seed
from random import randint
seed(1)
for _ in range(10):
	value = randint(0, 10)
	print(value)

Output:=
2
9
1
4
1
7
7
7
10
6

9.write the commands to get standard deviation, mean ,mode,median for a given vector
Source Code:=
>>> import statistics

>>> statistics.mean([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])
5.2


>>> import statistics

>>> statistics.median([3, 5, 1, 4, 2])
3


>>> import statistics

>>> statistics.mode([4, 1, 2, 2, 3, 5])
2
