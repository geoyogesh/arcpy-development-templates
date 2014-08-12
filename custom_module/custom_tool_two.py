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
        params = None
        return params


def isLicensed(self):
    """Set whether tool is licensed to execute."""
    #http://resources.arcgis.com/en/help/main/10.2/index.html#//002z0000000z000000
    '''
    try:
        if CheckExtension("3D") != "Available":
            raise Exception
    except Exception:
        return False # tool cannot be executed
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
    return