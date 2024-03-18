print "Begin Example.py"

#Init Environment 
import sys
PIEV4_BIN = "F:/svn/PIE4.1/PIE_CPLUS/src/OutDir/Debug_Win32"
sys.path.append(PIEV4_BIN)
import PIEAlgo
import os
os.chdir(PIEV4_BIN)
print "PIEV4_BIN = " + PIEV4_BIN

#PIECalibration
print "==========Begin PIECalibration=========="

#Init Parameters
strInputFile = 'G:/work/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1.tiff'
strXMLFile = 'G:/work/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/temp/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1.xml'
nCalibrationType = 200
strOutputFile = 'G:/work/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/temp/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1_Calibration.tiff'

#Execute
result = PIEAlgo.PIECalibration(strInputFile, strXMLFile, nCalibrationType, strOutputFile)
print result

print "==========End PIECalibration=========="


#AtmosphericCorrection
print "==========Begin AtmosphericCorrection=========="

#Init Parameters
nDataType = 3
strInputFile = 'G:/work/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/temp/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1_Calibration.tiff'
strInputXML = 'G:/work/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/temp/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1_Calibration.xml'
nAtmModel = 0
nAerosolType = 1
fInitialVIS = 40.0
nAeroRetrieval = 1
strOutputSR = 'G:/work/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/temp/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1_Atmospheric.tiff'

#Execute
result = PIEAlgo.AtmosphericCorrection(nDataType, strInputFile, strInputFile, strInputXML, nAtmModel, nAerosolType, fInitialVIS, nAeroRetrieval, strOutputSR)
print result

print "==========End AtmosphericCorrection=========="


#PIEOrtho
print "==========Begin PIEOrtho=========="

#Init Parameters
strSrcFileName = 'G:/work/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/temp/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1_Atmospheric.tiff'
strRPCFileName = 'G:/work/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/temp/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1.rpb'
strGcpFileName = ''
strOutputFile = 'G:/work/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/temp/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1_ortho.tiff'
strDestWKT = 'GEOGCS[\\"WGS 84\\",DATUM[\\"WGS_1984\\",SPHEROID[\\"WGS 84\\",6378137,298.257223563, AUTHORITY[\\"EPSG\\",\\"7030\\"]], TOWGS84[0,0,0,0,0,0,0], AUTHORITY[\\"EPSG\\",\\"6326\\"]], PRIMEM[\\"Greenwich\\",0, AUTHORITY[\\"EPSG\\",\\"8901\\"]], UNIT[\\"degree\\",0.0174532925199433, AUTHORITY[\\"EPSG\\",\\"9108\\"]], AUTHORITY[\\"EPSG\\",\\"4326\\"]]'
fConstDem = 340
strDemfile = ''
lImageResampling = 0
fOutPixelX = 0.000080
fOutPixelY = 0.000080

#Execute
result = PIEOrtho(strSrcFileName, strRPCFileName, strGcpFileName, strOutputFile, strDestWKT, fConstDem, strDemfile, lImageResampling, fOutPixelX, fOutPixelY)
print result

print "==========End PIEOrtho=========="


#ImageClip
print "==========Begin ImageClip=========="

#Init Parameters
strInputFile = 'G:/work/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/temp/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1_ortho.tiff'
lXStart = 0
lXEnd = 6260
lYStart = 0
lYEnd = 4860
strShpFile = ''
strOutputFile = 'G:/work/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/temp/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1_ImageClip.tiff'

#Execute
result = PIEAlgo.ImageClip(strInputFile, lXStart, lXEnd, lYStart, lYEnd, strShpFile, strOutputFile)
print result

print "==========End ImageClip=========="


print "End Example.py"
