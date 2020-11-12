import ROOT as R
import sys

path='.'

def th1_gev( name, title, xmin, xmax ):
    dict_th1[name] = R.TH1F( name, title, int((xmax-xmin)/20), xmin, xmax )
#end

def th1( name, title, nbin, xmin, xmax ):
    dict_th1[name] = R.TH1F( name, title, nbin, xmin, xmax )
#end

### MAIN ###
fin = R.TFile.Open('{0}/pred_ntuple_merged_7.root'.format(path))
tin = fin.Get('tree')

chain = R.TChain('tree')
print('reading {0}/pred_ntuple_merged_7.root ...'.format(path))
chain.Add('{0}/pred_ntuple_merged_7.root'.format(path))

nevent = chain.GetEntries();

'''
print(tin.GetBranch('isB').GetName())
R.gROOT.ProcessLine('.L struct1.C')
mys = R.MyStruct()
chain.SetBranchAddress('isB',R.AddressOf(mys,'isB'))
'''

print(nevent)

dict_th1 = dict()
# histograms #
th1    ('isB', 'B-Jet label', 30, -0.1, 1.1)
th1    ('isBB','BB-Jet label', 30, -0.1, 1.1)
th1    ('isC', 'C-Jet label', 30, -0.1, 1.1)
th1    ('isUDSG', 'LightFlavour-Jet label', 30, -0.1, 1.1)
th1    ('Norm','probability nomalization validation', 20, 0.9, 1.1)

th1    ('ptisB', 'B-Jet pt', 100, 0, 1000)
th1    ('ptisBB','BB-Jet pt', 100, 0, 1000)
th1    ('ptisC', 'C-Jet pt', 100, 0, 1000)
th1    ('ptisUDSG', 'LightFlavour-Jet pt', 100, 0, 1000)

th1    ('etaisB', 'B-Jet Eta', 100, -3, 3)
th1    ('etaisBB','BB-Jet Eta', 100, -3, 3)
th1    ('etaisC', 'C-Jet Eta', 100, -3, 3)
th1    ('etaisUDSG', 'LightFlavour-Jet Eta', 100, -3, 3)

th1    ('prob_isB','predicted B-Jet score', 100, -0.1, 1.1)
th1    ('prob_isB_true','predicted B-Jet score', 100, -0.1, 1.1)
th1    ('prob_isB_false','predicted B-Jet score', 100, -0.1, 1.1)

th1    ('prob_isBB','predicted BB-Jet score', 100, -0.1, 1.1)
th1    ('prob_isBB_true','predicted BB-Jet score', 100, -0.1, 1.1)
th1    ('prob_isBB_false','predicted BB-Jet score', 100, -0.1, 1.1)

th1    ('prob_isC','predicted C-Jet score', 100, -0.1, 1.1)
th1    ('prob_isC_true','predicted C-Jet score', 100, -0.1, 1.1)
th1    ('prob_isC_false','predicted C-Jet score', 100, -0.1, 1.1)

th1    ('prob_isUDSG','predicted LightFlavour-Jet score', 100, -0.1, 1.1)
th1    ('prob_isUDSG_true','predicted LightFlavour-Jet score', 100, -0.1, 1.1)
th1    ('prob_isUDSG_false','predicted LightFlavour-Jet score', 100, -0.1, 1.1)

'''
for event in tin:
    isB         = (event.__getattr__('isB'))
    dict_th1['isB'].Fill(isB)
    
    prob_isB    = (event.__getattr__('prob_isB'))
    dict_th1['prob_isB']          .Fill(prob_isB)
    
    if      isB == 0 :
        dict_th1['prob_isB_true'] .Fill(prob_isB)
    elif    isB == 1 :
        dict_th1['prob_isB_false'].Fill(prob_isB)
        norm = norm + 1
        
    isBB        = (event.__getattr__('isBB'))
    if      isBB == 1 :
        norm = norm + 1

    isC        = (event.__getattr__('isC'))
    if      isC == 1 :
        norm = norm + 1

    isUDSG        = (event.__getattr__('isUDSG'))
    if      isUDSG == 1 :
        norm = norm + 1
#end
'''
print('Analyzing... ')
for i in range(nevent):
    chain.GetEvent(i);
    
    isB         = (chain.GetLeaf('isB').GetValue())
    dict_th1['isB'].Fill(isB)
    
    prob_isB    = (chain.GetLeaf('prob_isB').GetValue())
    dict_th1['prob_isB']          .Fill(prob_isB)
    
    if      isB == 1 :
        dict_th1['prob_isB_true'] .Fill(prob_isB)
        dict_th1['ptisB'] .Fill(chain.GetLeaf('jet_pt').GetValue())
        dict_th1['etaisB'] .Fill(chain.GetLeaf('jet_eta').GetValue())
    elif    isB == 0 :
        dict_th1['prob_isB_false'].Fill(prob_isB)
        
    isBB         = (chain.GetLeaf('isBB').GetValue())
    dict_th1['isBB'].Fill(isBB)
    
    prob_isBB    = (chain.GetLeaf('prob_isBB').GetValue())
    dict_th1['prob_isBB']          .Fill(prob_isBB)
    
    if      isBB == 1 :
        dict_th1['prob_isBB_true'] .Fill(prob_isBB)
        dict_th1['ptisBB'] .Fill(chain.GetLeaf('jet_pt').GetValue())
        dict_th1['etaisBB'] .Fill(chain.GetLeaf('jet_eta').GetValue())
    elif    isBB == 0 :
        dict_th1['prob_isBB_false'].Fill(prob_isBB)
        
    isC         = (chain.GetLeaf('isC').GetValue())
    dict_th1['isC'].Fill(isC)
    
    prob_isC    = (chain.GetLeaf('prob_isC').GetValue())
    dict_th1['prob_isC']          .Fill(prob_isC)
    
    if      isC == 1 :
        dict_th1['prob_isC_true'] .Fill(prob_isC)
        dict_th1['ptisC'] .Fill(chain.GetLeaf('jet_pt').GetValue())
        dict_th1['etaisC'] .Fill(chain.GetLeaf('jet_eta').GetValue())
    elif    isC == 0 :
        dict_th1['prob_isC_false'].Fill(prob_isC)
        
    isUDSG         = (chain.GetLeaf('isUDSG').GetValue())
    dict_th1['isUDSG'].Fill(isUDSG)
    
    prob_isUDSG    = (chain.GetLeaf('prob_isUDSG').GetValue())
    dict_th1['prob_isUDSG']          .Fill(prob_isUDSG)
    
    if      isUDSG == 1 :
        dict_th1['prob_isUDSG_true'] .Fill(prob_isUDSG)
        dict_th1['ptisUDSG'] .Fill(chain.GetLeaf('jet_pt').GetValue())
        dict_th1['etaisUDSG'] .Fill(chain.GetLeaf('jet_eta').GetValue())
    elif    isUDSG == 0 :
        dict_th1['prob_isUDSG_false'].Fill(prob_isUDSG)
        
    dict_th1['Norm'].Fill(prob_isB + prob_isBB + prob_isC + prob_isUDSG)
print('Printing... ')
#end

c_isB = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['isB'].GetXaxis().SetTitle('isB')
dict_th1['isB'].GetYaxis().SetTitle('Counts')
dict_th1['isB'].Draw()

c_prob_isB = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['prob_isB'].GetXaxis().SetTitle('prob_isB')
dict_th1['prob_isB'].GetYaxis().SetTitle('Counts')
dict_th1['prob_isB']       .Draw()

c_predict_isB = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['prob_isB_true']   .SetFillColorAlpha(R.kBlue,0.5)
dict_th1['prob_isB_false']  .SetFillColorAlpha(R.kRed,0.7)
dict_th1['prob_isB_false']  .GetXaxis().SetTitle('Probability')
dict_th1['prob_isB_false']  .GetYaxis().SetTitle('Counts')
dict_th1['prob_isB_false']  .Draw()
dict_th1['prob_isB_true']   .Draw('SAME')
l_predict_isB = R.TLegend(0.6,0.7,0.85,0.85)
l_predict_isB.SetLineWidth(0)
l_predict_isB.AddEntry(dict_th1['prob_isB_true'],'Is B-Jet')
l_predict_isB.AddEntry(dict_th1['prob_isB_false'],'Not B-Jet')
l_predict_isB.Draw('SAME')

c_isBB = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['isBB'].GetXaxis().SetTitle('isBB')
dict_th1['isBB'].GetYaxis().SetTitle('Counts')
dict_th1['isBB'].Draw()

c_prob_isBB = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['prob_isBB'].GetXaxis().SetTitle('prob_isBB')
dict_th1['prob_isBB'].GetYaxis().SetTitle('Counts')
dict_th1['prob_isBB'].Draw()

c_predict_isBB = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['prob_isBB_true']   .SetFillColorAlpha(R.kBlue,0.5)
dict_th1['prob_isBB_false']  .SetFillColorAlpha(R.kRed,0.7)
dict_th1['prob_isBB_false']  .GetXaxis().SetTitle('Probability')
dict_th1['prob_isBB_false']  .GetYaxis().SetTitle('Counts')
dict_th1['prob_isBB_false']  .Draw()
dict_th1['prob_isBB_true']   .Draw('SAME')
l_predict_isBB = R.TLegend(0.6,0.7,0.85,0.85)
l_predict_isBB.SetLineWidth(0)
l_predict_isBB.AddEntry(dict_th1['prob_isBB_true'],'Is BB-Jet')
l_predict_isBB.AddEntry(dict_th1['prob_isBB_false'],'Not BB-Jet')
l_predict_isBB.Draw('SAME')

c_isC = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['isC'].GetXaxis().SetTitle('isC')
dict_th1['isC'].GetYaxis().SetTitle('Counts')
dict_th1['isC'].Draw()

c_prob_isC = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['prob_isC'].GetXaxis().SetTitle('prob_isC')
dict_th1['prob_isC'].GetYaxis().SetTitle('Counts')
dict_th1['prob_isC'].Draw()

c_predict_isC = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['prob_isC_true']   .SetFillColorAlpha(R.kBlue,0.5)
dict_th1['prob_isC_false']  .SetFillColorAlpha(R.kRed,0.7)
dict_th1['prob_isC_false']  .GetXaxis().SetTitle('Probability')
dict_th1['prob_isC_false']  .GetYaxis().SetTitle('Counts')
dict_th1['prob_isC_false']  .Draw()
dict_th1['prob_isC_true']   .Draw('SAME')
l_predict_isC = R.TLegend(0.6,0.7,0.85,0.85)
l_predict_isC.SetLineWidth(0)
l_predict_isC.AddEntry(dict_th1['prob_isC_true'],'Is C-Jet')
l_predict_isC.AddEntry(dict_th1['prob_isC_false'],'Not C-Jet')
l_predict_isC.Draw('SAME')

c_isUDSG = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['isUDSG'].GetXaxis().SetTitle('isUDSG')
dict_th1['isUDSG'].GetYaxis().SetTitle('Counts')
dict_th1['isUDSG'].Draw()

c_prob_isUDSG = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['prob_isUDSG'].GetXaxis().SetTitle('prob_isUDSG')
dict_th1['prob_isUDSG'].GetYaxis().SetTitle('Counts')
dict_th1['prob_isUDSG'].Draw()

c_predict_isUDSG = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['prob_isUDSG_true']   .SetFillColorAlpha(R.kBlue,0.7)
dict_th1['prob_isUDSG_false']  .SetFillColorAlpha(R.kRed,0.5)
dict_th1['prob_isUDSG_true']  .GetXaxis().SetTitle('Probability')
dict_th1['prob_isUDSG_true']  .GetYaxis().SetTitle('Counts')
dict_th1['prob_isUDSG_true']  .Draw()
dict_th1['prob_isUDSG_false']   .Draw('SAME')
l_predict_isUDSG = R.TLegend(0.4,0.7,0.65,0.85)
l_predict_isUDSG.SetLineWidth(0)
l_predict_isUDSG.AddEntry(dict_th1['prob_isUDSG_true'],'Is LightFlavour-Jet')
l_predict_isUDSG.AddEntry(dict_th1['prob_isUDSG_false'],'Not LightFlavour-Jet')
l_predict_isUDSG.Draw('SAME')

c_Norm = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['Norm'].GetXaxis().SetTitle('Probability')
dict_th1['Norm'].GetYaxis().SetTitle('Counts')
dict_th1['Norm'].Draw()

c_pt = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['ptisUDSG'].GetXaxis().SetTitle('Jet-Pt')
dict_th1['ptisUDSG'].GetYaxis().SetTitle('Counts')
'''
dict_th1['ptisUDSG'].SetFillColorAlpha(R.kBlue,0.3)
dict_th1['ptisB'].SetFillColorAlpha(R.kRed,0.5)
dict_th1['ptisBB'].SetFillColorAlpha(R.kBlue,0.5)
dict_th1['ptisC'].SetFillColorAlpha(R.kGreen,0.5)
'''

dict_th1['ptisUDSG'].SetLineColor(R.kBlue)
dict_th1['ptisB'].SetLineColor(R.kRed)
dict_th1['ptisBB'].SetLineColor(R.kBlue)
dict_th1['ptisC'].SetLineColor(R.kGreen)

dict_th1['ptisUDSG'].SetLineWidth(3)
dict_th1['ptisB'].SetLineWidth(3)
dict_th1['ptisBB'].SetLineWidth(3)
dict_th1['ptisC'].SetLineWidth(3)

dict_th1['ptisUDSG'].Draw()
dict_th1['ptisB'].Draw('SAME')
dict_th1['ptisBB'].Draw('SAME')
dict_th1['ptisC'].Draw('SAME')

l_pt = R.TLegend(0.6,0.7,0.85,0.85)
l_pt.SetLineWidth(0)
l_pt.AddEntry(dict_th1['ptisUDSG'],'Is LightFlavour-Jet')
l_pt.AddEntry(dict_th1['ptisB'],'Is B-Jet')
l_pt.AddEntry(dict_th1['ptisBB'],'Is BB-Jet')
l_pt.AddEntry(dict_th1['ptisC'],'Is C-Jet')

l_pt.Draw('SAME')

c_eta = R.TCanvas()
R.gStyle.SetOptStat(0)
R.gPad.SetLogy(1)
dict_th1['etaisUDSG'].GetXaxis().SetTitle('Jet-Eta')
dict_th1['etaisUDSG'].GetYaxis().SetTitle('Counts')

dict_th1['etaisUDSG'].SetLineColor(R.kViolet)
dict_th1['etaisB'].SetLineColor(R.kRed)
dict_th1['etaisBB'].SetLineColor(R.kBlue)
dict_th1['etaisC'].SetLineColor(R.kGreen)

dict_th1['etaisUDSG'].SetLineWidth(3)
dict_th1['etaisB'].SetLineWidth(3)
dict_th1['etaisBB'].SetLineWidth(3)
dict_th1['etaisC'].SetLineWidth(3)

dict_th1['etaisB'].GetXaxis().SetTitle('Jet-Eta')
dict_th1['etaisB'].GetYaxis().SetTitle('Counts')

#dict_th1['etaisUDSG'].Draw()
dict_th1['etaisB'].Draw()
dict_th1['etaisBB'].Draw('SAME')
dict_th1['etaisC'].Draw('SAME')

l_eta = R.TLegend(0.65,0.75,0.90,0.90)
l_eta.SetLineWidth(0)
#l_pt.AddEntry(dict_th1['etaisUDSG'],'Is LightFlavour-Jet')
l_eta.AddEntry(dict_th1['etaisB'],'Is B-Jet')
l_eta.AddEntry(dict_th1['etaisBB'],'Is BB-Jet')
l_eta.AddEntry(dict_th1['etaisC'],'Is C-Jet')

l_eta.Draw('SAME')


### END ###

print('End of the process!')
noLove=input()
if noLove:
    print(True)
#input("Please Enter:")

