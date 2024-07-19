from random import random
def getHJ():
    ran=random();
    if ran > 0.5:
        return "짝"
    else:
        return "홀"
com = getHJ()
print("com",com)