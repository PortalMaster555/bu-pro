import ROOT
import time # for random seed
ROOT.gRandom.SetSeed(int(time.time()))

num2Plot = 100000
rangeMin=0
rangeMax=1
nBins = 10
h1d = ROOT.TH1D("h1d", "Uniform Distribution", nBins, rangeMin, rangeMax)
h1d.SetFillColor(ROOT.kMagenta + 1)

# this works, but it's not very elegant
# for i in range(num2Plot):
#     x = ROOT.gRandom.Uniform(rangeMin, rangeMax)
#     h1d.Fill(x)
#     # print(x)

uniformFunction = ROOT.TF1("uniformFunction", "1", 0, 1)
h1d.FillRandom("uniformFunction", num2Plot)

width = 1000
height = 800
c1 = ROOT.TCanvas("c1", "Histogram", width, height)
h1d.SetMinimum(0) # !!! no wonder my plot didn't look uniform!
ROOT.gStyle.SetOptStat(0) # get rid of that little box
h1d.Draw()
c1.Update()
with ROOT.TFile("histogram_uniform.root", "recreate") as outfile:
    outfile.WriteObject(h1d, "histogram")
c1.SaveAs("histogram_uniform.png")
input() # stop the window from closing