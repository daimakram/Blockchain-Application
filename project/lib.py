import json
import hashlib
import os

blockchain_dir = os.curdir + '/blockchain/'

def get_blocks():
    print(os.curdir)
    block = os.listdir(blockchain_dir)
    print(block)
    #block=(block[0].split('.')[0])
    #print(block)
    return sorted([int(i.split('.')[0]) for i in block])
    
def get_hash(blockname):
    file = open(blockchain_dir + blockname + '.json', 'rb').read()
    return hashlib.sha256(file).hexdigest()

def create_block(payer,amount, payee, p_hash=""):
    blocks=get_blocks()
    last_block = blocks[-1]

    blockname = str(last_block + 1)
    p_hash = get_hash(str(last_block))
    data = {'payer':payer,
    'amount': amount,
    'payee': payee,
    'hash': p_hash}
    with open(blockchain_dir + blockname+ '.json', 'w') as file:
        json.dump(data, file, indent=4)

def verify():
    blocks = get_blocks()
    print(blocks)
    results = []
    for file in blocks[1:]:
        prev_h = json.load(open(blockchain_dir + str(file) + '.json')) ['hash']
        prev_b = str(file-1)
        true_h=get_hash(prev_b)

        if prev_h == true_h:
            res = 'genuine'
        else:
            res = 'fake'
        results.append({'block':prev_b, 'result': res})
        print(results)
    return results
def main():
    create_block('Jhon',1,'Adam')
    create_block('Ahmad',4,'Asim')
    create_block('Asim',3,'Daim')
    create_block('Dam',6,'Sam')

    result = verify()
    print(result)

if __name__ == '__main__':
    main()