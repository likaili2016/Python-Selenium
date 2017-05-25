import configparser

config = configparser.ConfigParser()

config.read('config.ini')
emailConf = config['email']
for key in emailConf:
    print(key + ':' + emailConf[key])