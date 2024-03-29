import rsa

import cons

def getKeys(sender,receiver):
    MyKey = loadMyPrivateKey(sender)
    RKey = loadKeyReceiver(receiver)
    # print('ffffffffffffffffffffff')
    # print(RKey)
    return MyKey , RKey

def generateKeys(login):
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open(cons.PUB_KEYS+login+'.key', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open(cons.PRV_KEYS+login+'.key', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadKeyReceiver(login): # receiver's login
    with open(cons.PUB_KEYS+login+'.key', 'rb') as p:
        # publicKey = rsa.PublicKey.load_pkcs1(p.read(),
        
        # 'PEM')
        publicKey=p.read()
        # print('123456')

    return publicKey

def loadMyPrivateKey(login): # sender's login

    with open(cons.PRV_KEYS+login+'.key', 'rb') as p:
        # privateKey = rsa.PrivateKey.load_pkcs1(p.read())
        privateKey=p.read()
    return privateKey

def encrypt(message, key):
    return rsa.encrypt(message.encode("UTF-8"), key)

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode("UTF-8")
    except:
        return False


generateKeys("salma")
generateKeys("amira")