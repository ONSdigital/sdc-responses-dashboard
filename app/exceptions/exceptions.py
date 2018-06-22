class ApiError(Exception):

    def __init__(self, message):
        super(ApiError, self).__init__(message)
        self.message = message


class UnknownSurveyError(Exception):

    def __init__(self, message, survey_id):
        super(UnknownSurveyError, self).__init__(message, survey_id)
        self.message = message
        self.survey_id = survey_id
