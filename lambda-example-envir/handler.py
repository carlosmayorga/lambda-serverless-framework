import os

def hello(event, context):
    return os.environ['FIRST_NAME']


def hello2(event, context):
    return os.environ['FIRST_NAME']
