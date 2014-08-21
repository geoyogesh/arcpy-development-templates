__author__ = 'Yogesh'

from arcpy import Parameter, CheckExtension

class ToolTwo(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool with parameters"
        self.description = "Simple Tool with parameters"
        # category/toolset
        self.category = 'Custom Category'
        # stylesheet
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        '''
        #First Parameter
        param0 = Parameter(
            name='in_features',
            displayName='Input Features',
            datatype='Feature Layer',
            parameterType='Required',
            direction='Input'
        )
        # set new parameter to a default value
        #in_features.value = defaultValue
        param0.filter.list = ['Point', 'Polyline', 'Polygon']
        params = [param0]
        '''
        #GPMultiValue:GPString
        #datatypes supported by arcgis server
        # GPBoolean,GPDouble,GPLong,GPString,GPDate,GPLinearUnit,GPDataFile,GPRasterData
        # GPRecordSet,GPRasterDataLayer,GPFeatureRecordSetLayer,GPRasterDataLayer,GPFeatureRecordSetLayer
        # GPMultiValue:GPString

        #featureset
        #recordset(Table)
        #raster
        #linear unit (100kms, 10 miles)
        #file(.ZIp, .KML, .XML)
        #INteger,long,Double
        #date
        #Boolean
        params = None
        return params


def isLicensed(self):
    """Set whether tool is licensed to execute."""
    #http://resources.arcgis.com/en/help/main/10.2/index.html#//002z0000000z000000
    '''
    try:
        if CheckExtension("Spatial") != "Available":
            return False
        else:
            return True
    except Exception:
        return False #False- Tool Cannot be executed
    '''
    return True


def updateParameters(self, parameters):
    """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

    '''
        set defualt values
        change parameter filter
        '''
    return


def updateMessages(self, parameters):
    """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""


    return


def execute(self, parameters, messages):
    """The source code of the tool."""
    
    try:
        pass
    except:
        # Get the traceback object
        error = True
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        # Concatenate information together concerning the error into a message string
        pymsg = 'PYTHON ERRORS:\nTraceback info:\n' + tbinfo + '\nError Info:\n' + str(sys.exc_info()[1])
        msgs = 'ArcPy ERRORS:\n' + arcpy.GetMessages() + '\n'
        # Return python error messages for use in script tool or Python Window
        arcpy.AddError(pymsg)
        arcpy.AddError(msgs)
        # Print Python error messages for use in Python / Python Window
        #print pymsg + "\n" #UPDATE
        print(pymsg + '\n')
        #print msgs #UPDATE
        print(msgs)
    
    
    '''
    try:
        if CheckExtension("Spatial") == "Available":
            arcpy.CheckOutExtension("Spatial")
        else:
            raise arcpy.LicenseError
        pass
    finally:
        arcpy.CheckInExtension("Spatial")
    '''
    
    return
