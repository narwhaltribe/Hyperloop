import numpy as np
import pylab as p

data = np.array([
[0.69999999999999996, 0.70999999999999996, 0.71999999999999997, 0.72999999999999998, 0.73999999999999999, 0.75, 0.76000000000000001, 0.77000000000000002, 0.78000000000000003, 0.79000000000000004, 0.80000000000000004, 0.81000000000000005, 0.82000000000000006, 0.83000000000000007, 0.84000000000000008, 0.85000000000000009, 0.8600000000000001, 0.87000000000000011, 0.88000000000000012, 0.89000000000000012, 0.90000000000000013, 0.91000000000000014, 0.92000000000000015, 0.93000000000000016],
[76.929085596269772, 76.929180655650782, 76.92893154759993, 76.928625174314675, 76.928291042047164, 76.927926280389812, 76.927521921825758, 76.927373426115111, 76.927037462352516, 76.926680093006979, 76.926333125836067, 76.926088498481477, 76.925840539057262, 76.925420446687767, 76.925198202117997, 76.924981707956789, 76.924521823742353, 76.924240953088756, 76.923869718952886, 76.923406601513179, 76.922975652893427, 76.922651164033553, 76.922253692429081, 76.922020448822849],
[156.81475866356442, 163.06699238805285, 169.39639143715658, 176.17567076581227, 183.48993558360036, 191.40688842529258, 200.00123552289159, 209.60446824461877, 220.02372038597602, 231.5065877125065, 244.26303993238952, 258.63028292168445, 274.8267926914944, 292.93901895011976, 313.99136796898489, 338.34220682599886, 366.45335097633716, 400.29991204459554, 441.91861153248129, 491.97554075197723, 557.62439932580014, 646.71530896872468, 776.45804066298967, 992.88105048682928],
])

p.plot(data[0],data[2]/data[1])
p.show()