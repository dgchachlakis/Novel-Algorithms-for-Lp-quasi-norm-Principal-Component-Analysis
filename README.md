## Novel-Algorithms-for-Lp-quasi-norm-Principal-Component-Analysis

In this repo we implent the algorithms of [[1]](https://ieeexplore.ieee.org/document/9287335) for computing one or more Lp-norm Principal-Components of a matrix. 

* For any $p\leq 1$, algorithm 1 (```biftlipping.py```) approximates the exact solution to 
![equation](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cfn_cm%20%5CLARGE%20%5Cunderset%7B%5Cmathbf%20q%20%5Cin%20%5Cmathbb%20R%5ED%7E%3B%7E%5C%7C%5Cmathbf%20q%5C%7C_2%3D1%7D%7B%5Ctext%7Bmax.%7D%7D%5Cleft%5C%7C%5Cmathbf%20X%5E%5Ctop%5Cmathbf%20q%5Cright%5C%7C_p%5Ep.)

* Further, for any $p\leq 1$, algorithm 2 (```biftlipping_deflation.py```) approximates a solution to 
![equation](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cfn_cm%20%5CLARGE%20%5Cunderset%7B%5Cmathbf%20Q%20%5Cin%20%5Cmathbb%20R%5E%7BD%20%5Ctimes%20K%7D%7E%3B%7E%5Cmathbf%20Q%5E%5Ctop%5Cmathbf%20Q%3D%5Cmathbf%20I_K%7D%7B%5Ctext%7Bmax.%7D%7D%5Cleft%5C%7C%5Cmathbf%20X%5E%5Ctop%5Cmathbf%20Q%5Cright%5C%7C_p%5Ep.)

---
* IEEEXplore article: https://ieeexplore.ieee.org/document/9287335
* Source code: 
---
**Questions/issues**

Inquiries regarding the scripts provided below are cordially welcome. In case you spot a bug, please let me know. If you use some piece of code for your own work, please cite the article above.

---
**Citing**

If you use our algorihtms, please cite [[1]](https://ieeexplore.ieee.org/document/9287335).
```
@INPROCEEDINGS{9287335,
  author={D. G. {Chachlakis} and P. P. {Markopoulos}},
  booktitle={2020 28th European Signal Processing Conference (EUSIPCO)}, 
  title={Novel Algorithms for Lp-Quasi-Norm Principal-Component Analysis}, 
  year={2021},
  volume={},
  number={},
  pages={1045-1049},
  doi={10.23919/Eusipco47968.2020.9287335}}
```
|[[1]](https://ieeexplore.ieee.org/document/9287335)|D. G. Chachlakis and P. P. Markopoulos, "Novel Algorithms for Lp-Quasi-Norm Principal-Component Analysis," 2020 28th European Signal Processing Conference (EUSIPCO), Amsterdam, 2021, pp. 1045-1049, doi: 10.23919/Eusipco47968.2020.9287335.|
|-----|--------|