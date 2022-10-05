from tokenize import Double
import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *

#from bbtautauAnalysisScripts.BoostedTauIsoCorrectionTool.BoostedTauIsoCorrectionTool_cfi import *
from bbtautauAnalysisScripts.boostedTauLeadingLeptonIso.boostedTauLeadingLeptonIso_cfi import *

##################### Import reusable funtions and objects from std taus ########
from PhysicsTools.NanoAOD.taus_cff import _tauId2WPMask,_tauId5WPMask,_tauId7WPMask,tausMCMatchLepTauForTable,tausMCMatchHadTauForTable,tauMCTable
#BoostedTauIsoCorrectionTool.boostedTauCollection  = cms.InputTag("slimmedTausBoostedNewID")
#BoostedTauIsoCorrectionTool.muonCollection  = cms.InputTag("slimmedMuonsUpdated")

boostedTauLeadingLeptonIso.boostedTauCollection  = cms.InputTag("slimmedTausBoostedNewID")
boostedTauLeadingLeptonIso.muonCollection  = cms.InputTag("slimmedMuonsUpdated")

##################### User floats producers, selectors ##########################


finalBoostedTaus = cms.EDFilter("PATTauRefSelector",
    src = cms.InputTag("slimmedboostedTauWithUserData"),
    #tauSumChargedHadronPt = cms.InputTag("electronIsoCorrectionTool:tauSumChargedHadronPt"),
    #SumChargedHadronPt = cms.InputTag("electronIsoCorrectionTool:SumChargedHadronPt"),
    cut = cms.string("pt > 18")
    #cut = cms.string("pt > 40 && tauID('decayModeFindingNewDMs') && (tauID('byVVLooseIsolationMVArun2017v2DBoldDMwLT2017') || tauID('byVVLooseIsolationMVArun2017v2DBoldDMdR0p3wLT2017') || tauID('byVVLooseIsolationMVArun2017v2DBnewDMwLT2017'))")
)

slimmedboostedTauWithUserData = cms.EDProducer("PATTauUserDataEmbedder",
     src = cms.InputTag("slimmedTausBoostedNewID"),
     userFloats = cms.PSet(
        #ForEtauSumChargedHadronPt = cms.InputTag("BoostedTauIsoCorrectionTool:ForEtauSumChargedHadronPt"),
        #ForEtauSumPhotonEt = cms.InputTag("BoostedTauIsoCorrectionTool:ForEtauSumPhotonEt"),
        #ForEtauSumNeutralHadronEt = cms.InputTag("BoostedTauIsoCorrectionTool:ForEtauSumNeutralHadronEt"),
        #ESumChargedHadronPt = cms.InputTag("BoostedTauIsoCorrectionTool:ESumChargedHadronPt"),
        #ESumNeutralHadronEt = cms.InputTag("BoostedTauIsoCorrectionTool:ESumNeutralHadronEt"),
        #ESumPhotonEt = cms.InputTag("BoostedTauIsoCorrectionTool:ESumPhotonEt"),
        #Erho = cms.InputTag("BoostedTauIsoCorrectionTool:Erho"),
        #Eea = cms.InputTag("BoostedTauIsoCorrectionTool:Eea"),
        ##Ecounter = cms.InputTag("BoostedTauIsoCorrectionTool:Ecounter"),
        #EmatchedPt = cms.InputTag("BoostedTauIsoCorrectionTool:EmatchedPt"),
        #EmatchedEta = cms.InputTag("BoostedTauIsoCorrectionTool:EmatchedEta"),
        #EmatchedPhi = cms.InputTag("BoostedTauIsoCorrectionTool:EmatchedPhi"),
        #EmatchedMass = cms.InputTag("BoostedTauIsoCorrectionTool:EmatchedMass"),

        LeadingElectronPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectronPt"),
        LeadingElectronEta = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectronEta"),
        LeadingElectronPhi = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectronPhi"),
        LeadingElectronM = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectronM"),
        LeadingElectronCorrIso = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectronCorrIso"),
        LeadingElectronsumPFChargedHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectronsumPFChargedHadronPt"),
        LeadingElectronsumPFNeutralHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectronsumPFNeutralHadronPt"),
        LeadingElectronsumPFPhotonPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectronsumPFPhotonPt"),
        LeadingElectronea = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectronea"),
        LeadingElectronrho = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectronrho"),
        LeadingElectrontausumPFChargedHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectrontausumPFChargedHadronPt"),
        LeadingElectrontausumPFNeutralHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectrontausumPFNeutralHadronPt"),
        LeadingElectrontausumPFPhotonPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingElectrontausumPFPhotonPt"),


        SubLeadingElectronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectronPt"),
        SubLeadingElectronEta = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectronEta"),
        SubLeadingElectronPhi = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectronPhi"),
        SubLeadingElectronM = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectronM"),
        SubLeadingElectronCorrIso = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectronCorrIso"),
        SubLeadingElectronsumPFChargedHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectronsumPFChargedHadronPt"),
        SubLeadingElectronsumPFNeutralHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectronsumPFNeutralHadronPt"),
        SubLeadingElectronsumPFPhotonPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectronsumPFPhotonPt"),
        SubLeadingElectronea = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectronea"),
        SubLeadingElectronrho = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectronrho"),
        SubLeadingElectrontausumPFChargedHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectrontausumPFChargedHadronPt"),
        SubLeadingElectrontausumPFNeutralHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectrontausumPFNeutralHadronPt"),
        SubLeadingElectrontausumPFPhotonPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingElectrontausumPFPhotonPt"),        

        SubSubLeadingElectronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectronPt"),
        SubSubLeadingElectronEta = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectronEta"),
        SubSubLeadingElectronPhi = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectronPhi"),
        SubSubLeadingElectronM = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectronM"),
        SubSubLeadingElectronCorrIso = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectronCorrIso"),
        SubSubLeadingElectronsumPFChargedHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectronsumPFChargedHadronPt"),
        SubSubLeadingElectronsumPFNeutralHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectronsumPFNeutralHadronPt"),
        SubSubLeadingElectronsumPFPhotonPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectronsumPFPhotonPt"),
        SubSubLeadingElectronea = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectronea"),
        SubSubLeadingElectronrho = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectronrho"),
        SubSubLeadingElectrontausumPFChargedHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectrontausumPFChargedHadronPt"),
        SubSubLeadingElectrontausumPFNeutralHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectrontausumPFNeutralHadronPt"),
        SubSubLeadingElectrontausumPFPhotonPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingElectrontausumPFPhotonPt"),        
        ##############################################################################
        
        #ForMtauSumChargedHadronPt = cms.InputTag("BoostedTauIsoCorrectionTool:ForMtauSumChargedHadronPt"),
        #ForMtauSumPhotonEt = cms.InputTag("BoostedTauIsoCorrectionTool:ForMtauSumPhotonEt"),
        #ForMtauSumNeutralHadronEt = cms.InputTag("BoostedTauIsoCorrectionTool:ForMtauSumNeutralHadronEt"),
        #MSumChargedHadronPt = cms.InputTag("BoostedTauIsoCorrectionTool:MSumChargedHadronPt"),
        #MSumNeutralHadronEt = cms.InputTag("BoostedTauIsoCorrectionTool:MSumNeutralHadronEt"),
        #MSumPhotonEt = cms.InputTag("BoostedTauIsoCorrectionTool:MSumPhotonEt"),
        #MsumPUPt = cms.InputTag("BoostedTauIsoCorrectionTool:MsumPUPt"),
        ##Mcounter = cms.InputTag("BoostedTauIsoCorrectionTool:Mcounter"),
        #MmatchedPt = cms.InputTag("BoostedTauIsoCorrectionTool:MmatchedPt"),
        #MmatchedEta = cms.InputTag("BoostedTauIsoCorrectionTool:MmatchedEta"),
        #MmatchedPhi = cms.InputTag("BoostedTauIsoCorrectionTool:MmatchedPhi"),
        #MmatchedMass = cms.InputTag("BoostedTauIsoCorrectionTool:MmatchedMass"),

        LeadingMuonPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingMuonPt"),
        LeadingMuonEta = cms.InputTag("boostedTauLeadingLeptonIso:LeadingMuonEta"),
        LeadingMuonPhi = cms.InputTag("boostedTauLeadingLeptonIso:LeadingMuonPhi"),
        LeadingMuonM = cms.InputTag("boostedTauLeadingLeptonIso:LeadingMuonM"),
        LeadingMuonCorrIso = cms.InputTag("boostedTauLeadingLeptonIso:LeadingMuonCorrIso"),
        LeadingMuonsumPFChargedHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingMuonsumPFChargedHadronPt"),
        LeadingMuonsumPFNeutralHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingMuonsumPFNeutralHadronPt"),
        LeadingMuonsumPFPhotonPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingMuonsumPFPhotonPt"),
        LeadingMuonsumPUPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingMuonsumPUPt"),
        LeadingMuontausumPFChargedHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingMuontausumPFChargedHadronPt"),
        LeadingMuontausumPFNeutralHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingMuontausumPFNeutralHadronPt"),
        LeadingMuontausumPFPhotonPt = cms.InputTag("boostedTauLeadingLeptonIso:LeadingMuontausumPFPhotonPt"),

        SubLeadingMuonPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingMuonPt"),
        SubLeadingMuonEta = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingMuonEta"),
        SubLeadingMuonPhi = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingMuonPhi"),
        SubLeadingMuonM = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingMuonM"),
        SubLeadingMuonCorrIso = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingMuonCorrIso"),
        SubLeadingMuonsumPFChargedHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingMuonsumPFChargedHadronPt"),
        SubLeadingMuonsumPFNeutralHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingMuonsumPFNeutralHadronPt"),
        SubLeadingMuonsumPFPhotonPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingMuonsumPFPhotonPt"),
        SubLeadingMuonsumPUPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingMuonsumPUPt"),
        SubLeadingMuontausumPFChargedHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingMuontausumPFChargedHadronPt"),
        SubLeadingMuontausumPFNeutralHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingMuontausumPFNeutralHadronPt"),
        SubLeadingMuontausumPFPhotonPt = cms.InputTag("boostedTauLeadingLeptonIso:SubLeadingMuontausumPFPhotonPt"),        

        SubSubLeadingMuonPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingMuonPt"),
        SubSubLeadingMuonEta = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingMuonEta"),
        SubSubLeadingMuonPhi = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingMuonPhi"),
        SubSubLeadingMuonM = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingMuonM"),
        SubSubLeadingMuonCorrIso = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingMuonCorrIso"),
        SubSubLeadingMuonsumPFChargedHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingMuonsumPFChargedHadronPt"),
        SubSubLeadingMuonsumPFNeutralHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingMuonsumPFNeutralHadronPt"),
        SubSubLeadingMuonsumPFPhotonPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingMuonsumPFPhotonPt"),
        SubSubLeadingMuonsumPUPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingMuonsumPUPt"),
        SubSubLeadingMuontausumPFChargedHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingMuontausumPFChargedHadronPt"),
        SubSubLeadingMuontausumPFNeutralHadronPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingMuontausumPFNeutralHadronPt"),
        SubSubLeadingMuontausumPFPhotonPt = cms.InputTag("boostedTauLeadingLeptonIso:SubSubLeadingMuontausumPFPhotonPt"),         
  
     ),
     userInts = cms.PSet(
      Ecounter = cms.InputTag("boostedTauLeadingLeptonIso:Ecounter"),
      Mcounter = cms.InputTag("boostedTauLeadingLeptonIso:Mcounter"),
     ),

     #userCands = cms.PSet(
        #jetForLepJetVar = cms.InputTag("ptRatioRelForMu:jetForLepJetVar") # warning: Ptr is null if no match is found
     #),
)

def _tauIdWPMask(pattern, choices, doc=""):
    return Var(" + ".join(["%d * tauID('%s')" % (pow(2,i), pattern % c) for (i,c) in enumerate(choices)]), "uint8", 
               doc=doc+": bitmask "+", ".join(["%d = %s" % (pow(2,i),c) for (i,c) in enumerate(choices)]))
def _tauId2WPMask(pattern,doc):
    return _tauIdWPMask(pattern,choices=("Loose","Tight"),doc=doc)
def _tauId3WPMask(pattern,doc):
    return _tauIdWPMask(pattern,choices=("Loose","Medium","Tight"),doc=doc)
def _tauId4WPMask(pattern,doc):
    return _tauIdWPMask(pattern, choices=("VLoose", "Loose", "Medium", "Tight"), doc=doc)
def _tauId5WPMask(pattern,doc):
    return _tauIdWPMask(pattern,choices=("VLoose","Loose","Medium","Tight","VTight"),doc=doc)
def _tauId6WPMask(pattern,doc):
    return _tauIdWPMask(pattern,choices=("VLoose","Loose","Medium","Tight","VTight","VVTight"),doc=doc)
def _tauId7WPMask(pattern,doc):
    return _tauIdWPMask(pattern,choices=("VVLoose","VLoose","Loose","Medium","Tight","VTight","VVTight"),doc=doc)
def _tauId8WPMask(pattern,doc):
    return _tauIdWPMask(pattern,choices=("VVVLoose","VVLoose","VLoose","Loose","Medium","Tight","VTight","VVTight"),doc=doc)


boostedTauTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("finalBoostedTaus"), 
 #       tauSumChargedHadronPt = cms.InputTag("electronIsoCorrectionTool:tauSumChargedHadronPt"),
    #SumChargedHadronPt = cms.InputTag("electronIsoCorrectionTool:SumChargedHadronPt"),
    cut = cms.string(""), #we should not filter on cross linked collections
    name= cms.string("boostedTau"),
    doc = cms.string("slimmedBoostedTaus after basic selection (" + finalBoostedTaus.cut.value()+")"),
    singleton = cms.bool(False), # the number of entries is variable
    extension = cms.bool(False), # this is the main table for the taus
    variables = cms.PSet() # PSet defined below in era dependent way
)
_boostedTauVarsBase = cms.PSet(P4Vars,
       charge = Var("charge", int, doc="electric charge"),
       jetIdx = Var("?hasUserCand('jet')?userCand('jet').key():-1", int, doc="index of the associated jet (-1 if none)"),
       decayMode = Var("decayMode()",int),
       leadTkPtOverTauPt = Var("leadChargedHadrCand.pt/pt ",float, doc="pt of the leading track divided by tau pt",precision=10),
       leadTkDeltaEta = Var("leadChargedHadrCand.eta - eta ",float, doc="eta of the leading track, minus tau eta",precision=8),
       leadTkDeltaPhi = Var("deltaPhi(leadChargedHadrCand.phi, phi) ",float, doc="phi of the leading track, minus tau phi",precision=8),
       ###This is what I am adding for Electron variables
       #ForEtauSumChargedHadronPt = Var("userFloat('ForEtauSumChargedHadronPt')",float,doc="Tau contamination, SumChargedHadronPt,  in the matched electron cone"),
       #ForEtauSumPhotonEt = Var("userFloat('ForEtauSumPhotonEt')",float,doc="Tau contamination, SumPhotonEt,  in the matched electron cone"),
       #ForEtauSumNeutralHadronEt = Var("userFloat('ForEtauSumNeutralHadronEt')",float,doc="Tau contamination, SumNeutralHadronEt,  in the matched electron cone"),
       #ESumChargedHadronPt = Var("userFloat('ESumChargedHadronPt')",float,doc="Matched Electron's SumChargedHadronPt"),
       #ESumNeutralHadronEt = Var("userFloat('ESumNeutralHadronEt')",float,doc="Matched Electron's SumNeutralHadronEt"),
       #ESumPhotonEt = Var("userFloat('ESumPhotonEt')",float,doc="Matched Electron's SumPhotonEt"),
       #Erho = Var("userFloat('Erho')",float,doc="Matched Electron's rho"),
       #Eea = Var("userFloat('Eea')",float,doc="Matched Electron's Effective Area"),
       
       #EmatchedPt = Var("userFloat('EmatchedPt')",float,doc="Matched Electron's Pt"),
       #EmatchedEta = Var("userFloat('EmatchedEta')",float,doc="Matched Electron's Eta"),
       #EmatchedPhi = Var("userFloat('EmatchedPhi')",float,doc="Matched Electron's Phi"),
       #EmatchedMass = Var("userFloat('EmatchedMass')",float,doc="Matched Electron's Mass"),

       Ecounter = Var("userInt('Ecounter')",int,doc="Number of electrons that passed & matched with Tau and has the Loose ID and the delta R < 0.4 and > 0.02 requirements. Sadly we only store 3 leading"),

       LeadingElectronPt = Var("userFloat('LeadingElectronPt')",float,doc="Leading Matched Electron Pt"),
       LeadingElectronEta = Var("userFloat('LeadingElectronEta')",float,doc="Leading Matched Electron eta"),
       LeadingElectronPhi = Var("userFloat('LeadingElectronPhi')",float,doc="Leading Matched Electron phi"),
       LeadingElectronM = Var("userFloat('LeadingElectronM')",float,doc="Leading Matched Electron mass"),
       LeadingElectronCorrIso = Var("userFloat('LeadingElectronCorrIso')",float,doc="Corrected isolation for the Leading Electron matched"),
       LeadingElectronsumPFChargedHadronPt = Var("userFloat('LeadingElectronsumPFChargedHadronPt')",float,doc="sumPFChargedHadronPt for the Leading Electron matched"),
       LeadingElectronsumPFNeutralHadronPt = Var("userFloat('LeadingElectronsumPFNeutralHadronPt')",float,doc="sumPFNeutralHadronPt for the Leading Electron matched"),
       LeadingElectronsumPFPhotonPt = Var("userFloat('LeadingElectronsumPFPhotonPt')",float,doc="sumPFPhotonPt for the Leading Electron matched"),
       LeadingElectronea = Var("userFloat('LeadingElectronea')",float,doc="Electronea for the Leading Electron matched"),
       LeadingElectronrho = Var("userFloat('LeadingElectronrho')",float,doc="Electronrho for the Leading Electron matched"),
       LeadingElectrontausumPFChargedHadronPt = Var("userFloat('LeadingElectrontausumPFChargedHadronPt')",float,doc="tausumPFChargedHadronPt for the Leading Electron matched"),
       LeadingElectrontausumPFNeutralHadronPt = Var("userFloat('LeadingElectrontausumPFNeutralHadronPt')",float,doc="tausumPFNeutralHadronPt for the Leading Electron matched"),
       LeadingElectrontausumPFPhotonPt = Var("userFloat('LeadingElectrontausumPFPhotonPt')",float,doc="tausumPFPhotonPt for the Leading Electron matched"),              

       SubLeadingElectronPt = Var("userFloat('SubLeadingElectronPt')",float,doc="Sub Leading Matched Electron Pt"),
       SubLeadingElectronEta = Var("userFloat('SubLeadingElectronEta')",float,doc="Sub Leading Matched Electron eta"),
       SubLeadingElectronPhi = Var("userFloat('SubLeadingElectronPhi')",int,doc="Sub Leading Matched Electron phi"),
       SubLeadingElectronM = Var("userFloat('SubLeadingElectronM')",float,doc="Sub Leading Matched Electron mass"),
       SubLeadingElectronCorrIso = Var("userFloat('SubLeadingElectronCorrIso')",float,doc="Corrected isolation for the sub Leading Electron matched"),
       SubLeadingElectronsumPFChargedHadronPt = Var("userFloat('SubLeadingElectronsumPFChargedHadronPt')",float,doc="sumPFChargedHadronPt for the Sub Leading Electron matched"),
       SubLeadingElectronsumPFNeutralHadronPt = Var("userFloat('SubLeadingElectronsumPFNeutralHadronPt')",float,doc="sumPFNeutralHadronPt for the Sub Leading Electron matched"),
       SubLeadingElectronsumPFPhotonPt = Var("userFloat('SubLeadingElectronsumPFPhotonPt')",float,doc="sumPFPhotonPt for the Sub Leading Electron matched"),
       SubLeadingElectronea = Var("userFloat('SubLeadingElectronea')",float,doc="Electronea for the Sub Leading Electron matched"),
       SubLeadingElectronrho = Var("userFloat('SubLeadingElectronrho')",float,doc="Electronrho for the Sub Leading Electron matched"),
       SubLeadingElectrontausumPFChargedHadronPt = Var("userFloat('SubLeadingElectrontausumPFChargedHadronPt')",float,doc="tausumPFChargedHadronPt for the Sub Leading Electron matched"),
       SubLeadingElectrontausumPFNeutralHadronPt = Var("userFloat('SubLeadingElectrontausumPFNeutralHadronPt')",float,doc="tausumPFNeutralHadronPt for the Sub Leading Electron matched"),
       SubLeadingElectrontausumPFPhotonPt = Var("userFloat('SubLeadingElectrontausumPFPhotonPt')",float,doc="tausumPFPhotonPt for the Sub Leading Electron matched"),

       SubSubLeadingElectronPt =  Var("userFloat('SubSubLeadingElectronPt')",float,doc="Sub Sub Leading Matched Electron Pt"),
       SubSubLeadingElectronEta = Var("userFloat('SubSubLeadingElectronEta')",float,doc="Sub Sub Leading Matched Electron eta"), 
       SubSubLeadingElectronPhi = Var("userFloat('SubSubLeadingElectronPhi')",int,doc="Sub Sub Leading Matched Electron phi"),
       SubSubLeadingElectronM = Var("userFloat('SubSubLeadingElectronM')",float,doc="Sub Sub Leading Matched Electron mass"),
       SubSubLeadingElectronCorrIso = Var("userFloat('SubSubLeadingElectronCorrIso')",float,doc="Corrected isolation for the sub sub Leading Electron matched"),
       SubSubLeadingElectronsumPFChargedHadronPt = Var("userFloat('SubSubLeadingElectronsumPFChargedHadronPt')",float,doc="sumPFChargedHadronPt for the Sub Sub Leading Electron matched"),
       SubSubLeadingElectronsumPFNeutralHadronPt = Var("userFloat('SubSubLeadingElectronsumPFNeutralHadronPt')",float,doc="sumPFNeutralHadronPt for the Sub Sub Leading Electron matched"),
       SubSubLeadingElectronsumPFPhotonPt = Var("userFloat('SubSubLeadingElectronsumPFPhotonPt')",float,doc="sumPFPhotonPt for the Sub Sub Leading Electron matched"),
       SubSubLeadingElectronea = Var("userFloat('SubSubLeadingElectronea')",float,doc="Electronea for the Sub Sub Leading Electron matched"),
       SubSubLeadingElectronrho = Var("userFloat('SubSubLeadingElectronrho')",float,doc="Electronrho for the Sub Sub Leading Electron matched"),
       SubSubLeadingElectrontausumPFChargedHadronPt = Var("userFloat('SubSubLeadingElectrontausumPFChargedHadronPt')",float,doc="tausumPFChargedHadronPt for the Sub Sub Leading Electron matched"),
       SubSubLeadingElectrontausumPFNeutralHadronPt = Var("userFloat('SubSubLeadingElectrontausumPFNeutralHadronPt')",float,doc="tausumPFNeutralHadronPt for the Sub Sub Leading Electron matched"),
       SubSubLeadingElectrontausumPFPhotonPt = Var("userFloat('SubSubLeadingElectrontausumPFPhotonPt')",float,doc="tausumPFPhotonPt for the Sub Sub Leading Electron matched"),              



       ###This is what I am adding for muon variables
       #ForMtauSumChargedHadronPt = Var("userFloat('ForMtauSumChargedHadronPt')",float,doc="Tau contamination, SumChargedHadronPt,  in the matched muon cone"),
       #ForMtauSumPhotonEt = Var("userFloat('ForMtauSumPhotonEt')",float,doc="Tau contamination, SumPhotonEt,  in the matched muon cone"),
       #ForMtauSumNeutralHadronEt = Var("userFloat('ForMtauSumNeutralHadronEt')",float,doc="Tau contamination, SumNeutralHadronEt,  in the matched muon cone"),
       #MSumChargedHadronPt = Var("userFloat('MSumChargedHadronPt')",float,doc="Matched Muon's SumChargedHadronPt"),
       #MSumNeutralHadronEt = Var("userFloat('MSumNeutralHadronEt')",float,doc="Matched Muon's SumNeutralHadronEt"),
       #MSumPhotonEt = Var("userFloat('MSumPhotonEt')",float,doc="Matched Muon's SumPhotonEt"),
       #MsumPUPt = Var("userFloat('MsumPUPt')",float,doc="Matched Muon's sumPUPt"),
       
       #MmatchedPt = Var("userFloat('MmatchedPt')",float,doc="Matched muon's Pt"),
       #MmatchedEta = Var("userFloat('MmatchedEta')",float,doc="Matched muon's Eta"),
       #MmatchedPhi =  Var("userFloat('MmatchedPhi')",float,doc="Matched muon's Phi"),
       #MmatchedMass = Var("userFloat('MmatchedMass')",float,doc="Matched muon's Mass"),       
       ##SumChargedHadronPt = Var("userFloat('SumChargedHadronPt')",float,doc="photon pf info"), 

       Mcounter = Var("userInt('Mcounter')",int,doc="Number of muons that passed and matched with the Tau and has the Loose ID and the delta R < 0.4 and > 0.02 requirements. But sadly we only store 3"),

       LeadingMuonPt = Var("userFloat('LeadingMuonPt')",float,doc="Leading Matched Muon Pt"),
       LeadingMuonEta = Var("userFloat('LeadingMuonEta')",float,doc="Leading Matched Muon eta"),
       LeadingMuonPhi = Var("userFloat('LeadingMuonPhi')",float,doc="Leading Matched Muon phi"),
       LeadingMuonM = Var("userFloat('LeadingMuonM')",float,doc="Leading Matched Muon mass"),
       LeadingMuonCorrIso = Var("userFloat('LeadingMuonCorrIso')",float,doc="Corrected isolation for the Muon Leading matched"),
       LeadingMuonsumPFChargedHadronPt = Var("userFloat('LeadingMuonsumPFChargedHadronPt')",float,doc="sumPFChargedHadronPt for the Muon Leading matched"),
       LeadingMuonsumPFNeutralHadronPt = Var("userFloat('LeadingMuonsumPFNeutralHadronPt')",float,doc="sumPFNeutralHadronPt for the Muon Leading matched"),
       LeadingMuonsumPFPhotonPt = Var("userFloat('LeadingMuonsumPFPhotonPt')",float,doc="sumPFPhotonPt for the Muon Leading matched"),
       LeadingMuonsumPUPt = Var("userFloat('LeadingMuonsumPUPt')",float,doc="sumPUPt for the Muon Leading matched"),
       LeadingMuontausumPFChargedHadronPt = Var("userFloat('LeadingMuontausumPFChargedHadronPt')",float,doc="tausumPFChargedHadronPt for the Muon Leading matched"),
       LeadingMuontausumPFNeutralHadronPt = Var("userFloat('LeadingMuontausumPFNeutralHadronPt')",float,doc="tausumPFNeutralHadronPt for the Muon Leading matched"),
       LeadingMuontausumPFPhotonPt = Var("userFloat('LeadingMuontausumPFPhotonPt')",float,doc="tausumPFPhotonPt for the Muon Leading matched"),


       SubLeadingMuonPt = Var("userFloat('SubLeadingMuonPt')",float,doc="Sub Leading Matched Muon Pt"),
       SubLeadingMuonEta = Var("userFloat('SubLeadingMuonEta')",float,doc="Sub Leading Matched Muon eta"),
       SubLeadingMuonPhi = Var("userFloat('SubLeadingMuonPhi')",float,doc="Sub Leading Matched Muon phi"),
       SubLeadingMuonM = Var("userFloat('SubLeadingMuonM')",int,doc="Sub Leading Matched Muon mass"),
       SubLeadingMuonCorrIso = Var("userFloat('SubSubLeadingMuonCorrIso')",float,doc="Corrected isolation for the sub Leading Muon matched"),
       SubLeadingMuonsumPFChargedHadronPt = Var("userFloat('SubLeadingMuonsumPFChargedHadronPt')",float,doc="sumPFChargedHadronPt for the Muon Sub Leading matched"),
       SubLeadingMuonsumPFNeutralHadronPt = Var("userFloat('SubLeadingMuonsumPFNeutralHadronPt')",float,doc="sumPFNeutralHadronPt for the Muon Sub Leading matched"),
       SubLeadingMuonsumPFPhotonPt = Var("userFloat('SubLeadingMuonsumPFPhotonPt')",float,doc="sumPFPhotonPt for the Muon Sub Leading matched"),
       SubLeadingMuonsumPUPt = Var("userFloat('SubLeadingMuonsumPUPt')",float,doc="sumPUPt for the Muon Sub Leading matched"),
       SubLeadingMuontausumPFChargedHadronPt = Var("userFloat('SubLeadingMuontausumPFChargedHadronPt')",float,doc="tausumPFChargedHadronPt for the Muon Sub Leading matched"),
       SubLeadingMuontausumPFNeutralHadronPt = Var("userFloat('SubLeadingMuontausumPFNeutralHadronPt')",float,doc="tausumPFNeutralHadronPt for the Muon Sub Leading matched"),
       SubLeadingMuontausumPFPhotonPt = Var("userFloat('SubLeadingMuontausumPFPhotonPt')",float,doc="tausumPFPhotonPt for the Muon Sub Leading matched"),

       SubSubLeadingMuonPt = Var("userFloat('SubSubLeadingMuonPt')",float,doc="Sub-Sub Leading Matched Muon Pt"),
       SubSubLeadingMuonEta = Var("userFloat('SubSubLeadingMuonEta')",float,doc="Sub-Sub Leading Matched Muon eta"),
       SubSubLeadingMuonPhi = Var("userFloat('SubSubLeadingMuonPhi')",float,doc="Sub-Sub Leading Matched Muon phi"),
       SubSubLeadingMuonM = Var("userFloat('SubSubLeadingMuonM')",int,doc="Sub-Sub Leading Matched Muon mass"),
       SubSubLeadingMuonCorrIso = Var("userFloat('SubSubLeadingMuonCorrIso')",float,doc="Corrected isolation for the sub-sub Leading Muon matched"),
       SubSubLeadingMuonsumPFChargedHadronPt = Var("userFloat('SubSubLeadingMuonsumPFChargedHadronPt')",float,doc="sumPFChargedHadronPt for the Muon Sub Sub Leading matched"),
       SubSubLeadingMuonsumPFNeutralHadronPt = Var("userFloat('SubSubLeadingMuonsumPFNeutralHadronPt')",float,doc="sumPFNeutralHadronPt for the Muon Sub Sub Leading matched"),
       SubSubLeadingMuonsumPFPhotonPt = Var("userFloat('SubSubLeadingMuonsumPFPhotonPt')",float,doc="sumPFPhotonPt for the Muon Sub Sub Leading matched"),
       SubSubLeadingMuonsumPUPt = Var("userFloat('SubSubLeadingMuonsumPUPt')",float,doc="sumPUPt for the Muon Sub Sub Leading matched"),
       SubSubLeadingMuontausumPFChargedHadronPt = Var("userFloat('SubSubLeadingMuontausumPFChargedHadronPt')",float,doc="tausumPFChargedHadronPt for the Muon Sub Sub Leading matched"),
       SubSubLeadingMuontausumPFNeutralHadronPt = Var("userFloat('SubSubLeadingMuontausumPFNeutralHadronPt')",float,doc="tausumPFNeutralHadronPt for the Muon Sub Sub Leading matched"),
       SubSubLeadingMuontausumPFPhotonPt = Var("userFloat('SubSubLeadingMuontausumPFPhotonPt')",float,doc="tausumPFPhotonPt for the Muon Sub Sub Leading matched"),


       #####################
       rawIso = Var( "tauID('byCombinedIsolationDeltaBetaCorrRaw3Hits')", float, doc = "combined isolation (deltaBeta corrections)", precision=10),
       rawIsodR03 = Var( "(tauID('chargedIsoPtSumdR03')+max(0.,tauID('neutralIsoPtSumdR03')-0.072*tauID('puCorrPtSum')))", float, doc = "combined isolation (deltaBeta corrections, dR=0.3)", precision=10),
       chargedIso = Var( "tauID('chargedIsoPtSum')", float, doc = "charged isolation", precision=10),
       neutralIso = Var( "tauID('neutralIsoPtSum')", float, doc = "neutral (photon) isolation", precision=10),
       puCorr = Var( "tauID('puCorrPtSum')", float, doc = "pileup correction", precision=10),
       photonsOutsideSignalCone = Var( "tauID('photonPtSumOutsideSignalCone')", float, doc = "sum of photons outside signal cone", precision=10),
       idAntiMu = _tauId2WPMask("againstMuon%s3", doc= "Anti-muon discriminator V3: "),
       #MVA 2017 v2 variables
       rawMVAoldDM2017v2=Var("tauID('byIsolationMVArun2017v2DBoldDMwLTraw2017')",float, doc="byIsolationMVArun2017v2DBoldDMwLT raw output discriminator (2017v2)",precision=10),
       rawMVAnewDM2017v2 = Var("tauID('byIsolationMVArun2017v2DBnewDMwLTraw2017')",float,doc='byIsolationMVArun2017v2DBnewDMwLT raw output discriminator (2017v2)',precision=10),
       rawMVAoldDMdR032017v2 = Var("tauID('byIsolationMVArun2017v2DBoldDMdR0p3wLTraw2017')",float,doc='byIsolationMVArun2017v2DBoldDMdR0p3wLT raw output discriminator (2017v2)'),    
       idMVAnewDM2017v2 = _tauId7WPMask("by%sIsolationMVArun2017v2DBnewDMwLT2017", doc="IsolationMVArun2017v2DBnewDMwLT ID working point (2017v2)"),
       idMVAoldDM2017v2=_tauId7WPMask("by%sIsolationMVArun2017v2DBoldDMwLT2017",doc="IsolationMVArun2017v2DBoldDMwLT ID working point (2017v2)"),
       idMVAoldDMdR032017v2 = _tauId7WPMask("by%sIsolationMVArun2017v2DBoldDMdR0p3wLT2017",doc="IsolationMVArun2017v2DBoldDMdR0p3wLT ID working point (2017v2)"),
       rawAntiEle2018 = Var("tauID('againstElectronMVA6Raw')", float, doc= "Anti-electron MVA discriminator V6 raw output discriminator (2018)", precision=10),
       rawAntiEleCat2018 = Var("tauID('againstElectronMVA6category')", int, doc="Anti-electron MVA discriminator V6 category (2018)"),
       idAntiEle2018 = _tauId5WPMask("againstElectron%sMVA6", doc= "Anti-electron MVA discriminator V6 (2018)"),
)

_deepTauVars2017v2p1 = cms.PSet(
    rawDeepTau2017v2p1VSe = Var("tauID('byDeepTau2017v2p1VSeraw')", float, doc="byDeepTau2017v2p1VSe raw output discriminator (deepTau2017v2p1)", precision=10),
    rawDeepTau2017v2p1VSmu = Var("tauID('byDeepTau2017v2p1VSmuraw')", float, doc="byDeepTau2017v2p1VSmu raw output discriminator (deepTau2017v2p1)", precision=10),
    rawDeepTau2017v2p1VSjet = Var("tauID('byDeepTau2017v2p1VSjetraw')", float, doc="byDeepTau2017v2p1VSjet raw output discriminator (deepTau2017v2p1)", precision=10),
    idDeepTau2017v2p1VSe = _tauId8WPMask("by%sDeepTau2017v2p1VSe", doc="byDeepTau2017v2p1VSe ID working points (deepTau2017v2p1)"),
    idDeepTau2017v2p1VSmu = _tauId4WPMask("by%sDeepTau2017v2p1VSmu", doc="byDeepTau2017v2p1VSmu ID working points (deepTau2017v2p1)"),
    idDeepTau2017v2p1VSjet = _tauId8WPMask("by%sDeepTau2017v2p1VSjet", doc="byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1)"),
)


_variablesMiniV2 = cms.PSet(
    _boostedTauVarsBase,
    _deepTauVars2017v2p1
)

#boostedTauTable.variables = _boostedTauVarsBase
boostedTauTable.variables = _variablesMiniV2


boostedTausMCMatchLepTauForTable = tausMCMatchLepTauForTable.clone(
    src = boostedTauTable.src
)

#This requires genVisTaus in taus_cff.py
boostedTausMCMatchHadTauForTable = tausMCMatchHadTauForTable.clone(
    src = boostedTauTable.src
)

boostedTauMCTable = tauMCTable.clone(
    src = boostedTauTable.src,
    mcMap = cms.InputTag("boostedTausMCMatchLepTauForTable"),
    mcMapVisTau = cms.InputTag("boostedTausMCMatchHadTauForTable"),                         
    objName = boostedTauTable.name,
)

boostedTauSequence = cms.Sequence( boostedTauLeadingLeptonIso + slimmedboostedTauWithUserData + finalBoostedTaus)
#boostedTauSequence = cms.Sequence( BoostedTauIsoCorrectionTool + slimmedboostedTauWithUserData + finalBoostedTaus)
#boostedTauIsoSequence = cms.Sequence(electronIsoCorrectionTool)
boostedTauTables = cms.Sequence( boostedTauTable)
boostedTauMC = cms.Sequence( boostedTausMCMatchLepTauForTable + boostedTausMCMatchHadTauForTable + boostedTauMCTable)

