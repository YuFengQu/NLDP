print "Begin PythonTest.py"

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
PIECalibration_strInputFile = 'F:/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1.tiff'
PIECalibration_strXMLFile = 'F:/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1.xml'
PIECalibration_nCalibrationType = '200'
PIECalibration_strOutputFile = 'F:/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/ExportFile/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1-Calibration.tiff'

PIECalibration_param = '{'
PIECalibration_param += '"strInputFile":"'
PIECalibration_param += PIECalibration_strInputFile
PIECalibration_param += '", '

PIECalibration_param += '"strXMLFile":"'
PIECalibration_param += PIECalibration_strXMLFile
PIECalibration_param += '", '

PIECalibration_param += '"nCalibrationType":"'
PIECalibration_param += PIECalibration_nCalibrationType
PIECalibration_param += '", '

PIECalibration_param += '"strOutputFile":"'
PIECalibration_param += PIECalibration_strOutputFile

PIECalibration_param += '"}'
print "PIECalibration_param = " + PIECalibration_param

#Execute
PIECalibration_result = PIEAlgo.ExcuteAlgoObj("PIECalibration", PIECalibration_param)
print PIECalibration_result

print "==========End PIECalibration=========="


#AtmosphericCorrection
print "==========Begin AtmosphericCorrection=========="

#Init Parameters
AtmosphericCorrection_nDataType = '3'
AtmosphericCorrection_strInputFile = 'F:/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/ExportFile/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1-Calibration.tiff'
AtmosphericCorrection_strInputXML = 'F:/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/ExportFile/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1-Calibration.xml'
AtmosphericCorrection_nAtmModel = '0'
AtmosphericCorrection_nAerosolType = '1'
AtmosphericCorrection_fInitialVIS = '40.0'
AtmosphericCorrection_nAeroRetrieval = '1'
AtmosphericCorrection_strOutputSR = 'F:/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/ExportFile/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1-Atmospheric.tiff'

AtmosphericCorrection_param = '{'
AtmosphericCorrection_param += '"nDataType":"'
AtmosphericCorrection_param += AtmosphericCorrection_nDataType
AtmosphericCorrection_param += '", '

AtmosphericCorrection_param += '"strInputFile":"'
AtmosphericCorrection_param += AtmosphericCorrection_strInputFile
AtmosphericCorrection_param += '", '

AtmosphericCorrection_param += '"strInputXML":"'
AtmosphericCorrection_param += AtmosphericCorrection_strInputXML
AtmosphericCorrection_param += '", '

AtmosphericCorrection_param += '"nAtmModel":"'
AtmosphericCorrection_param += AtmosphericCorrection_nAtmModel
AtmosphericCorrection_param += '", '

AtmosphericCorrection_param += '"nAerosolType":"'
AtmosphericCorrection_param += AtmosphericCorrection_nAerosolType
AtmosphericCorrection_param += '", '

AtmosphericCorrection_param += '"fInitialVIS":"'
AtmosphericCorrection_param += AtmosphericCorrection_fInitialVIS
AtmosphericCorrection_param += '", '

AtmosphericCorrection_param += '"nAeroRetrieval":"'
AtmosphericCorrection_param += AtmosphericCorrection_nAeroRetrieval
AtmosphericCorrection_param += '", '

AtmosphericCorrection_param += '"strOutputSR":"'
AtmosphericCorrection_param += AtmosphericCorrection_strOutputSR

AtmosphericCorrection_param += '"}'
print "AtmosphericCorrection_param = " + AtmosphericCorrection_param

#Execute
AtmosphericCorrection_result = PIEAlgo.ExcuteAlgoObj("AtmosphericCorrection", AtmosphericCorrection_param)
print AtmosphericCorrection_result

print "==========End AtmosphericCorrection=========="


#PIEOrtho
print "==========Begin PIEOrtho=========="

#Init Parameters
PIEOrtho_strSrcFileName = 'F:/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/ExportFile/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1-Atmospheric.tiff'
PIEOrtho_strRPCFileName = 'F:/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/ExportFile/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1-Atmospheric.rpb'
PIEOrtho_strGcpFileName = ''
PIEOrtho_strOutputFile = 'F:/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/ExportFile/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1-ortho.tif'
PIEOrtho_strDestWKT = 'GEOGCS[\\"WGS 84\\",DATUM[\\"WGS_1984\\",SPHEROID[\\"WGS 84\\",6378137,298.257223563, AUTHORITY[\\"EPSG\\",\\"7030\\"]], TOWGS84[0,0,0,0,0,0,0], AUTHORITY[\\"EPSG\\",\\"6326\\"]], PRIMEM[\\"Greenwich\\",0, AUTHORITY[\\"EPSG\\",\\"8901\\"]], UNIT[\\"degree\\",0.0174532925199433, AUTHORITY[\\"EPSG\\",\\"9108\\"]], AUTHORITY[\\"EPSG\\",\\"4326\\"]]'
PIEOrtho_fConstDem = '340'
PIEOrtho_strDemfile = ''
PIEOrtho_lImageResampling = '0'
PIEOrtho_fOutPixelX = '0.000080'
PIEOrtho_fOutPixelY = '0.000080'

PIEOrtho_param = '{'
PIEOrtho_param += '"strSrcFileName":"'
PIEOrtho_param += PIEOrtho_strSrcFileName
PIEOrtho_param += '", '

PIEOrtho_param += '"strRPCFileName":"'
PIEOrtho_param += PIEOrtho_strRPCFileName
PIEOrtho_param += '", '

PIEOrtho_param += '"strGcpFileName":"'
PIEOrtho_param += PIEOrtho_strGcpFileName
PIEOrtho_param += '", '

PIEOrtho_param += '"strOutputFile":"'
PIEOrtho_param += PIEOrtho_strOutputFile
PIEOrtho_param += '", '

PIEOrtho_param += '"strDestWKT":"'
PIEOrtho_param += PIEOrtho_strDestWKT
PIEOrtho_param += '", '

PIEOrtho_param += '"fConstDem":"'
PIEOrtho_param += PIEOrtho_fConstDem
PIEOrtho_param += '", '

PIEOrtho_param += '"strDemfile":"'
PIEOrtho_param += PIEOrtho_strDemfile
PIEOrtho_param += '", '

PIEOrtho_param += '"lImageResampling":"'
PIEOrtho_param += PIEOrtho_lImageResampling
PIEOrtho_param += '", '

PIEOrtho_param += '"fOutPixelX":"'
PIEOrtho_param += PIEOrtho_fOutPixelX
PIEOrtho_param += '", '

PIEOrtho_param += '"fOutPixelY":"'
PIEOrtho_param += PIEOrtho_fOutPixelY

PIEOrtho_param += '"}'
print "PIEOrtho_param = " + PIEOrtho_param

#Execute
PIEOrtho_result = PIEAlgo.ExcuteAlgoObj("PIEOrtho", PIEOrtho_param)
print PIEOrtho_result

print "==========End PIEOrtho=========="


#ImageClip
print "==========Begin ImageClip=========="

#Init Parameters
ImageClip_strInputFile = 'F:/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/ExportFile/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1-ortho.tif'
ImageClip_lXStart = '0'
ImageClip_lXEnd = '6260'
ImageClip_lYStart = '0'
ImageClip_lYEnd = '4860'
ImageClip_strShpFile = ''
ImageClip_strOutputFile = 'F:/work2015/data/gaofen/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600/ExportFile/GF1_PMS1_E116.5_N39.4_20131127_L1A0000117600-MSS1-ImageClip.tif'

ImageClip_param = '{'
ImageClip_param += '"strInputFile":"'
ImageClip_param += ImageClip_strInputFile
ImageClip_param += '", '

ImageClip_param += '"lXStart":"'
ImageClip_param += ImageClip_lXStart
ImageClip_param += '", '

ImageClip_param += '"lXEnd":"'
ImageClip_param += ImageClip_lXEnd
ImageClip_param += '", '

ImageClip_param += '"lYStart":"'
ImageClip_param += ImageClip_lYStart
ImageClip_param += '", '

ImageClip_param += '"lYEnd":"'
ImageClip_param += ImageClip_lYEnd
ImageClip_param += '", '

ImageClip_param += '"strShpFile":"'
ImageClip_param += ImageClip_strShpFile
ImageClip_param += '", '

ImageClip_param += '"strOutputFile":"'
ImageClip_param += ImageClip_strOutputFile

ImageClip_param += '"}'
print "ImageClip_param = " + ImageClip_param

#Execute
ImageClip_result = PIEAlgo.ExcuteAlgoObj("ImageClip", ImageClip_param)
print ImageClip_result

print "==========End ImageClip=========="


print "End PythonTest.py"
