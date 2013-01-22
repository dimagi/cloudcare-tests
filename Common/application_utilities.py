from robot.api import logger
from robot.errors import DataError
from robot.libraries.BuiltIn import BuiltIn
			
def App_Get_Element_Text(locator):

		"""

        Retrive the given element text
        """
		logger.info("Retrive the element text")															## This info goes to the Log file
		seleniumlib = BuiltIn().get_library_instance('Selenium2Library')								## Creates an Instance of Selenium2Library
		element = seleniumlib._element_find(locator, True, True)										## Gets the Element by locator and stores into a variable 
		return  element.text																			## Returns the element text
		
def App_Verify_Alert_Present():
		seleniumlib = BuiltIn().get_library_instance('Selenium2Library')
		try:
			alert=seleniumlib._current_browser().switch_to_alert()
			text = ' '.join(alert.text.splitlines())
			return True
		except:
			return False
			
	
       

    