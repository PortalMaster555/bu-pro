import ROOT
import time # for random seed
import numpy as np
ROOT.gRandom.SetSeed(int(time.time()))

num2Plot = 10000 # number of points to plot in the circle
rangeMin = 0
rangeMax = 1

width = 800
height = 800

c2 = ROOT.TCanvas("c2", "Quarter Circle", width, height)
x = np.random.random(num2Plot)
y = np.random.random(num2Plot)
scatter = ROOT.TGraph(num2Plot, x, y)

circlepts = 500 # there is likely a better way to make a uniform circle
circlex = np.linspace(rangeMin, rangeMax, circlepts)
circley = np.sqrt(rangeMax**2 - circlex**2)
circleplot = ROOT.TGraph(circlepts, circlex, circley)


circleplot.SetMarkerStyle(21)
circleplot.SetMarkerSize(1)
circleplot.Draw("ap")

scatter.SetMarkerColor(ROOT.kMagenta + 1)
scatter.SetMarkerStyle(21)
scatter.SetMarkerSize(1)
scatter.Draw("p same")


with ROOT.TFile("montecarlo.root", "recreate") as outfile:
    outfile.WriteObject(scatter, "scatter")

magnitudes = np.sqrt(x**2 + y**2)

ct = 0
for mag in magnitudes:
    if mag <= 1:
        ct = ct + 1

frac = ct / num2Plot
area = (rangeMax-rangeMin)**2

true = np.pi/4
quarter_circle_area = frac * area
error = abs(np.pi/4 - frac)/(np.pi/4)
print("Number of scatter points:", scatter.GetN())
print(f"Area: {quarter_circle_area:4.3f}")
print(f"True Area: {true:4.3f}")
print("Error:", f"{100*error:5.3f}%")

c2.cd()
c2.Draw()
c2.Update()
c2.SaveAs("monte_carlo.png")

input() # stop the window from closing