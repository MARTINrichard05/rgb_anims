import configparser
from multiprocessing import Process
from time import sleep
import os

class Main:
    def __init__(self):
        print("Starting")
        self.config = configparser.ConfigParser()
        self.generaltimer = 0
        self.buffer = {'script_name': 'rgb_keypress'}
        self.cfg_ready = {'script_name': 'rgb_keypress'}
        try:
            os.listdir().index('config.ini')  # if it finds the file , then do nothing
            print('config.ini found')
        except:
            print('no config.ini found')
            self.reset_config()  # if th file is not here juste create new one
            print('config.ini generated successfully')
        #self.readconfig()
        self.main()

    def reset_config(self):
        config = configparser.ConfigParser()
        config['DEFAULT'] = self.cfg_ready  # default values
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def getfromcfg(self, value):  # get a value from config file
        print(value)
        if len(self.config.sections()) == 0:  # if there is only a default section
            return self.config['DEFAULT'][value]
        else:
            return self.config[str(self.config.sections()[0])][value]

    def readconfig(self):
        self.config.read('config.ini')  # reloading the config file in cache
        # next step is to refresh the values in the cfg_ready dict to be faster to acess
        buffer = list(self.cfg_ready.keys())
        for i in range(len(buffer)):
            self.cfg_ready[buffer[i]] = self.getfromcfg(buffer[i])

    def run_animation(self):
        print("Fetching animation")
        exec("from scripts import " + self.cfg_ready['script_name'])

    def main(self):
        animation = Process(target=self.run_animation)
        animation.start()
        while True:
            #self.readconfig()
            print("stututu")
            if self.buffer['script_name'] != self.cfg_ready['script_name']:
                self.buffer['script_name'] = self.cfg_ready['script_name']
                try:
                    animation.kill()
                except:
                    pass
                print("creating Thread")
                animation = Process(target=self.run_animation)
                animation.start()
            else:
                sleep(1)
a = Main()
