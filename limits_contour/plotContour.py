#!/usr/bin/env python
"""
python plotMultiOffShell.py 40x40_300fb_mha/gridinfosystlumiscale.txt 40x40_3000fb_mha/gridinfosystlumiscale.txt
"""
import ROOT as r
import sys
#import CMS_lumi
import math as m
import numpy as np
from array import array
import random
from array import array

col_store=[]
def CreateTransparentColor(color, alpha):
  adapt   = r.gROOT.GetColor(color)
  new_idx = r.gROOT.GetListOfColors().GetSize() + 1
  trans = r.TColor(new_idx, adapt.GetRed(), adapt.GetGreen(), adapt.GetBlue(), '', alpha)
  col_store.append(trans)
  trans.SetName('userColor%i' % new_idx)
  return new_idx

def fillTH2(hist2d, graph):
    for x in xrange(1, hist2d.GetNbinsX()+1):
        for y in xrange(1, hist2d.GetNbinsY()+1):
            xc = hist2d.GetXaxis().GetBinCenter(x)
            yc = hist2d.GetYaxis().GetBinCenter(y)
            val = graph.Interpolate(xc, yc)
            hist2d.SetBinContent(x, y, val)

def makeHist(name, xbins, ybins, graph2d):
    len_x = graph2d.GetXmax() - graph2d.GetXmin()
    binw_x = (len_x * 0.5 / (float(xbins) - 1.)) - 1E-5
    len_y = graph2d.GetYmax() - graph2d.GetYmin()
    binw_y = (len_y * 0.5 / (float(ybins) - 1.)) - 1E-5
    hist = r.TH2F(name, '', xbins, graph2d.GetXmin()-binw_x, graph2d.GetXmax()+binw_x, ybins, graph2d.GetYmin()-binw_y, graph2d.GetYmax()+binw_y)
    return hist

def OnePad():
    pad = r.TPad('pad', 'pad', 0., 0., 1., 1.)
    pad.Draw()
    pad.cd()
    result = [pad]
    return result

def frameTH2D(hist, threshold, mult = 1.0,frameValue=1000):
  # NEW LOGIC:
  #   - pretend that the center of the last bin is on the border if the frame
  #   - add one tiny frame with huge values
  #frameValue = 1000
  # if (TString(in->GetName()).Contains("bayes")) frameValue = -1000;

  xw = hist.GetXaxis().GetBinWidth(1)
  yw = hist.GetYaxis().GetBinWidth(1)

  nx = hist.GetNbinsX()
  ny = hist.GetNbinsY()

  x0 = hist.GetXaxis().GetXmin()
  x1 = hist.GetXaxis().GetXmax()

  y0 = hist.GetYaxis().GetXmin()
  y1 = hist.GetYaxis().GetXmax()
  xbins = array('d', [0]*999)
  ybins = array('d', [0]*999)
  eps = 0.1
  # mult = 1.0

  xbins[0] = x0 - eps * xw - xw * mult
  xbins[1] = x0 + eps * xw - xw * mult
  for ix in xrange(2, nx+1): xbins[ix] = x0 + (ix - 1) * xw
  xbins[nx + 1] = x1 - eps * xw + 0.5 * xw * mult
  xbins[nx + 2] = x1 + eps * xw + xw * mult

  ybins[0] = y0 - eps * yw - yw * mult
  ybins[1] = y0 + eps * yw - yw * mult
  for iy in xrange(2, ny+1): ybins[iy] = y0 + (iy - 1) * yw
  ybins[ny + 1] = y1 - eps * yw + yw * mult
  ybins[ny + 2] = y1 + eps * yw + yw * mult

  framed = r.TH2D('%s framed' % hist.GetName(), '%s framed' % hist.GetTitle(), nx + 2, xbins, ny + 2, ybins)

  # Copy over the contents
  for ix in xrange(1, nx+1):
    for iy in xrange(1, ny+1):
      framed.SetBinContent(1 + ix, 1 + iy, hist.GetBinContent(ix, iy))


  # Frame with huge values
  nx = framed.GetNbinsX()
  ny = framed.GetNbinsY()
  for ix in xrange(1, nx+1):
    framed.SetBinContent(ix, 1, frameValue)
    framed.SetBinContent(ix, ny, frameValue)

  for iy in xrange(2, ny):
    framed.SetBinContent(1, iy, frameValue)
    framed.SetBinContent(nx, iy, frameValue)

  return framed

def contourFromTH2(h2in, threshold, minPoints=10, mult = 1.0, smoothN = 0):
  # std::cout << "Getting contour at threshold " << threshold << " from "
  #           << h2in->GetName() << std::endl;
  # // http://root.cern.ch/root/html/tutorials/hist/ContourList.C.html

  contoursList = [threshold]
  contours = array('d', contoursList)
  if (h2in.GetNbinsX() * h2in.GetNbinsY()) > 10000: minPoints = 50
  if (h2in.GetNbinsX() * h2in.GetNbinsY()) <= 100: minPoints = 10

  #h2 = h2in.Clone()
  h2 = frameTH2D(h2in, threshold, mult)

  for i in range(smoothN):
    h2.Smooth(1, "k5b")
  
  h2.SetContour(1, contours)

  # Draw contours as filled regions, and Save points
  backup = r.gPad
  canv = r.TCanvas('tmp', 'tmp')
  canv.cd()
  h2.Draw('CONT Z LIST')
  r.gPad.Update() # Needed to force the plotting and retrieve the contours in

  conts = r.gROOT.GetListOfSpecials().FindObject('contours')
  contLevel = None

  if conts is None or conts.GetSize() == 0:
    print '*** No Contours Were Extracted!'
    return None
  ret = r.TList()
  for i in xrange(conts.GetSize()):
    contLevel = conts.At(i)
    print 'Contour %d has %d Graphs\n' % (i, contLevel.GetSize())
    for j in xrange(contLevel.GetSize()):
      gr1 = contLevel.At(j)
      print'\t Graph %d has %d points' % (j, gr1.GetN())
      if gr1.GetN() > minPoints: ret.Add(gr1.Clone())
      # // break;
  backup.cd()
  return ret


outf = r.TFile('PlotCanvas.root','RECREATE')
def makePlot():

  contours = []

  for k in range(len(sys.argv)-1):
    infile = open(sys.argv[k+1],"r")
    filestoread=infile.readlines()
    yvalues=[]
    for i in range(len(filestoread)):
      thisline=filestoread[i].split()
#      yvalues.append([10**(float(thisline[0])),thisline[1]])
      yvalues.append([float(thisline[0]),thisline[1]])
    yvalues.sort(key=lambda x: float(x[0]))

    #loop over y values getting tfiles and extracting x values and limits
    medianvalues=[]
    ybincenters=[]
    xbincenters=[]
    for i in range(len(yvalues)):
      ybincenters.append(float(yvalues[i][0]))
      tf = r.TFile(yvalues[i][1])
      tree = tf.Get('limit')
      xvalues=[]
      for j in range(tree.GetEntries()):
        tree.GetEntry(j)
        xvalues.append([tree.mh, tree.limit])
      xvalues.sort(key=lambda x: float(x[0]))
      print xvalues
        
      if len(xvalues) != 6*40:  # TODO: check the number!
        xs = []
        for item in xvalues:
          if item[0] not in xs: xs.append(item[0])

        # get how many of them are there in the list
        for x in xs:
          check = [item for item in xvalues if x in item]
          if i==0:
            xbincenters.append(x)
          # if there are less than 6 then add stuff
          for index in range(6-len(check)):
            xvalues.append([x, 10000+random.random()])
    
      # get limits for all x values for this y value
      for j in range(len(xvalues)):
        if (j%6==0):
          if len(xvalues)>j+2 : medianvalues.append([xvalues[j][0],yvalues[i][0],xvalues[j+2][1]])
          else : medianvalues.append([xvalues[j][0],yvalues[i][0],10000])

    graph_exp=r.TGraph2D()

    #Populate TGraph with points
    n=0
    for j in range(len(ybincenters)):
      for i in range(len(xbincenters)):
        graph_exp.SetPoint(n,xbincenters[i],ybincenters[j],medianvalues[j*len(xbincenters)+i][2])
        n=n+1

    #Make histogram out of TGraph
#    axis = r.TH2D('hist2d','', len(xbincenters), graph_exp.GetXmin(), graph_exp.GetXmax(), len(ybincenters), graph_exp.GetYmin(), graph_exp.GetYmax())
    axis = r.TH2D('hist2d','', len(xbincenters), 0, graph_exp.GetXmax()+1, len(ybincenters), 0, graph_exp.GetYmax()+1)

    pointmultiple=5
    h_exp = makeHist("h_exp", pointmultiple*len(xbincenters), pointmultiple*len(ybincenters), graph_exp)
    fillTH2(h_exp, graph_exp)

    #call getcontour function
    cont_exp0=contourFromTH2(h_exp, 1, minPoints=1, mult = 1.0, smoothN=0)  #bp: set here contour value
    contours.append(cont_exp0)

  canv = r.TCanvas()
  pads=OnePad()
  pads[0].Draw()
#  pads[0].SetLogx(True)
#  pads[0].SetLogy(True)
#  pads[0].SetLogz(True)
  pads[0].SetBottomMargin(0.12)
  leg = r.TLegend(0.15, 0.60, 0.35, 0.8)
  leg.SetFillStyle(1001)
  leg.SetFillColor(0)
  leg.SetBorderSize(0)
  leg.SetTextFont(42)

  axis.GetXaxis().SetTitle('m_{S}[GeV]')
  axis.GetYaxis().SetTitle('m_{Zp}[GeV]')
  axis.SetTitleSize(.05,"X")
  axis.SetLabelSize(.04,"X")
  axis.SetTitleOffset(1.1,"X")
  axis.SetTitleSize(.05,"Y")
  axis.SetLabelSize(.04,"Y")
  axis.SetTitleOffset(0.9,"Y")
  axis.SetStats(0)
  axis.GetXaxis().SetRangeUser(xbincenters[0],xbincenters[len(xbincenters)-1])
  axis.GetXaxis().SetRangeUser(xbincenters[0],xbincenters[len(xbincenters)-1])
  axis.Draw()

  # make text box
  lat = r.TLatex()
  lat.SetNDC()
  lat.SetTextFont(42);

  lat2 = r.TLatex()
  lat2.SetNDC()
  lat2.SetTextSize(0.04)
  lat2.SetTextFont(42);

  # contours
  for i, contour in enumerate(contours):
    print "numer of i "+str(i)
    for q, p in enumerate(contour):
      # set the luminosities - style
        p.SetLineWidth(3)
        p.SetLineStyle(1)
        p.Draw("L SAME")
        p.SetLineColor(r.kBlue-4)




  # draw text
#  lat.DrawLatex(0.23,0.28,"#color[210]{g = darkHiggs}")
  lat.DrawLatex(0.23,0.28,"darkHiggs")
#  h_exp.Draw("samecolz")

  # draw legend
#  dummy3000 = r.TGraphAsymmErrors()
#  dummy3000.SetLineColor(r.kBlack)
#  dummy3000.SetLineStyle(1)
#  dummy3000.SetLineWidth(3)
#  dummy300 = r.TGraphAsymmErrors()
#  dummy300.SetLineColor(r.kBlack)
#  dummy300.SetLineStyle(7)
#  dummy300.SetLineWidth(3)
#  dummy20 = r.TGraphAsymmErrors()
#  dummy20.SetLineColor(r.kBlack)
#  dummy20.SetLineStyle(3)
#  dummy20.SetLineWidth(3)

#  leg.AddEntry(dummy3000,'3000fb^{-1}','L')
#  leg.AddEntry(dummy300,'300fb^{-1}','L')
#  leg.AddEntry(dummy20,'20fb^{-1}','L')
#  leg.Draw("same")
 
  r.gPad.RedrawAxis()

  # print canvas
  canv.Update()
  print 'the bottom margin is', canv.GetBottomMargin()
  canv.Print('contour.png')
  outf.cd()
  canv.SetName("limit_cavas")
  canv.Write()

makePlot()

 

