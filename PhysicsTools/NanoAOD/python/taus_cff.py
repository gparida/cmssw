import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *
from PhysicsTools.NanoAOD.nano_eras_cff import run3_nanoAOD_124
from PhysicsTools.NanoAOD.simpleCandidateFlatTableProducer_cfi import simpleCandidateFlatTableProducer

from PhysicsTools.JetMCAlgos.TauGenJets_cfi import tauGenJets
from PhysicsTools.JetMCAlgos.TauGenJetsDecayModeSelectorAllHadrons_cfi import tauGenJetsSelectorAllHadrons

##################### Updated tau collection with MVA-based tau-Ids rerun #######
# Used only in some eras
from PhysicsTools.NanoAOD.taus_updatedMVAIds_cff import *

#Changes made by Ganesh

#from bbtautauAnalysisScripts.TauIsoCorrectionTool.TauIsoCorrectionTool_cfi import *

from bbtautauAnalysisScripts.TauLeadingLeptonIso.TauLeadingLeptonIso_cfi import *
TauLeadingLeptonIso.TauCollection  = cms.InputTag("slimmedTaus")
TauLeadingLeptonIso.muonCollection  = cms.InputTag("slimmedMuonsUpdated")


##################### User floats producers, selectors ##########################

# Original DeepTau v2p5 in 12_4_X doesn't include WPs in MINIAOD
# Import thresholds here to define WPs manually from raw scores
from RecoTauTag.RecoTau.tauIdWPsDefs import WORKING_POINTS_v2p5

finalTaus = cms.EDFilter("PATTauRefSelector",
    #src = cms.InputTag("slimmedTaus"),
    src = cms.InputTag("slimmedTauWithUserData"),
    #cut = cms.string("pt > 18 && tauID('decayModeFindingNewDMs') && (tauID('byLooseCombinedIsolationDeltaBetaCorr3Hits') || (tauID('chargedIsoPtSumdR03')+max(0.,tauID('neutralIsoPtSumdR03')-0.072*tauID('puCorrPtSum'))<2.5) || tauID('byVVVLooseDeepTau2017v2p1VSjet') || tauID('byVVVLooseDeepTau2018v2p5VSjet'))")
    cut = cms.string("pt > 18")
)

run3_nanoAOD_124.toModify(
    finalTaus,
    #cut = cms.string("pt > 18 && tauID('decayModeFindingNewDMs') && (tauID('byLooseCombinedIsolationDeltaBetaCorr3Hits') || (tauID('chargedIsoPtSumdR03')+max(0.,tauID('neutralIsoPtSumdR03')-0.072*tauID('puCorrPtSum'))<2.5) || tauID('byVVVLooseDeepTau2017v2p1VSjet') || (tauID('byDeepTau2018v2p5VSjetraw') > {}))".format(WORKING_POINTS_v2p5["jet"]["VVVLoose"]))
    cut = cms.string("pt > 18")
)

slimmedTauWithUserData = cms.EDProducer("PATTauUserDataEmbedder",
     src = cms.InputTag("slimmedTaus"),
     userFloats = cms.PSet(
        #ForEtauSumChargedHadronPt = cms.InputTag("TauIsoCorrectionTool:ForEtauSumChargedHadronPt"),
        #ForEtauSumPhotonEt = cms.InputTag("TauIsoCorrectionTool:ForEtauSumPhotonEt"),
        #ForEtauSumNeutralHadronEt = cms.InputTag("TauIsoCorrectionTool:ForEtauSumNeutralHadronEt"),
        #ESumChargedHadronPt = cms.InputTag("TauIsoCorrectionTool:ESumChargedHadronPt"),
        #ESumNeutralHadronEt = cms.InputTag("TauIsoCorrectionTool:ESumNeutralHadronEt"),
        #ESumPhotonEt = cms.InputTag("TauIsoCorrectionTool:ESumPhotonEt"),
        #Erho = cms.InputTag("TauIsoCorrectionTool:Erho"),
        #Eea = cms.InputTag("TauIsoCorrectionTool:Eea"),
        ##Ecounter = cms.InputTag("TauIsoCorrectionTool:Ecounter"),
        #EmatchedPt = cms.InputTag("TauIsoCorrectionTool:EmatchedPt"),
        #EmatchedEta = cms.InputTag("TauIsoCorrectionTool:EmatchedEta"),
        #EmatchedPhi = cms.InputTag("TauIsoCorrectionTool:EmatchedPhi"),
        #EmatchedMass = cms.InputTag("TauIsoCorrectionTool:EmatchedMass"),
        LeadingElectronPt = cms.InputTag("TauLeadingLeptonIso:LeadingElectronPt"),
        LeadingElectronEta = cms.InputTag("TauLeadingLeptonIso:LeadingElectronEta"),
        LeadingElectronPhi = cms.InputTag("TauLeadingLeptonIso:LeadingElectronPhi"),
        LeadingElectronM = cms.InputTag("TauLeadingLeptonIso:LeadingElectronM"),
        LeadingElectronCorrIso = cms.InputTag("TauLeadingLeptonIso:LeadingElectronCorrIso"),
        LeadingElectronsumPFChargedHadronPt = cms.InputTag("TauLeadingLeptonIso:LeadingElectronsumPFChargedHadronPt"),
        LeadingElectronsumPFNeutralHadronPt = cms.InputTag("TauLeadingLeptonIso:LeadingElectronsumPFNeutralHadronPt"),
        LeadingElectronsumPFPhotonPt = cms.InputTag("TauLeadingLeptonIso:LeadingElectronsumPFPhotonPt"),
        LeadingElectronea = cms.InputTag("TauLeadingLeptonIso:LeadingElectronea"),
        LeadingElectronrho = cms.InputTag("TauLeadingLeptonIso:LeadingElectronrho"),
        LeadingElectrontausumPFChargedHadronPt = cms.InputTag("TauLeadingLeptonIso:LeadingElectrontausumPFChargedHadronPt"),
        LeadingElectrontausumPFNeutralHadronPt = cms.InputTag("TauLeadingLeptonIso:LeadingElectrontausumPFNeutralHadronPt"),
        LeadingElectrontausumPFPhotonPt = cms.InputTag("TauLeadingLeptonIso:LeadingElectrontausumPFPhotonPt"),

        SubLeadingElectronPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectronPt"),
        SubLeadingElectronEta = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectronEta"),
        SubLeadingElectronPhi = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectronPhi"),
        SubLeadingElectronM = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectronM"),
        SubLeadingElectronCorrIso = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectronCorrIso"),
        SubLeadingElectronsumPFChargedHadronPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectronsumPFChargedHadronPt"),
        SubLeadingElectronsumPFNeutralHadronPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectronsumPFNeutralHadronPt"),
        SubLeadingElectronsumPFPhotonPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectronsumPFPhotonPt"),
        SubLeadingElectronea = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectronea"),
        SubLeadingElectronrho = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectronrho"),
        SubLeadingElectrontausumPFChargedHadronPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectrontausumPFChargedHadronPt"),
        SubLeadingElectrontausumPFNeutralHadronPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectrontausumPFNeutralHadronPt"),
        SubLeadingElectrontausumPFPhotonPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingElectrontausumPFPhotonPt"),

        SubSubLeadingElectronPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectronPt"),
        SubSubLeadingElectronEta = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectronEta"),
        SubSubLeadingElectronPhi = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectronPhi"),
        SubSubLeadingElectronM = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectronM"),
        SubSubLeadingElectronCorrIso = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectronCorrIso"),
        SubSubLeadingElectronsumPFChargedHadronPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectronsumPFChargedHadronPt"),
        SubSubLeadingElectronsumPFNeutralHadronPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectronsumPFNeutralHadronPt"),
        SubSubLeadingElectronsumPFPhotonPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectronsumPFPhotonPt"),
        SubSubLeadingElectronea = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectronea"),
        SubSubLeadingElectronrho = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectronrho"),
        SubSubLeadingElectrontausumPFChargedHadronPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectrontausumPFChargedHadronPt"),
        SubSubLeadingElectrontausumPFNeutralHadronPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectrontausumPFNeutralHadronPt"),
        SubSubLeadingElectrontausumPFPhotonPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingElectrontausumPFPhotonPt"),
        ##############################################################################
        #ForMtauSumChargedHadronPt = cms.InputTag("TauIsoCorrectionTool:ForMtauSumChargedHadronPt"),
        #ForMtauSumPhotonEt = cms.InputTag("TauIsoCorrectionTool:ForMtauSumPhotonEt"),
        #ForMtauSumNeutralHadronEt = cms.InputTag("TauIsoCorrectionTool:ForMtauSumNeutralHadronEt"),
        #MSumChargedHadronPt = cms.InputTag("TauIsoCorrectionTool:MSumChargedHadronPt"),
        #MSumNeutralHadronEt = cms.InputTag("TauIsoCorrectionTool:MSumNeutralHadronEt"),
        #MSumPhotonEt = cms.InputTag("TauIsoCorrectionTool:MSumPhotonEt"),
        #MsumPUPt = cms.InputTag("TauIsoCorrectionTool:MsumPUPt"),
        ##Mcounter = cms.InputTag("TauIsoCorrectionTool:Mcounter"),
        #MmatchedPt = cms.InputTag("TauIsoCorrectionTool:MmatchedPt"),
        #MmatchedEta = cms.InputTag("TauIsoCorrectionTool:MmatchedEta"),
        #MmatchedPhi = cms.InputTag("TauIsoCorrectionTool:MmatchedPhi"),
        #MmatchedMass = cms.InputTag("TauIsoCorrectionTool:MmatchedMass"),

        LeadingMuonPt = cms.InputTag("TauLeadingLeptonIso:LeadingMuonPt"),
        LeadingMuonEta = cms.InputTag("TauLeadingLeptonIso:LeadingMuonEta"),
        LeadingMuonPhi = cms.InputTag("TauLeadingLeptonIso:LeadingMuonPhi"),
        LeadingMuonM = cms.InputTag("TauLeadingLeptonIso:LeadingMuonM"),
        LeadingMuonCorrIso = cms.InputTag("TauLeadingLeptonIso:LeadingMuonCorrIso"),
        LeadingMuonsumPFChargedHadronPt = cms.InputTag("TauLeadingLeptonIso:LeadingMuonsumPFChargedHadronPt"),
        LeadingMuonsumPFNeutralHadronPt = cms.InputTag("TauLeadingLeptonIso:LeadingMuonsumPFNeutralHadronPt"),
        LeadingMuonsumPFPhotonPt = cms.InputTag("TauLeadingLeptonIso:LeadingMuonsumPFPhotonPt"),
        LeadingMuonsumPUPt = cms.InputTag("TauLeadingLeptonIso:LeadingMuonsumPUPt"),
        LeadingMuontausumPFChargedHadronPt = cms.InputTag("TauLeadingLeptonIso:LeadingMuontausumPFChargedHadronPt"),
        LeadingMuontausumPFNeutralHadronPt = cms.InputTag("TauLeadingLeptonIso:LeadingMuontausumPFNeutralHadronPt"),
        LeadingMuontausumPFPhotonPt = cms.InputTag("TauLeadingLeptonIso:LeadingMuontausumPFPhotonPt"),

        SubLeadingMuonPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingMuonPt"),
        SubLeadingMuonEta = cms.InputTag("TauLeadingLeptonIso:SubLeadingMuonEta"),
        SubLeadingMuonPhi = cms.InputTag("TauLeadingLeptonIso:SubLeadingMuonPhi"),
        SubLeadingMuonM = cms.InputTag("TauLeadingLeptonIso:SubLeadingMuonM"),
        SubLeadingMuonCorrIso = cms.InputTag("TauLeadingLeptonIso:SubLeadingMuonCorrIso"),
        SubLeadingMuonsumPFChargedHadronPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingMuonsumPFChargedHadronPt"),
        SubLeadingMuonsumPFNeutralHadronPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingMuonsumPFNeutralHadronPt"),
        SubLeadingMuonsumPFPhotonPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingMuonsumPFPhotonPt"),
        SubLeadingMuonsumPUPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingMuonsumPUPt"),
        SubLeadingMuontausumPFChargedHadronPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingMuontausumPFChargedHadronPt"),
        SubLeadingMuontausumPFNeutralHadronPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingMuontausumPFNeutralHadronPt"),
        SubLeadingMuontausumPFPhotonPt = cms.InputTag("TauLeadingLeptonIso:SubLeadingMuontausumPFPhotonPt"),

        SubSubLeadingMuonPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingMuonPt"),
        SubSubLeadingMuonEta = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingMuonEta"),
        SubSubLeadingMuonPhi = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingMuonPhi"),
        SubSubLeadingMuonM = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingMuonM"),
        SubSubLeadingMuonCorrIso = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingMuonCorrIso"),
        SubSubLeadingMuonsumPFChargedHadronPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingMuonsumPFChargedHadronPt"),
        SubSubLeadingMuonsumPFNeutralHadronPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingMuonsumPFNeutralHadronPt"),
        SubSubLeadingMuonsumPFPhotonPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingMuonsumPFPhotonPt"),
        SubSubLeadingMuonsumPUPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingMuonsumPUPt"),
        SubSubLeadingMuontausumPFChargedHadronPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingMuontausumPFChargedHadronPt"),
        SubSubLeadingMuontausumPFNeutralHadronPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingMuontausumPFNeutralHadronPt"),
        SubSubLeadingMuontausumPFPhotonPt = cms.InputTag("TauLeadingLeptonIso:SubSubLeadingMuontausumPFPhotonPt"),


        #miniIsoChg = cms.InputTag("isoForMu:miniIsoChg"),
        #miniIsoAll = cms.InputTag("isoForMu:miniIsoAll"),
        #TauCorrPfIso = cms.InputTag("muonIsoCorrectionTool:TauCorrPfIso"),
        #ptRatio = cms.InputTag("ptRatioRelForMu:ptRatio"),
        #ptRel = cms.InputTag("ptRatioRelForMu:ptRel"),
        #jetNDauChargedMVASel = cms.InputTag("ptRatioRelForMu:jetNDauChargedMVASel"),
     ),
     userInts = cms.PSet(
      Ecounter = cms.InputTag("TauLeadingLeptonIso:Ecounter"),
      Mcounter = cms.InputTag("TauLeadingLeptonIso:Mcounter"),
     ),
     #userCands = cms.PSet(
        #jetForLepJetVar = cms.InputTag("ptRatioRelForMu:jetForLepJetVar") # warning: Ptr is null if no match is found
     #),
)

##################### Tables for final output and docs ##########################
def _tauIdWPMask(pattern, choices, doc="", from_raw=False, wp_thrs=None):
    if from_raw:
        assert wp_thrs is not None, "wp_thrs argument in _tauIdWPMask() is None, expect it to be dict-like"

        var_definition = []
        for wp_name in choices:
            if not isinstance(wp_thrs[wp_name], float):
                raise TypeError("Threshold for WP=%s is not a float number." % wp_name)
            wp_definition = "test_bit(tauID('{}')-{}+1,0)".format(pattern, wp_thrs[wp_name])
            var_definition.append(wp_definition)
        var_definition = " + ".join(var_definition)
    else:
        var_definition = " + ".join(["tauID('%s')" % (pattern % c) for c in choices])

    doc = doc + ": "+", ".join(["%d = %s" % (i,c) for (i,c) in enumerate(choices, start=1)])
    return Var(var_definition, "uint8", doc=doc)


tauTable = simpleCandidateFlatTableProducer.clone(
    src = cms.InputTag("linkedObjects","taus"),
    name= cms.string("Tau"),
    doc = cms.string("slimmedTaus after basic selection (" + finalTaus.cut.value()+")")
)

_tauVarsBase = cms.PSet(P4Vars,
       charge = Var("charge", "int16", doc="electric charge"),
       jetIdx = Var("?hasUserCand('jet')?userCand('jet').key():-1", "int16", doc="index of the associated jet (-1 if none)"),
       eleIdx = Var("?overlaps('electrons').size()>0?overlaps('electrons')[0].key():-1", "int16", doc="index of first matching electron"),
       muIdx = Var("?overlaps('muons').size()>0?overlaps('muons')[0].key():-1", "int16", doc="index of first matching muon"),
       svIdx1 = Var("?overlaps('vertices').size()>0?overlaps('vertices')[0].key():-1", "int16", doc="index of first matching secondary vertex"),
       svIdx2 = Var("?overlaps('vertices').size()>1?overlaps('vertices')[1].key():-1", "int16", doc="index of second matching secondary vertex"),
       nSVs = Var("?hasOverlaps('vertices')?overlaps('vertices').size():0", "uint8", doc="number of secondary vertices in the tau"),
       decayMode = Var("decayMode()", "uint8"),
       idDecayModeOldDMs = Var("tauID('decayModeFinding')", bool),

       #Changes made by Ganesh
       Ecounter = Var("userInt('Ecounter')",int,doc="Number of electrons that passed & matched with taus and has the Loose ID and the delta R < 0.4 and > 0.02 requirements. We sadly store only leading 3"),

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

       Mcounter = Var("userInt('Mcounter')",int,doc="Number of muons that passed & matched with tau and has the Loose ID and the delta R < 0.4 and > 0.02 requirements.We sadly store only leading 3"),

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



       leadTkPtOverTauPt = Var("leadChargedHadrCand.pt/pt ",float, doc="pt of the leading track divided by tau pt",precision=10),
       leadTkDeltaEta = Var("leadChargedHadrCand.eta - eta ",float, doc="eta of the leading track, minus tau eta",precision=8),
       leadTkDeltaPhi = Var("deltaPhi(leadChargedHadrCand.phi, phi) ",float, doc="phi of the leading track, minus tau phi",precision=8),

       dxy = Var("leadChargedHadrCand().dxy()",float, doc="d_{xy} of lead track with respect to PV, in cm (with sign)",precision=10),
       dz = Var("leadChargedHadrCand().dz()",float, doc="d_{z} of lead track with respect to PV, in cm (with sign)",precision=14),

       # these are too many, we may have to suppress some
       rawIso = Var( "tauID('byCombinedIsolationDeltaBetaCorrRaw3Hits')", float, doc = "combined isolation (deltaBeta corrections)", precision=10),
       rawIsodR03 = Var( "(tauID('chargedIsoPtSumdR03')+max(0.,tauID('neutralIsoPtSumdR03')-0.072*tauID('puCorrPtSum')))", float, doc = "combined isolation (deltaBeta corrections, dR=0.3)", precision=10),
       chargedIso = Var( "tauID('chargedIsoPtSum')", float, doc = "charged isolation", precision=10),
       neutralIso = Var( "tauID('neutralIsoPtSum')", float, doc = "neutral (photon) isolation", precision=10),
       puCorr = Var( "tauID('puCorrPtSum')", float, doc = "pileup correction", precision=10),
       photonsOutsideSignalCone = Var( "tauID('photonPtSumOutsideSignalCone')", float, doc = "sum of photons outside signal cone", precision=10),

       idAntiMu = _tauIdWPMask("againstMuon%s3", choices=("Loose","Tight"), doc= "Anti-muon discriminator V3: "),
       idAntiEleDeadECal = Var("tauID('againstElectronDeadECAL')", bool, doc = "Anti-electron dead-ECal discriminator"),

)

_deepTauVars2017v2p1 = cms.PSet(
    rawDeepTau2017v2p1VSe = Var("tauID('byDeepTau2017v2p1VSeraw')", float, doc="byDeepTau2017v2p1VSe raw output discriminator (deepTau2017v2p1)", precision=10),
    rawDeepTau2017v2p1VSmu = Var("tauID('byDeepTau2017v2p1VSmuraw')", float, doc="byDeepTau2017v2p1VSmu raw output discriminator (deepTau2017v2p1)", precision=10),
    rawDeepTau2017v2p1VSjet = Var("tauID('byDeepTau2017v2p1VSjetraw')", float, doc="byDeepTau2017v2p1VSjet raw output discriminator (deepTau2017v2p1)", precision=10),
    idDeepTau2017v2p1VSe = _tauIdWPMask("by%sDeepTau2017v2p1VSe",
                                            choices=("VVVLoose","VVLoose","VLoose","Loose","Medium","Tight","VTight","VVTight"),
                                            doc="byDeepTau2017v2p1VSe ID working points (deepTau2017v2p1)"),
    idDeepTau2017v2p1VSmu = _tauIdWPMask("by%sDeepTau2017v2p1VSmu",
                                            choices=("VLoose", "Loose", "Medium", "Tight"),
                                            doc="byDeepTau2017v2p1VSmu ID working points (deepTau2017v2p1)"),
    idDeepTau2017v2p1VSjet = _tauIdWPMask("by%sDeepTau2017v2p1VSjet",
                                            choices=("VVVLoose","VVLoose","VLoose","Loose","Medium","Tight","VTight","VVTight"),
                                            doc="byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1)"),
)
_deepTauVars2018v2p5 = cms.PSet(
    rawDeepTau2018v2p5VSe = Var("tauID('byDeepTau2018v2p5VSeraw')", float, doc="byDeepTau2018v2p5VSe raw output discriminator (deepTau2018v2p5)", precision=10),
    rawDeepTau2018v2p5VSmu = Var("tauID('byDeepTau2018v2p5VSmuraw')", float, doc="byDeepTau2018v2p5VSmu raw output discriminator (deepTau2018v2p5)", precision=10),
    rawDeepTau2018v2p5VSjet = Var("tauID('byDeepTau2018v2p5VSjetraw')", float, doc="byDeepTau2018v2p5VSjet raw output discriminator (deepTau2018v2p5)", precision=10),
    idDeepTau2018v2p5VSe = _tauIdWPMask("by%sDeepTau2018v2p5VSe",
                                            choices=("VVVLoose","VVLoose","VLoose","Loose","Medium","Tight","VTight","VVTight"),
                                            doc="byDeepTau2018v2p5VSe ID working points (deepTau2018v2p5)"),
    idDeepTau2018v2p5VSmu = _tauIdWPMask("by%sDeepTau2018v2p5VSmu",
                                            choices=("VLoose", "Loose", "Medium", "Tight"),
                                            doc="byDeepTau2018v2p5VSmu ID working points (deepTau2018v2p5)"),
    idDeepTau2018v2p5VSjet = _tauIdWPMask("by%sDeepTau2018v2p5VSjet",
                                            choices=("VVVLoose","VVLoose","VLoose","Loose","Medium","Tight","VTight","VVTight"),
                                            doc="byDeepTau2018v2p5VSjet ID working points (deepTau2018v2p5)"),
)

_variablesMiniV2 = cms.PSet(
    _tauVarsBase,
    _deepTauVars2017v2p1,
    _deepTauVars2018v2p5
)

tauTable.variables = _variablesMiniV2

run3_nanoAOD_124.toModify(
    tauTable.variables,
    idDeepTau2018v2p5VSe = _tauIdWPMask("byDeepTau2018v2p5VSeraw",
                 choices=("VVVLoose","VVLoose","VLoose","Loose","Medium","Tight","VTight","VVTight"),
                 doc="byDeepTau2018v2p5VSe ID working points (deepTau2018v2p5)",
                 from_raw=True, wp_thrs=WORKING_POINTS_v2p5["e"]),
    idDeepTau2018v2p5VSmu = _tauIdWPMask("byDeepTau2018v2p5VSmuraw",
                 choices=("VLoose", "Loose", "Medium", "Tight"),
                 doc="byDeepTau2018v2p5VSmu ID working points (deepTau2018v2p5)",
                 from_raw=True, wp_thrs=WORKING_POINTS_v2p5["mu"]),
    idDeepTau2018v2p5VSjet = _tauIdWPMask("byDeepTau2018v2p5VSjetraw",
                 choices=("VVVLoose","VVLoose","VLoose","Loose","Medium","Tight","VTight","VVTight"),
                 doc="byDeepTau2018v2p5VSjet ID working points (deepTau2018v2p5)",
                 from_raw=True, wp_thrs=WORKING_POINTS_v2p5["jet"])
)


tauGenJetsForNano = tauGenJets.clone(
    GenParticles = "finalGenParticles",
    includeNeutrinos = False
)

tauGenJetsSelectorAllHadronsForNano = tauGenJetsSelectorAllHadrons.clone(
    src = "tauGenJetsForNano"
)

genVisTaus = cms.EDProducer("GenVisTauProducer",
    src = cms.InputTag("tauGenJetsSelectorAllHadronsForNano"),
    srcGenParticles = cms.InputTag("finalGenParticles")
)

genVisTauTable = simpleCandidateFlatTableProducer.clone(
    src = cms.InputTag("genVisTaus"),
    cut = cms.string("pt > 10."),
    name = cms.string("GenVisTau"),
    doc = cms.string("gen hadronic taus "),
    variables = cms.PSet(
         pt = Var("pt", float,precision=8),
         phi = Var("phi", float,precision=8),
         eta = Var("eta", float,precision=8),
         mass = Var("mass", float,precision=8),
	 charge = Var("charge", "int16"),
	 status = Var("status", "uint8", doc="Hadronic tau decay mode. 0=OneProng0PiZero, 1=OneProng1PiZero, 2=OneProng2PiZero, 10=ThreeProng0PiZero, 11=ThreeProng1PiZero, 15=Other"),
	 genPartIdxMother = Var("?numberOfMothers>0?motherRef(0).key():-1", "int16", doc="index of the mother particle"),
    )
)

tausMCMatchLepTauForTable = cms.EDProducer("MCMatcher",  # cut on deltaR, deltaPt/Pt; pick best by deltaR
    src         = tauTable.src,                 # final reco collection
    matched     = cms.InputTag("finalGenParticles"), # final mc-truth particle collection
    mcPdgId     = cms.vint32(11,13),            # one or more PDG ID (11 = electron, 13 = muon); absolute values (see below)
    checkCharge = cms.bool(False),              # True = require RECO and MC objects to have the same charge
    mcStatus    = cms.vint32(),                 # PYTHIA status code (1 = stable, 2 = shower, 3 = hard scattering)
    maxDeltaR   = cms.double(0.3),              # Minimum deltaR for the match
    maxDPtRel   = cms.double(0.5),              # Minimum deltaPt/Pt for the match
    resolveAmbiguities    = cms.bool(True),     # Forbid two RECO objects to match to the same GEN object
    resolveByMatchQuality = cms.bool(True),     # False = just match input in order; True = pick lowest deltaR pair first
)

tausMCMatchHadTauForTable = cms.EDProducer("MCMatcher",  # cut on deltaR, deltaPt/Pt; pick best by deltaR
    src         = tauTable.src,                 # final reco collection
    matched     = cms.InputTag("genVisTaus"),   # generator level hadronic tau decays
    mcPdgId     = cms.vint32(15),               # one or more PDG ID (15 = tau); absolute values (see below)
    checkCharge = cms.bool(False),              # True = require RECO and MC objects to have the same charge
    mcStatus    = cms.vint32(),                 # CV: no *not* require certain status code for matching (status code corresponds to decay mode for hadronic tau decays)
    maxDeltaR   = cms.double(0.3),              # Maximum deltaR for the match
    maxDPtRel   = cms.double(1.),               # Maximum deltaPt/Pt for the match
    resolveAmbiguities    = cms.bool(True),     # Forbid two RECO objects to match to the same GEN object
    resolveByMatchQuality = cms.bool(True),     # False = just match input in order; True = pick lowest deltaR pair first
)

tauMCTable = cms.EDProducer("CandMCMatchTableProducer",
    src = tauTable.src,
    mcMap = cms.InputTag("tausMCMatchLepTauForTable"),
    mcMapVisTau = cms.InputTag("tausMCMatchHadTauForTable"),
    objName = tauTable.name,
    objType = tauTable.name, #cms.string("Tau"),
    branchName = cms.string("genPart"),
    docString = cms.string("MC matching to status==2 taus"),
)


#tauTask = cms.Task(TauLeadingLeptonIso + slimmedTauWithUserData + finalTaus)
tauTask = cms.Task(finalTaus)
tauTablesTask = cms.Task(tauTable)

genTauTask = cms.Task(tauGenJetsForNano,tauGenJetsSelectorAllHadronsForNano,genVisTaus,genVisTauTable)
tauMCTask = cms.Task(genTauTask,tausMCMatchLepTauForTable,tausMCMatchHadTauForTable,tauMCTable)

