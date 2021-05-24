from time import time 
import json 
import hashlib

class Blockchain(object):
    def __init__(self):
    	self.chain = [self.addGenesisBlock()]


    def getLastBlock(self):
    	return self.chain[-1]

    def addBlock(self, block):
    	if(len(self.chain) > 0):
    		block.prev = self.getLastBlock().hash
    	else:
    		block.prev = 'none'
    	self.chain.append(block)

    #This  is the first block of the blockchain that is added to it 
    # The transaction always don't reflect real transaction
    def addGenesisBlock(self):
    	tArr = [];
    	tArr.append(Transaction("me","you",10))
    	genesis = Block(tArr, time(),0);
    	genesis.prev = "None";
    	return genesis;
    def chainJSONencode(self):
    	blockArrJSON = []
    	for block in self.chain:
    		blockJSON = {}
    		blockJSON['hash'] = block.hash 
    		blockJSON['index'] = block.index
    		blockJSON['prev'] = block.prev
    		blockJSON['time'] = block.time
    		# blockJSON['nonse'] = block.nonse
    		# blockJSON['gym'] = block.gym

    		transactionsJSON = [];
    		tJSON = {};
    		for transaction in block.transactions:
    			tJSON['time'] = transaction.time
    			tJSON['sender'] = transaction.sender
    			tJSON['reciever'] = transaction.reciever
    			tJSON['amt'] = transaction.amt
    			tJSON['hash'] = transaction.hash 
    			transactionsJSON.append(tJSON)
    		blockJSON['transactions'] = transactionsJSON
    		blockArrJSON.append(blockJSON)

    	return blockArrJSON
class Block(object):
	"""
	Block Contains Information about itself for example it's hash 
	the hash of the previous block , index and time at which block 
	was created. 
	It also contains all the Transaction that has been done

	"""
	def __init__(self, Transactions, time , index):
		self.index = index; # Block Number
		self.transactions = Transactions # Transaction data
		self.time = time
		self.prev = '' #Hash of the Previous block 
		self.hash = self.calculateHash() # Hash of Block 


	def calculateHash(self):
		"""
		The hash is calculated from the transcations
		made on that block , the hash of the previous block 
		time at which block is cretaed and the index of the block 
		"""
		hashTransactions = ''
		for transaction in self.transactions:
			hashTransactions  += transaction.hash 
		hashString  = str(self.time)+ hashTransactions + self.prev + str(self.index)
		hashEncoded = json.dumps(hashString, sort_keys=True).encode()
		return hashlib.sha256(hashEncoded).hexdigest() #SHA256 Hash Encoding - Same as Bitcoin



class Transaction(object):
    """
    Transaction is the transfer of value  from sender to 
    reciever
    """
    def __init__(self,sender, reciever, amt):
        self.sender = sender
        self.reciever = reciever
        self.amt  = amt 
        self.time = time()
        self.hash = self.calculateHash()

    def calculateHash(self):
    	"""
    	THe hash is calculated based on the sender , reciever
    	and the time for which transaction is made
    	"""
    	hashString = self.sender + self.reciever + str(self.amt) + str(self.time);
    	hashEncoded = json.dumps(hashString, sort_keys=True).encode()
    	return hashEncoded.sha256(hashEncoded).hexdigest()



   



