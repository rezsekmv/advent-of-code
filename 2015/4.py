import hashlib

inp='ckczppom'

p1=False
i=0
while True:
    h = hashlib.md5((inp+str(i)).encode())

    if h.hexdigest().startswith('00000') and not p1:
        p1=True
        print(i)
    if h.hexdigest().startswith('000000'):
        print(i)
        break
    i+=1
