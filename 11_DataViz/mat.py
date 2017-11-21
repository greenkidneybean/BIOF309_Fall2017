import numpy as np
import matplotlib.pyplot as plt

###random sampling in numpy to create data
x1 = np.random.uniform(0,1,10000)
x2 = np.random.normal(0, 1, 10000)
x3 = np.random.poisson(2, 10000)

#Histograms help you visualize what it looks like to randomly sample from different distributions
plt.hist(x1)
plt.show()
#add bins
plt.hist(x1, 100)
plt.show()
plt.hist(x2, 100)
plt.show()
plt.hist(x3, 100)
plt.show()

#You can do a scatter plot too
plt.plot(np.random.normal(0, 1, 1000), np.random.normal(0, 1, 1000), "g.")
plt.title("Independent Gaussians")
plt.xlabel("First Random Var")
plt.ylabel("Second Random Var")
plt.show()

#ion makes it so you don't have to do plt.show()
plt.ion()
#ioff()  undoes it
plt.ioff()
#I like plt.ion()
plt.ion()

#How to make a QQ plot
LMDA = 1000.
xn1 = np.random.poisson(LMDA, 10000) #poisson with lambda = 1000
xn2 = np.random.normal(LMDA, np.sqrt(LMDA), 10000) #approximate it with a gaussian
#sort your data
xn1.sort()
xn2.sort()
#scatter plot sorted data
plt.plot(xn1, xn2, "b.")
#plot a line with slope of 1 for perspective
m1 = np.min(np.concatenate([xn1, xn2]))
m2 = np.max(np.concatenate([xn1, xn2]))
plt.plot([m1, m2], [m1, m2], "r", linestyle = "dashed")

#Look at the histograms on top of one another
fig, (ax1, ax2) = plt.subplots(1,2, sharex = True)
ax1.hist(xn1, 100)
ax2.hist(xn2, 100)
ax1.set_title("Poisson")
ax2.set_title("Gaussian")

#Exercise
x4 = np.random.normal(10, 2, 10000)
x5 = np.random.normal(0, 1, 10000)
#transform x5 so it looks like x4
#check your results with a QQ plot
#check again by creating histograms of each in a subplot
#measure the means and standard deviations of each distribution to see if they are similar
