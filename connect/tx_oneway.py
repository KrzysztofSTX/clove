# One-way transaction to be used by the two-way transaction class
    

# txid can be a 3-ple of 2 IDs for each chain and 1 for Clove
# one-way transaction to be used inside one chain
class oneway_tx:
    def __init__(self, txid, send_addr, recv_addr,
                 compiled_contract_code,
                 value = None,  
                 gas = None, gasPrice = None, nonce = None):
        self.txid = txid
        self.send_addr = send_addr
        seld.recv_addr = recv.addr
        self.compiled = compiled_contract_code
        self.value = value
        self.gas = gas
        self.gasPrice = gasPrice
        self.nonce = nonce

    def info(self):
        print('Transaction ID:',self.txid,
              'Sender Address:',self.send_addr,
              'Receiver Address:',self.recv_addr,
              'Value Sent:',self.value,
              'Gas Amount:',self.gas,
              'Gas Price:',self.gasPrice,
              'Nonce:',self.nonce)

    # Create proper dictionary taken by deploy function 
    def parameters(self):
        output = { 'from':self.send_addr,
                   'to':self.recv_addr,
                   'data':self.compiled}        
        opt_names = ['value','gas','gasPrice','nonce']
        optionals = [self.value, self.gas, self.gasPrice, self.nonce]
        
        for i in range(len(optionals)):
            if optionals[i] != None:
                output[ opt_names[i] ] = optionals[i]
        return output

    

                
                
        
        
