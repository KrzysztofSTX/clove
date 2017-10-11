from web3 import Web3, TCPProvider


def create_web3( ip_addr,
                 password):
    ''' Creates a Web3 object. Set this function to a variable to call Web3
    methods, and use the variable inside other high level functions.
    '''
    a = Web3(TCPProvider( ip_addr ))
    a.personal.newAccount( password )
    return a
                     

def contract_deployer(web3obj,
                      contract_data,
                      password,
                      address = None,
                      duration = 0,
                      name = 'Contract'):
    ''' Deploys a contract. This contract can be reused, so you can set this
    function to a variable to transact the contract again.
    Arguments:
    ~~~~~~~~~~
    web3obj - the web3 object of the node
    contract_data - the abi, bytecode, and runtime bytecode of the contract in json
        format.
    password - account password to unlock it for deployment
    duration - time for which to keep the account unlocked. Default will open account
        for five seconds.
    name - the name of the contract to call it in the future.
    '''
    from Web3 import contract
    
    a_contract = contract.Contract.factory( web3 = web3obj,
            contract_name = name,
            abi= contract_data["abi"],
            bytecode = contract_data["code"],
            bytecode_runtime = contract_data["code_runtime"] )
    print( 'Contract named %s created.' % name )

    if not address:
        accounts = web3obj.personal.listAccounts
        if len( accounts ) >= 1:
            print( 'More than one account present. Please specify address' )
        else:
            address = web3obj.personal.listAccounts[0]

    transaction = { 'from' : address }
        
    if not duration:
        duration = 5
        web3obj.personal.unlockAccount( web3obj, password, duration )
    else:
        web3obj.personal.unlockAccount( web3obj, password, duration )
    tx_hash = a_contract.deploy

    deploy = a_contract.deploy(transaction = transaction)
   
    if deploy:
        print( 'Contract deployed successfully!\nTransaction Hash: %s' % deploy )
    else:
        print( 'Contract not deployed, please check parameters or source code.' )
