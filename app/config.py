# application configurations
# general configurations
class Config():
    SECRET_KEY = "MR1VnMp6w1Wz&eV7s#V5btqYCRCCq@OW&iJzSxDD8$Tm63dzTi"
    # initialize applicaton
    def init_app(self):
        pass

# development configurations
class DevelopmentConfig(Config):
    PORT = 5001
    SERVER_NAME = "localhost:"+str(PORT)
    DEBUG = True 

# testing configurations
class TestingConfig(Config):
    PORT = 5002
    SERVER_NAME = "localhost:"+str(PORT)
    TESTING = True 

# configuration types
config = {
    'default':      DevelopmentConfig,
    'development':  DevelopmentConfig,
    'testing':      TestingConfig
}