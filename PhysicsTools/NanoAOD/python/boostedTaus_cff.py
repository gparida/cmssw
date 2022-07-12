from tokenize import Double
import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *

from bbtautauAnalysisScripts.BoostedTauIsoCorrectionTool.BoostedTauIsoCorrectionTool_cfi import *

##################### Import reusable funtions and objects from std taus ########
from PhysicsTools.NanoAOD.taus_cff import _tauId2WPMask,_tauId5WPMask,_tauId7WPMask,tausMCMatchLepTauForTable,tausMCMatchHadTauForTable,tauMCTable
BoostedTauIsoCorrectionTool.boostedTauCollection  = cms.InputTag("slimmedTausBoostedNewID")

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
        ForEtauSumChargedHadronPt = cms.InputTag("BoostedTauIsoCorrectionTool:ForEtauSumChargedHadronPt"),
        ForEtauSumPhotonEt = cms.InputTag("BoostedTauIsoCorrectionTool:ForEtauSumPhotonEt"),
        ForEtauSumNeutralHadronEt = cms.InputTag("BoostedTauIsoCorrectionTool:ForEtauSumNeutralHadronEt"),
        ESumChargedHadronPt = cms.InputTag("BoostedTauIsoCorrectionTool:ESumChargedHadronPt"),
        ESumNeutralHadronEt = cms.InputTag("BoostedTauIsoCorrectionTool:ESumNeutralHadronEt"),
        ESumPhotonEt = cms.InputTag("BoostedTauIsoCorrectionTool:ESumPhotonEt"),
        Erho = cms.InputTag("BoostedTauIsoCorrectionTool:Erho"),
        Eea = cms.InputTag("BoostedTauIsoCorrectionTool:Eea"),
        #Ecounter = cms.InputTag("BoostedTauIsoCorrectionTool:Ecounter"),
        EmatchedPt = cms.InputTag("BoostedTauIsoCorrectionTool:EmatchedPt"),
        EmatchedEta = cms.InputTag("BoostedTauIsoCorrectionTool:EmatchedEta"),
        EmatchedPhi = cms.InputTag("BoostedTauIsoCorrectionTool:EmatchedPhi"),
        EmatchedMass = cms.InputTag("BoostedTauIsoCorrectionTool:EmatchedMass"),
        ##############################################################################
        ForMtauSumChargedHadronPt = cms.InputTag("BoostedTauIsoCorrectionTool:ForMtauSumChargedHadronPt"),
        ForMtauSumPhotonEt = cms.InputTag("BoostedTauIsoCorrectionTool:ForMtauSumPhotonEt"),
        ForMtauSumNeutralHadronEt = cms.InputTag("BoostedTauIsoCorrectionTool:ForMtauSumNeutralHadronEt"),
        MSumChargedHadronPt = cms.InputTag("BoostedTauIsoCorrectionTool:MSumChargedHadronPt"),
        MSumNeutralHadronEt = cms.InputTag("BoostedTauIsoCorrectionTool:MSumNeutralHadronEt"),
        MSumPhotonEt = cms.InputTag("BoostedTauIsoCorrectionTool:MSumPhotonEt"),
        MsumPUPt = cms.InputTag("BoostedTauIsoCorrectionTool:MsumPUPt"),
        #Mcounter = cms.InputTag("BoostedTauIsoCorrectionTool:Mcounter"),
        MmatchedPt = cms.InputTag("BoostedTauIsoCorrectionTool:MmatchedPt"),
        MmatchedEta = cms.InputTag("BoostedTauIsoCorrectionTool:MmatchedEta"),
        MmatchedPhi = cms.InputTag("BoostedTauIsoCorrectionTool:MmatchedPhi"),
        MmatchedMass = cms.InputTag("BoostedTauIsoCorrectionTool:MmatchedMass"),

        #miniIsoChg = cms.InputTag("isoForMu:miniIsoChg"),
        #miniIsoAll = cms.InputTag("isoForMu:miniIsoAll"),
        #TauCorrPfIso = cms.InputTag("muonIsoCorrectionTool:TauCorrPfIso"),
        #ptRatio = cms.InputTag("ptRatioRelForMu:ptRatio"),
        #ptRel = cms.InputTag("ptRatioRelForMu:ptRel"),
        #jetNDauChargedMVASel = cms.InputTag("ptRatioRelForMu:jetNDauChargedMVASel"),
     ),
     userInts = cms.PSet(
      Ecounter = cms.InputTag("BoostedTauIsoCorrectionTool:Ecounter"),
      Mcounter = cms.InputTag("BoostedTauIsoCorrectionTool:Mcounter"),
     ),

     #userCands = cms.PSet(
        #jetForLepJetVar = cms.InputTag("ptRatioRelForMu:jetForLepJetVar") # warning: Ptr is null if no match is found
     #),
)

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
       ###This is what I am adding for electron variables
       ForEtauSumChargedHadronPt = Var("userFloat('ForEtauSumChargedHadronPt')",float,doc="Tau contamination, SumChargedHadronPt,  in the matched electron cone"),
       ForEtauSumPhotonEt = Var("userFloat('ForEtauSumPhotonEt')",float,doc="Tau contamination, SumPhotonEt,  in the matched electron cone"),
       ForEtauSumNeutralHadronEt = Var("userFloat('ForEtauSumNeutralHadronEt')",float,doc="Tau contamination, SumNeutralHadronEt,  in the matched electron cone"),
       ESumChargedHadronPt = Var("userFloat('ESumChargedHadronPt')",float,doc="Matched Electron's SumChargedHadronPt"),
       ESumNeutralHadronEt = Var("userFloat('ESumNeutralHadronEt')",float,doc="Matched Electron's SumNeutralHadronEt"),
       ESumPhotonEt = Var("userFloat('ESumPhotonEt')",float,doc="Matched Electron's SumPhotonEt"),
       Erho = Var("userFloat('Erho')",float,doc="Matched Electron's rho"),
       Eea = Var("userFloat('Eea')",float,doc="Matched Electron's Effective Area"),
       Ecounter = Var("userInt('Ecounter')",int,doc="Number of electrons that passed the ID and the delta R requirements"),
       EmatchedPt = Var("userFloat('EmatchedPt')",float,doc="Matched Electron's Pt"),
       EmatchedEta = Var("userFloat('EmatchedEta')",float,doc="Matched Electron's Eta"),
       EmatchedPhi = Var("userFloat('EmatchedPhi')",float,doc="Matched Electron's Phi"),
       EmatchedMass = Var("userFloat('EmatchedMass')",float,doc="Matched Electron's Mass"),

       ###This is what I am adding for muon variables
       ForMtauSumChargedHadronPt = Var("userFloat('ForMtauSumChargedHadronPt')",float,doc="Tau contamination, SumChargedHadronPt,  in the matched muon cone"),
       ForMtauSumPhotonEt = Var("userFloat('ForMtauSumPhotonEt')",float,doc="Tau contamination, SumPhotonEt,  in the matched muon cone"),
       ForMtauSumNeutralHadronEt = Var("userFloat('ForMtauSumNeutralHadronEt')",float,doc="Tau contamination, SumNeutralHadronEt,  in the matched muon cone"),
       MSumChargedHadronPt = Var("userFloat('MSumChargedHadronPt')",float,doc="Tau contamination, SumChargedHadronPt,  in the matched muon cone"),
       MSumNeutralHadronEt = Var("userFloat('MSumNeutralHadronEt')",float,doc="Tau contamination, SumNeutralHadronEt,  in the matched muon cone"),
       MSumPhotonEt = Var("userFloat('MSumPhotonEt')",float,doc="Tau contamination, SumPhotonEt,  in the matched muon cone"),
       MsumPUPt = Var("userFloat('MsumPUPt')",float,doc="Tau contamination, sumPUPt,  in the matched muon cone"),
       Mcounter = Var("userInt('Mcounter')",int,doc="Number of muons that passed the Loose ID and the delta R < 0.4 and > 0.02 requirements"),
       MmatchedPt = Var("userFloat('MmatchedPt')",float,doc="Matched muon's Pt"),
       MmatchedEta = Var("userFloat('MmatchedEta')",float,doc="Matched muon's Eta"),
       MmatchedPhi =  Var("userFloat('MmatchedPhi')",float,doc="Matched muon's Phi"),
       MmatchedMass = Var("userFloat('MmatchedMass')",float,doc="Matched muon's Mass"),       
       #SumChargedHadronPt = Var("userFloat('SumChargedHadronPt')",float,doc="photon pf info"), 
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

boostedTauTable.variables = _boostedTauVarsBase


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


boostedTauSequence = cms.Sequence( BoostedTauIsoCorrectionTool + slimmedboostedTauWithUserData + finalBoostedTaus)
#boostedTauIsoSequence = cms.Sequence(electronIsoCorrectionTool)
boostedTauTables = cms.Sequence( boostedTauTable)
boostedTauMC = cms.Sequence( boostedTausMCMatchLepTauForTable + boostedTausMCMatchHadTauForTable + boostedTauMCTable)

