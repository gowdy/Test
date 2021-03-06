import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('Demo')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
    limit = cms.untracked.int32(-1)
)
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

myFileName = 'root://localhost//var/tmp/gowdy/newFile.root'
#'file:/var/tmp/gowdy/newFile.root'
#'file:/var/tmp/gowdy/patTuple_mini_ZH.root'
#'root://localhost//var/tmp/gowdy/patTuple_mini_ZH.root'
process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        myFileName, myFileName, myFileName, myFileName, myFileName
    ),
    duplicateCheckMode = cms.untracked.string( "noDuplicateCheck" )
)

process.demo = cms.EDAnalyzer('SelectiveReader',
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    muons = cms.InputTag("slimmedMuons"),
    electrons = cms.InputTag("slimmedElectrons"),
    taus = cms.InputTag("slimmedTaus"),
    photons = cms.InputTag("slimmedPhotons"),
    jets = cms.InputTag("slimmedJets"),
    fatjets = cms.InputTag("slimmedJetsCA8"),
    mets = cms.InputTag("slimmedMETs"),
    tracks = cms.InputTag("lostTracks"),
    packed = cms.InputTag("packedPFCandidates"),
    packedGen = cms.InputTag("packedGenParticles")
)


process.p = cms.Path(process.demo)
