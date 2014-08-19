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

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        #'file:myfile.root'
        #'file:/afs/cern.ch/cms/Tutorials/TWIKI_DATA/TTJets_8TeV_53X.root'
        ##'root://localhost//var/tmp/gowdy/patTuple_mini_ZH.root',
        ##'root://localhost//var/tmp/gowdy/patTuple_mini_ZH.root',
        ##'root://localhost//var/tmp/gowdy/patTuple_mini_ZH.root',
        ##'root://localhost//var/tmp/gowdy/patTuple_mini_ZH.root',
        ##'root://localhost//var/tmp/gowdy/patTuple_mini_ZH.root'
        ##'file:/var/tmp/gowdy/patTuple_mini_ZH.root',
        ##'file:/var/tmp/gowdy/patTuple_mini_ZH.root',
        ##'file:/var/tmp/gowdy/patTuple_mini_ZH.root',
        ##'file:/var/tmp/gowdy/patTuple_mini_ZH.root',
        'file:/var/tmp/gowdy/patTuple_mini_ZH.root'
    ),
    duplicateCheckMode = cms.untracked.string( "noDuplicateCheck" )
)

process.out = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( 'file:newFile.root' ),
    compressionLevel = cms.untracked.int32( 0 )
)

process.o = cms.EndPath( process.out )
