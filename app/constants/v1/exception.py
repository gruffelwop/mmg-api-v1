import app.constants.v1.error as error_v1

class NameNotFoundException(Exception):
    error_v1.NAME_NOT_FOUND
    pass

class InvalidPlanCredentialsException(Exception):
    error_v1.INVALID_PLAN_CREDENTIALS
    pass

class InvalidPortalCredentialsException(Exception):
    error_v1.INVALID_PORTAL_CREDENTIALS
    pass

class InvalidAPICredentialsException(Exception):
    error_v1.INVALID_API_CREDENTIALS
    pass

class EmailAlreadyUsedException(Exception):
    error_v1.EMAIL_ALREADY_USED
    pass

class UsernameAlreadyUsedException(Exception):
    error_v1.USERNAME_ALREADY_USED
    pass
