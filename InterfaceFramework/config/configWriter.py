import configparser

config = configparser.ConfigParser()
defaultConf = {
    'ServerAliveInterval': '45',
    'Compression': 'yes',
    'CompressionLevel': '9',
    'ForwardX11': 'yes'
}
config['DEFAULT'] = defaultConf

with open('example.ini', 'w') as configFile:
    config.write(configFile)