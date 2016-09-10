import ROOT as r
import sys
#import CMS_lumi
outf = r.TFile('PlotCanvas.root','RECREATE')
blind=False
def makePlot():

#these values are for 
  modelname="D5"
  luminosity="3000fb"
  lam=10000
  power=2
  
#  CMS_lumi.lumi_13TeV = ""
#  CMS_lumi.writeExtraText = 1
  #CMS_lumi.extraText = "Model: "+modelname
  iPos=33
  
  canv = r.TCanvas()
  canv.Clear()
  canv.SetLogy(False)
  canv.SetLogx(False)
  canv.SetBottomMargin(.13)
  canv.SetLeftMargin(.12)
  canv.SetRightMargin(.05)
  mg = r.TMultiGraph()
  leg = r.TLegend(0.79, 0.70, 0.95, 0.89)
  leg.SetFillStyle(0)
  leg.SetBorderSize(0)
  leg.SetTextFont(62)
  leg.SetTextSize(0.05)

  dummyHist = r.TH1D("dummy","",1,10,100)
  # make text box
  lat = r.TLatex()
  lat.SetNDC()
  lat.SetTextFont(42);

  lat2 = r.TLatex()
  lat2.SetNDC()
  lat2.SetTextSize(0.04)
  lat2.SetTextFont(42);

  # get the data 
  tf = [0] * len(sys.argv)
  tree = [0] * len(sys.argv)
  values = [0] * len(sys.argv)
  graph = [0] * len(sys.argv)
  exp = [0] * len(sys.argv)
  oneSigma = [0] * len(sys.argv)
  twoSigma = [0] * len(sys.argv)
  for k in range(len(sys.argv)-1):
    print "Index: "+str(k)
    tf[k] = r.TFile(sys.argv[k+1])
    tree[k] = tf[k].Get('limit')
    values[k]=[]
    for i in range(tree[k].GetEntries()):
        tree[k].GetEntry(i)
        values[k].append([tree[k].mh, tree[k].limit])
    values[k].sort(key=lambda x: x[0])
    print values[k]
    # make graph from values
    graph[k] = r.TGraphAsymmErrors()
    exp[k] = r.TGraphAsymmErrors()
    oneSigma[k] = r.TGraphAsymmErrors()
    twoSigma[k] = r.TGraphAsymmErrors()

    point_counter=0
    for j in range(len(values[k])):
        if (j%6==0):
          mh = values[k][j][0]
          down95 = values[k][j][1]
          down68 = values[k][j+1][1]
          median = values[k][j+2][1]
          up68 = values[k][j+3][1]
          up95 = values[k][j+4][1]
          obs = values[k][j+5][1]

          # transformation
          down95 = lam*down95**(-1./power)
          down68 = lam*down68**(-1./power)
          median = lam*median**(-1./power)
          up95 = lam*up95**(-1./power)
          up68 = lam*up68**(-1./power)
          print down95
          
          exp[k].SetLineStyle(1)
          exp[k].SetLineWidth(3)
   
          # add to graph in the same way as before
          exp[k].SetPoint(point_counter, mh, median)
          oneSigma[k].SetPoint(point_counter,mh,median)
          oneSigma[k].SetPointError(point_counter,0,0,abs(median-down68),abs(up68-median))
          twoSigma[k].SetPoint(point_counter,mh,median)
          twoSigma[k].SetPointError(point_counter,0,0,abs(median-down95),abs(up95-median))
          point_counter+=1

    
    oneSigma[k].SetLineColor(r.kGreen)
    twoSigma[k].SetLineColor(r.kYellow)
    oneSigma[k].SetFillColor(r.kGreen)
    twoSigma[k].SetFillColor(r.kYellow)

    mg.Add(exp[k])
    mg.Draw("AXIS")

  
  # draw dummy hist and multigraph
  mg.GetXaxis().SetTitleOffset(1.2)
  mg.GetYaxis().SetTitleOffset(1.2)
  mg.GetXaxis().SetTitle('m_{#chi} [GeV]')
  mg.GetYaxis().SetTitle('#Lambda [GeV]')
  dummyHist.SetMinimum(1)
  dummyHist.SetMaximum(mg.GetYaxis().GetXmax())
  dummyHist.SetLineColor(0)
  dummyHist.SetStats(0)
  dummyHist.Draw("AXIS")
  mg.Draw("AL") 
 
#  CMS_lumi.CMS_lumi(canv, 4, iPos)
  # draw legend
  dummy3000 = r.TGraphAsymmErrors()
  dummy3000.SetLineColor(r.kBlack)
  dummy3000.SetLineStyle(1)
  dummy3000.SetLineWidth(3)
  dummy300 = r.TGraphAsymmErrors()
  dummy300.SetLineColor(r.kBlack)
  dummy300.SetLineStyle(7)
  dummy300.SetLineWidth(3)
  dummy20 = r.TGraphAsymmErrors()
  dummy20.SetLineColor(r.kBlack)
  dummy20.SetLineStyle(3)
  dummy20.SetLineWidth(3)
  #leg.SetHeader('95% CL')
  leg.AddEntry(dummy3000,'3000fb^{-1}','L')
  leg.Draw()
  canv.RedrawAxis()

  # print canvas
  canv.Update()
  canv.Print(modelname+"_limit.pdf")
  outf.cd()
  canv.SetName("limit_cavas")
  canv.Write()

makePlot()
