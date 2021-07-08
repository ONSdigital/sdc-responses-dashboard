class UnknownSurveyError(Exception):
    def __init__(self, message, survey_id):
        super().__init__(message, survey_id)
        self.message = message
        self.survey_id = survey_id


class MissingConfigError(Exception):
    def __init__(self, keys: set):
        super().__init__(keys)
        self.keys = keys


class APIConnectionError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
