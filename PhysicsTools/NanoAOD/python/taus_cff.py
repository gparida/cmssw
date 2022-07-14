import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *
from PhysicsTools.NanoAOD.nano_eras_cff import *
from PhysicsTools.JetMCAlgos.TauGenJets_cfi import tauGenJets
from PhysicsTools.JetMCAlgos.TauGenJetsDecayModeSelectorAllHadrons_cfi import tauGenJetsSelectorAllHadrons 

##################### Updated tau collection with MVA-based tau-Ids rerun #######
# Used only in some eras
from PhysicsTools.NanoAOD.taus_updatedMVAIds_cff import *
from bbtautauAnalysisScripts.TauIsoCorrectionTool.TauIsoCorrectionTool_cfi import *
TauIsoCorrectionTool.TauCollection  = cms.InputTag("slimmedTausUpdated")
TauIsoCorrectionTool.muonCollection  = cms.InputTag("slimmedMuonsUpdated")

##################### User floats producers, selectors ##########################


finalTaus = cms.EDFilter("PATTauRefSelector",
    src = cms.InputTag("slimmedTauWithUserData"),
    cut = cms.string("pt > 18")
    #cut = cms.string("pt > 18 && tauID('decayModeFindingNewDMs') && (tauID('byLooseCombinedIsolationDeltaBetaCorr3Hits') || (tauID('chargedIsoPtSumdR03')+max(0.,tauID('neutralIsoPtSumdR03')-0.072*tauID('puCorrPtSum'))<2.5) || tauID('byVVVLooseDeepTau2017v2p1VSjet'))")
)

slimmedTauWithUserData = cms.EDProducer("PATTauUserDataEmbedder",
     src = cms.InputTag("slimmedTausUpdated"),
     userFloats = cms.PSet(
        ForEtauSumChargedHadronPt = cms.InputTag("TauIsoCorrectionTool:ForEtauSumChargedHadronPt"),
        ForEtauSumPhotonEt = cms.InputTag("TauIsoCorrectionTool:ForEtauSumPhotonEt"),
        ForEtauSumNeutralHadronEt = cms.InputTag("TauIsoCorrectionTool:ForEtauSumNeutralHadronEt"),
        ESumChargedHadronPt = cms.InputTag("TauIsoCorrectionTool:ESumChargedHadronPt"),
        ESumNeutralHadronEt = cms.InputTag("TauIsoCorrectionTool:ESumNeutralHadronEt"),
        ESumPhotonEt = cms.InputTag("TauIsoCorrectionTool:ESumPhotonEt"),
        Erho = cms.InputTag("TauIsoCorrectionTool:Erho"),
        Eea = cms.InputTag("TauIsoCorrectionTool:Eea"),
        #Ecounter = cms.InputTag("TauIsoCorrectionTool:Ecounter"),
        EmatchedPt = cms.InputTag("TauIsoCorrectionTool:EmatchedPt"),
        EmatchedEta = cms.InputTag("TauIsoCorrectionTool:EmatchedEta"),
        EmatchedPhi = cms.InputTag("TauIsoCorrectionTool:EmatchedPhi"),
        EmatchedMass = cms.InputTag("TauIsoCorrectionTool:EmatchedMass"),
        ##############################################################################
        ForMtauSumChargedHadronPt = cms.InputTag("TauIsoCorrectionTool:ForMtauSumChargedHadronPt"),
        ForMtauSumPhotonEt = cms.InputTag("TauIsoCorrectionTool:ForMtauSumPhotonEt"),
        ForMtauSumNeutralHadronEt = cms.InputTag("TauIsoCorrectionTool:ForMtauSumNeutralHadronEt"),
        MSumChargedHadronPt = cms.InputTag("TauIsoCorrectionTool:MSumChargedHadronPt"),
        MSumNeutralHadronEt = cms.InputTag("TauIsoCorrectionTool:MSumNeutralHadronEt"),
        MSumPhotonEt = cms.InputTag("TauIsoCorrectionTool:MSumPhotonEt"),
        MsumPUPt = cms.InputTag("TauIsoCorrectionTool:MsumPUPt"),
        #Mcounter = cms.InputTag("TauIsoCorrectionTool:Mcounter"),
        MmatchedPt = cms.InputTag("TauIsoCorrectionTool:MmatchedPt"),
        MmatchedEta = cms.InputTag("TauIsoCorrectionTool:MmatchedEta"),
        MmatchedPhi = cms.InputTag("TauIsoCorrectionTool:MmatchedPhi"),
        MmatchedMass = cms.InputTag("TauIsoCorrectionTool:MmatchedMass"),

        #miniIsoChg = cms.InputTag("isoForMu:miniIsoChg"),
        #miniIsoAll = cms.InputTag("isoForMu:miniIsoAll"),
        #TauCorrPfIso = cms.InputTag("muonIsoCorrectionTool:TauCorrPfIso"),
        #ptRatio = cms.InputTag("ptRatioRelForMu:ptRatio"),
        #ptRel = cms.InputTag("ptRatioRelForMu:ptRel"),
        #jetNDauChargedMVASel = cms.InputTag("ptRatioRelForMu:jetNDauChargedMVASel"),
     ),
     userInts = cms.PSet(
      Ecounter = cms.InputTag("TauIsoCorrectionTool:Ecounter"),
      Mcounter = cms.InputTag("TauIsoCorrectionTool:Mcounter"),
     ),
     #userCands = cms.PSet(
        #jetForLepJetVar = cms.InputTag("ptRatioRelForMu:jetForLepJetVar") # warning: Ptr is null if no match is found
     #),
)





for era in [run2_nanoAOD_94XMiniAODv2, run2_nanoAOD_94X2016, run2_nanoAOD_102Xv1, run2_nanoAOD_106Xv1]:
    era.toModify(finalTaus,
		 cut = cms.string("pt > 18")
                 #cut = cms.string("pt > 18 && tauID('decayModeFindingNewDMs') && (tauID('byLooseCombinedIsolationDeltaBetaCorr3Hits') || tauID('byVLooseIsolationMVArun2v1DBoldDMwLT2015') || tauID('byVLooseIsolationMVArun2v1DBnewDMwLT') || tauID('byVLooseIsolationMVArun2v1DBdR03oldDMwLT') || tauID('byVVLooseIsolationMVArun2v1DBoldDMwLT') || tauID('byVVLooseIsolationMVArun2v1DBoldDMwLT2017v2') || tauID('byVVLooseIsolationMVArun2v1DBnewDMwLT2017v2') || tauID('byVVLooseIsolationMVArun2v1DBdR03oldDMwLT2017v2') || tauID('byVVVLooseDeepTau2017v2p1VSjet'))")
    )
for era in [run2_nanoAOD_94XMiniAODv1,]:
    era.toModify(finalTaus,
		 cut = cms.string("pt > 18")
                 #cut = cms.string("pt > 18 && tauID('decayModeFindingNewDMs') && (tauID('byLooseCombinedIsolationDeltaBetaCorr3Hits') || tauID('byVLooseIsolationMVArun2v1DBoldDMwLT') || tauID('byVLooseIsolationMVArun2v1DBnewDMwLT') || tauID('byVLooseIsolationMVArun2v1DBdR03oldDMwLT') || tauID('byVVLooseIsolationMVArun2v1DBoldDMwLT2017v1') || tauID('byVVLooseIsolationMVArun2v1DBoldDMwLT2017v2') || tauID('byVVLooseIsolationMVArun2v1DBnewDMwLT2017v2') || tauID('byVVLooseIsolationMVArun2v1DBdR03oldDMwLT2017v2') || tauID('byVVVLooseDeepTau2017v2p1VSjet'))")
    )
run2_miniAOD_80XLegacy.toModify(finalTaus,
                                     src = cms.InputTag("slimmedTaus"),
                                     cut =  cms.string("pt > 18")
				     #cut =  cms.string("pt > 18 && tauID('decayModeFindingNewDMs') && (tauID('byLooseCombinedIsolationDeltaBetaCorr3Hits') || tauID('byVLooseIsolationMVArun2v1DBoldDMwLT') || tauID('byVLooseIsolationMVArun2v1DBnewDMwLT') || tauID('byVLooseIsolationMVArun2v1DBdR03oldDMwLT'))")
    )

##################### Tables for final output and docs ##########################
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

tauTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("linkedObjects","taus"),
    cut = cms.string(""), #we should not filter on cross linked collections
    name= cms.string("Tau"),
    doc = cms.string("slimmedTaus after basic selection (" + finalTaus.cut.value()+")"),
    singleton = cms.bool(False), # the number of entries is variable
    extension = cms.bool(False), # this is the main table for the taus
    variables = cms.PSet() # PSet defined below in era dependent way
)
_tauVarsBase = cms.PSet(P4Vars,
       charge = Var("charge", int, doc="electric charge"),
       jetIdx = Var("?hasUserCand('jet')?userCand('jet').key():-1", int, doc="index of the associated jet (-1 if none)"),
       decayMode = Var("decayMode()",int),
       idDecayModeOldDMs = Var("tauID('decayModeFinding')", bool),

       leadTkPtOverTauPt = Var("leadChargedHadrCand.pt/pt ",float, doc="pt of the leading track divided by tau pt",precision=10),
       leadTkDeltaEta = Var("leadChargedHadrCand.eta - eta ",float, doc="eta of the leading track, minus tau eta",precision=8),
       leadTkDeltaPhi = Var("deltaPhi(leadChargedHadrCand.phi, phi) ",float, doc="phi of the leading track, minus tau phi",precision=8),

       dxy = Var("leadChargedHadrCand().dxy()",float, doc="d_{xy} of lead track with respect to PV, in cm (with sign)",precision=10),
       dz = Var("leadChargedHadrCand().dz()",float, doc="d_{z} of lead track with respect to PV, in cm (with sign)",precision=14),

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
       MSumChargedHadronPt = Var("userFloat('MSumChargedHadronPt')",float,doc="Matched Muon's SumChargedHadronPt"),
       MSumNeutralHadronEt = Var("userFloat('MSumNeutralHadronEt')",float,doc="Matched Muon's SumNeutralHadronEt"),
       MSumPhotonEt = Var("userFloat('MSumPhotonEt')",float,doc="Matched Muon's SumPhotonEt"),
       MsumPUPt = Var("userFloat('MsumPUPt')",float,doc="Matched Muon's sumPUPt"),
       Mcounter = Var("userInt('Mcounter')",int,doc="Number of muons that passed the Loose ID and the delta R < 0.4 and > 0.02 requirements"),
       MmatchedPt = Var("userFloat('MmatchedPt')",float,doc="Matched muon's Pt"),
       MmatchedEta = Var("userFloat('MmatchedEta')",float,doc="Matched muon's Eta"),
       MmatchedPhi =  Var("userFloat('MmatchedPhi')",float,doc="Matched muon's Phi"),
       MmatchedMass = Var("userFloat('MmatchedMass')",float,doc="Matched muon's Mass"), 

       # these are too many, we may have to suppress some
       rawIso = Var( "tauID('byCombinedIsolationDeltaBetaCorrRaw3Hits')", float, doc = "combined isolation (deltaBeta corrections)", precision=10),
       rawIsodR03 = Var( "(tauID('chargedIsoPtSumdR03')+max(0.,tauID('neutralIsoPtSumdR03')-0.072*tauID('puCorrPtSum')))", float, doc = "combined isolation (deltaBeta corrections, dR=0.3)", precision=10),
       chargedIso = Var( "tauID('chargedIsoPtSum')", float, doc = "charged isolation", precision=10),
       neutralIso = Var( "tauID('neutralIsoPtSum')", float, doc = "neutral (photon) isolation", precision=10),
       puCorr = Var( "tauID('puCorrPtSum')", float, doc = "pileup correction", precision=10),
       photonsOutsideSignalCone = Var( "tauID('photonPtSumOutsideSignalCone')", float, doc = "sum of photons outside signal cone", precision=10),

       idAntiMu = _tauId2WPMask("againstMuon%s3", doc= "Anti-muon discriminator V3: "),
       idAntiEleDeadECal = Var("tauID('againstElectronDeadECALForNano')", bool, doc = "Anti-electron dead-ECal discriminator"),

#   isoCI3hit = Var(  "tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits")" doc="byCombinedIsolationDeltaBetaCorrRaw3Hits raw output discriminator"),
#   photonOutsideSigCone = Var( "tauID("photonPtSumOutsideSignalCone")" doc="photonPtSumOutsideSignalCone raw output discriminator"),

)

_mvaIsoVars2015 = cms.PSet(
    rawMVAnewDM = Var( "tauID('byIsolationMVArun2v1DBnewDMwLTraw')",float, doc="byIsolationMVArun2v1DBoldDMwLT raw output discriminator (2015)",precision=10),
    rawMVAoldDM = Var( "tauID('byIsolationMVArun2v1DBoldDMwLTraw')",float, doc="byIsolationMVArun2v1DBoldDMwLT raw output discriminator (2015)",precision=10),
    rawMVAoldDMdR03 = Var( "tauID('byIsolationMVArun2v1DBdR03oldDMwLTraw')",float, doc="byIsolationMVArun2v1DBoldDMwLT raw output discriminator (2015)",precision=10),
    idMVAnewDM = _tauId6WPMask( "by%sIsolationMVArun2v1DBnewDMwLT", doc="IsolationMVArun2v1DBnewDMwLT ID working point (2015)"),
    idMVAoldDM = _tauId6WPMask( "by%sIsolationMVArun2v1DBoldDMwLT", doc="IsolationMVArun2v1DBoldDMwLT ID working point (2015)"),
    idMVAoldDMdR03 = _tauId6WPMask( "by%sIsolationMVArun2v1DBdR03oldDMwLT", doc="IsolationMVArun2v1DBoldDMdR0p3wLT ID working point (2015)")
)
_mvaIsoVars2015Reduced = cms.PSet(
    rawMVAoldDM = Var( "tauID('byIsolationMVArun2v1DBoldDMwLTraw2015')",float, doc="byIsolationMVArun2v1DBoldDMwLT raw output discriminator (2015)",precision=10),
    idMVAoldDM = _tauId6WPMask( "by%sIsolationMVArun2v1DBoldDMwLT2015", doc="IsolationMVArun2v1DBoldDMwLT ID working point (2015)"),
)
_mvaIsoVars2017v1 = cms.PSet(
    rawMVAoldDM2017v1 = Var( "tauID('byIsolationMVArun2v1DBoldDMwLTraw')",float, doc="byIsolationMVArun2v1DBoldDMwLT raw output discriminator (2017v1)",precision=10),
    idMVAoldDM2017v1 = _tauId7WPMask( "by%sIsolationMVArun2v1DBoldDMwLT", doc="IsolationMVArun2v1DBoldDMwLT ID working point (2017v1)")
)
_mvaIsoVars2017v2 = cms.PSet(
    rawMVAnewDM2017v2 = Var( "tauID('byIsolationMVArun2v1DBnewDMwLTraw2017v2')",float, doc="byIsolationMVArun2v1DBnewDMwLT raw output discriminator (2017v2)",precision=10),
    rawMVAoldDM2017v2 = Var( "tauID('byIsolationMVArun2v1DBoldDMwLTraw2017v2')",float, doc="byIsolationMVArun2v1DBoldDMwLT raw output discriminator (2017v2)",precision=10),
    rawMVAoldDMdR032017v2 = Var( "tauID('byIsolationMVArun2v1DBdR03oldDMwLTraw2017v2')",float, doc="byIsolationMVArun2v1DBdR03oldDMwLT raw output discriminator (2017v2)",precision=10),
    idMVAnewDM2017v2 = _tauId7WPMask( "by%sIsolationMVArun2v1DBnewDMwLT2017v2", doc="IsolationMVArun2v1DBnewDMwLT ID working point (2017v2)"),
    idMVAoldDM2017v2 = _tauId7WPMask( "by%sIsolationMVArun2v1DBoldDMwLT2017v2", doc="IsolationMVArun2v1DBoldDMwLT ID working point (2017v2)"),
    idMVAoldDMdR032017v2 = _tauId7WPMask( "by%sIsolationMVArun2v1DBdR03oldDMwLT2017v2", doc="IsolationMVArun2v1DBoldDMdR0p3wLT ID working point (2017v2)")
)
_mvaAntiEVars2015 = cms.PSet(
       rawAntiEle = Var("tauID('againstElectronMVA6Raw')", float, doc= "Anti-electron MVA discriminator V6 raw output discriminator (2015)", precision=10),
       rawAntiEleCat = Var("tauID('againstElectronMVA6category')", int, doc="Anti-electron MVA discriminator V6 category (2015)"),
       idAntiEle = _tauId5WPMask("againstElectron%sMVA6", doc= "Anti-electron MVA discriminator V6 (2015)")
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
    _tauVarsBase,
    _deepTauVars2017v2p1
)
_variablesMiniV1 = cms.PSet(
    _variablesMiniV2,
    _mvaIsoVars2017v2
)
_variablesMiniV1.rawMVAoldDM = Var( "tauID('byIsolationMVArun2v1DBoldDMwLTraw')",float, doc="byIsolationMVArun2v1DBoldDMwLT raw output discriminator (2015)",precision=10)
_variablesMiniV1.rawMVAoldDM2017v1 = Var( "tauID('byIsolationMVArun2v1DBoldDMwLTraw2017v1')",float, doc="byIsolationMVArun2v1DBoldDMwLT raw output discriminator (2017v1)",precision=10)
_variablesMiniV1.idMVAoldDM = _tauId6WPMask( "by%sIsolationMVArun2v1DBoldDMwLT", doc="IsolationMVArun2v1DBoldDMwLT ID working point (2015)")
_variablesMiniV1.idMVAoldDM2017v1 = _tauId7WPMask( "by%sIsolationMVArun2v1DBoldDMwLT2017v1", doc="IsolationMVArun2v1DBoldDMwLT ID working point (2017v1)")
_variables80X =  cms.PSet(
    _tauVarsBase,
    _mvaAntiEVars2015,
    _mvaIsoVars2015
)

tauTable.variables = _variablesMiniV2

(run2_nanoAOD_92X | run2_nanoAOD_94XMiniAODv2 | run2_nanoAOD_94X2016 | run2_nanoAOD_102Xv1 | run2_nanoAOD_106Xv1).toModify(tauTable,
                 variables = cms.PSet(tauTable.variables, _mvaIsoVars2015Reduced, _mvaIsoVars2017v1, _mvaIsoVars2017v2)
    )
for era in [run2_nanoAOD_94XMiniAODv1,]:
    era.toModify(tauTable,
                 variables = _variablesMiniV1
    )
run2_miniAOD_80XLegacy.toModify(tauTable,
                                variables = _variables80X
)
for era in [run2_nanoAOD_92X, run2_nanoAOD_94XMiniAODv1, run2_nanoAOD_94XMiniAODv2, \
            run2_nanoAOD_94X2016, run2_nanoAOD_102Xv1, run2_nanoAOD_106Xv1]:
    era.toModify(tauTable.variables,
                 rawAntiEle2018 = Var("tauID('againstElectronMVA6Raw2018')", float, doc= "Anti-electron MVA discriminator V6 raw output discriminator (2018)", precision=10),
                 rawAntiEleCat2018 = Var("tauID('againstElectronMVA6category2018')", int, doc="Anti-electron MVA discriminator V6 category (2018)"),
                 idAntiEle2018 = _tauId5WPMask("againstElectron%sMVA62018", doc= "Anti-electron MVA discriminator V6 (2018)"),
                 rawAntiEle = Var("tauID('againstElectronMVA6Raw')", float, doc= "Anti-electron MVA discriminator V6 raw output discriminator (2015)", precision=10),
                 rawAntiEleCat = Var("tauID('againstElectronMVA6category')", int, doc="Anti-electron MVA discriminator V6 category (2015"),
                 idAntiEle = _tauId5WPMask("againstElectron%sMVA6", doc= "Anti-electron MVA discriminator V6 (2015)")
)
for era in [run2_miniAOD_80XLegacy, run2_nanoAOD_92X, run2_nanoAOD_94XMiniAODv1, run2_nanoAOD_94XMiniAODv2, \
            run2_nanoAOD_94X2016, run2_nanoAOD_102Xv1, run2_nanoAOD_106Xv1]:
    era.toModify(tauTable.variables,
                 idDecayMode = Var("tauID('decayModeFinding')", bool),
                 idDecayModeNewDMs = Var("tauID('decayModeFindingNewDMs')", bool),
                 idDecayModeOldDMs = None
    )
run2_miniAOD_80XLegacy.toModify(tauTable.variables,
                                idAntiEleDeadECal = None
)
(run2_nanoAOD_106Xv2 | run2_miniAOD_devel).toModify(tauTable.variables,
                 idAntiEleDeadECal = Var("tauID('againstElectronDeadECAL')", bool, doc = "Anti-electron dead-ECal discriminator"),
)

tauGenJetsForNano = tauGenJets.clone(
    GenParticles = "finalGenParticles",
    includeNeutrinos = False
)
(run2_nanoAOD_106Xv1 & ~run2_nanoAOD_devel).toModify(tauGenJetsForNano, GenParticles = "prunedGenParticles")

tauGenJetsSelectorAllHadronsForNano = tauGenJetsSelectorAllHadrons.clone(
    src = "tauGenJetsForNano"
)

genVisTaus = cms.EDProducer("GenVisTauProducer",
    src = cms.InputTag("tauGenJetsSelectorAllHadronsForNano"),
    srcGenParticles = cms.InputTag("finalGenParticles")
)
(run2_nanoAOD_106Xv1 & ~run2_nanoAOD_devel).toModify(genVisTaus, srcGenParticles = "prunedGenParticles")

genVisTauTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("genVisTaus"),
    cut = cms.string("pt > 10."),
    name = cms.string("GenVisTau"),
    doc = cms.string("gen hadronic taus "),
    singleton = cms.bool(False), # the number of entries is variable
    extension = cms.bool(False), # this is the main table for generator level hadronic tau decays
    variables = cms.PSet(
         pt = Var("pt", float,precision=8),
         phi = Var("phi", float,precision=8),
         eta = Var("eta", float,precision=8),
         mass = Var("mass", float,precision=8),                           
	 charge = Var("charge", int),
	 status = Var("status", int, doc="Hadronic tau decay mode. 0=OneProng0PiZero, 1=OneProng1PiZero, 2=OneProng2PiZero, 10=ThreeProng0PiZero, 11=ThreeProng1PiZero, 15=Other"),
	 genPartIdxMother = Var("?numberOfMothers>0?motherRef(0).key():-1", int, doc="index of the mother particle"),
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


tauSequence = cms.Sequence(patTauMVAIDsSeq + TauIsoCorrectionTool + slimmedTauWithUserData + finalTaus)
_tauSequence80X =  cms.Sequence(finalTaus)
run2_miniAOD_80XLegacy.toReplaceWith(tauSequence,_tauSequence80X)
tauTables = cms.Sequence(tauTable)
genTauSequence = cms.Sequence(tauGenJetsForNano + tauGenJetsSelectorAllHadronsForNano + genVisTaus + genVisTauTable)
tauMC = cms.Sequence(genTauSequence + tausMCMatchLepTauForTable + tausMCMatchHadTauForTable + tauMCTable)

