from pb_py import main as API
from os import listdir
from os.path import isfile, join

HOST = 'aiaas.pandorabots.com'
USER_KEY = "b59cb68824a509016ac6dadbbbfa54c4"
APP_ID = "1409613156857"

def create_a_bot(botname):
    return API.create_bot(USER_KEY, APP_ID, HOST, botname)

def get_bot_list():
    return API.list_bots(USER_KEY, APP_ID, HOST)

def delete_a_bot(botname):
    return API.delete_bot(USER_KEY, APP_ID, HOST, botname)

def upload_a_file(botname, filename):
    return API.upload_file(USER_KEY, APP_ID, HOST, botname, filename)

def delete_a_file(botname, filename):
    return API.delete_file(USER_KEY, APP_ID, HOST, botname, filename)

def get_list_of_files(botname):
    return API.list_files(USER_KEY, APP_ID, HOST, botname)

def compile(botname):
    return API.compile_bot(USER_KEY, APP_ID, HOST, botname)

if __name__ == "__main__":

    botname = "hackbot"

    # create a bot
    text = create_a_bot(botname)
    print(text)

    # upload aiml files
    onlyfiles = [f for f in listdir("./lib/aiml/") if isfile(join("./lib/aiml/", f))]
    for file in onlyfiles:
        print(file)
        text = upload_a_file("testbot", "./lib/aiml/" + file)
        print(text)

    # compile bot
    text = compile(botname)
