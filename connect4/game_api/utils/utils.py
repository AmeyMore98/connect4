from game_api.utils.constants import Constants

class Utils:

    @staticmethod
    def build_reponse(status, message, data=None):

        if data:
            return {
                Constants.STATUS: status,
                Constants.MESSAGE: message,
                Constants.DATA: data
            }
        
        return {
            Constants.STATUS: status,
            Constants.MESSAGE: message,
        }
