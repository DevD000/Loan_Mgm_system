

class PropertyUtil:

    @staticmethod
    def getPropertyString():
        SERVER_NAME = "DM"
        DATABASE_NAME = "LoanManagementSystem1"
        TRUSTED_CONNECTION = "Yes"
        CONNECTION_STRING = f"Driver={{SQL Server}}; Server={SERVER_NAME}; Database={DATABASE_NAME}; Trusted_Connection={TRUSTED_CONNECTION}"
        return CONNECTION_STRING