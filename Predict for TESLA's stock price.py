Python 3.10.1 (v3.10.1:2cd268a3a9, Dec  6 2021, 14:28:59) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Plot the scatter graphic
import matplotlib.pyplot as plt

#TESLA stock price from 3/14/2022 to 4/13/2022
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22]
y = [981.08,997.64,980.4,1043.21,1052.39,1073.47,1136.3,1089.38,1081.15,1094.57,1091.17,1107.99,1065.1,1008,1009.73,979.94,930,914.98,874.49,830.99,809,775.27,780.61]
y.reverse()

plt.scatter(x, y)
plt.show()

#Plot the linear regression line
#use Scipy

from scipy import stats
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

#Predict for Tesla’s stock price for the next three months

#Predict Data
x=list(range(120))
y2=[]

#Original data
x0= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22]
y0= [981.08,997.64,980.4,1043.21,1052.39,1073.47,1136.3,1089.38,1081.15,1094.57,1091.17,1107.99,1065.1,1008,1009.73,979.94,930,914.98,874.49,830.99,809,775.27,780.61]
y0.reverse()

slope=11.608893280632337
intercept=859.5569565217401 

for i in x:
    y=slope*i+intercept
    y2.append(y)
    

Stock_fig = plt.figure()

SF = Stock_fig.add_subplot(1, 1, 1)  
SF.scatter(x, y2,s=1, color = 'blue')
SF.scatter(x0, y0,s=1, color = 'red')
SF.set_title('Predict for Tesla’s stock price for the next three months')
plt.show()