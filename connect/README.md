  # Decentralized Contract Ecosystem
  
  ## Cross-Blockchain Swap
  ~~~~~~~~~  
  Alice and Bob initiate contract details and parameters
      |                                        |
      |                                        |
  Alice writes their contract               Bob writes their contract    
      |                                        |
      \                                        /
       \---Miner Network compiles contract----/
        \          {and verifies}            /      
       /-U----------------------------------/        
      |    \
  Alice     \---------------Bob gets Alice's contract code
  gets                               |        
  Bob's contract code                |
        |                            |
        \                            /
         \----------\  /------------/   
                     \/
          Contracts Execute simultaneously
          using one of several methods
          depending on Alice and Bob's 
          initial agreement.
  ~~~~~~~~~          
      
    
  # Contract Initialization
  
  Alice wants to initiate a new contract. She has figured out her parameters, for example:
  
  ~~~~~~~~~
  from flora import example_contract, example.json 
  contract_1 = example_contract
  params_1 = example.json
  print( params_1 )
  ~~~~~~~~~
  Which yields the contract parameters: 
  ~~~~~~~~~
  {
    "solidity_version":"0.4.8",
    "contract_name":"Testcoin",
    "symbol":"TST",
    "asset_name":"Testcoin",
    "total_supply":"1000000"
  }
  ~~~~~~~~~
  Now she combines the contract parameters with the appropriate contract template:
  ~~~~~~~~~
  import tsol
  source = tsol.compile( contract_1, params_1 )
  ~~~~~~~~~
  With her complete source, Alice now wants to deploy it to miners for it get compiled into bytecode and ABI:
  ~~~~~~~~~
  from clove.connect import zmq_tools
  source_publisher( source )
  ~~~~~~~~~
  With miners online, Alice would see: 
  
  ![alt text](https://github.com/Lamden/clove/blob/master/connect/zmq_tools/change_server.png) 
  
  Where 'Hello World' can be replaced with any source code. Alice successfully published her address and source, and most importantly she can go offline and the miners would continue receiving sources such as another Bob's 'Goodbye World!' broadcast.
  

  There are a few ports for connecting contract publishers like Alice to the miners. Afterwards, miners use other specialized ports to connect amongst themselves and combine their efforts into compiling the contract and sharing their results. For illustartion, here is what it would look like when the functions are called directly from the command line:
  ~~~~~~~~~
  from clove.connect import zmq_tools
  messages = source_listener()
  print( messages )
  >>> 127.0.0.1///pragma solidity ^{{solidity_version}};

  contract {{contract_name}} {...
  ~~~~~~~~~
  
  # Compilation With TSOL
  
  You can easily compile a templated verified contract using tsol. Create a variable of a streaming file that can take the .read() method, on a local machine this can be accomplished by putting the template in the /temp folder. For Mac this is /private/tmp/. Then using a json objects to store the contract parameters, call tsol.compile:
  
  ~~~~~~~~~
  import tsol
  
  fexample = {
    "solidity_version":"0.4.8",
    "contract_name":"Testcoin",
    "symbol":"TST",
    "asset_name":"Testcoin",
    "total_supply":"1000000"
  }

  template = '/private/tmp/template.tsol'
  template = open(ftemplate)
  contract = tsol.compile(template, example)
  ~~~~~~~~~
  
  # Compilation With SOLC
  
  If you already have the contract source, you can likewise use py-solc by itself:
  ~~~~~~~~~
  from solc import compile_source
  
  contract = compile_source( source )
  ~~~~~~~~~
  
  # Verifying Contracts
  
  The contract bytecode, runtime bytecode, and abi are needed to deploy the contract. Depending on the compilation method used, the nested dictionary structure of the compiled contract will vary, so you can check it by running a quick nested function:
  ~~~~~~~~~  
  def display(dic,i=0):
    if type(dic)==dict:
        for key in dic.keys():
            print(i*' '+key)
            display(dic[key],i=i+4)
  ~~~~~~~~~
  Which for the TSOL compilation method would yield this structure:
  ~~~~~~~~~
  sources
    Testcoin
        ast
            id
            absolutePath
            nodes
            src
            exportedSymbols
                Testcoin
            nodeType
        id
        legacyAST
            src
            attributes
                exportedSymbols
                    Testcoin
                absolutePath
            id
            children
            name
errors
contracts
    Testcoin
        Testcoin
            devdoc
                methods
            metadata
            evm
                legacyAssembly
                    .code
                    .data
                        0
                            .code
                            .auxdata
                bytecode
                    opcodes
                    object
                    sourceMap
                    linkReferences
                gasEstimates
                    external
                        name()
                        symbol()
                        decimals()
                        balanceOf(address)
                        transferFrom(address,address,uint256)
                        approve(address,uint256)
                        allowance(address,address)
                        owner()
                        totalSupply()
                        transfer(address,uint256)
                    creation
                        totalCost
                        executionCost
                        codeDepositCost
                deployedBytecode
                    opcodes
                    object
                    sourceMap
                    linkReferences
                methodIdentifiers
                    name()
                    symbol()
                    decimals()
                    balanceOf(address)
                    transferFrom(address,address,uint256)
                    approve(address,uint256)
                    allowance(address,address)
                    owner()
                    totalSupply()
                    transfer(address,uint256)
                assembly
            userdoc
                methods
            abi
  ~~~~~~~~~  
  To gather the ingredients we need, we go up by the dictionary roots to obtain the three components. We can put it in a dictionary and pass it as contract_data into the contract deployment function, to immediately deploy it from your node to the connected blockchain. 
  ~~~~~~~~~  
  bytecode_runtime = fex['contracts']['Testcoin']['Testcoin']['evm']['deployedBytecode']['object']
  bytecode = fex['contracts']['Testcoin']['Testcoin']['evm']['bytecode']
  abi = fex['contracts']['Testcoin']['Testcoin']['abi']
  
  contract_data = {
            'abi':abi,
            'code': bytecode,
            'code_runtime': bytecode_runtime,
            }
  ~~~~~~~~~
  Alice can create her own Web3 object to easily use other functions. All she needs is the IP address to connect to her chain and a password for her account. Then she can deploy the contract with one function call:
  ~~~~~~~~~
  ip_addr = 225.0.225.0
  password = 'inwonderland'
  
  alice = create_web3( ip_addr, password, name = 'My_First_Contract' )
  
  contract_deployer( alice, contract_data, password )
  
  # This then prints:
  Contract named My_First_Contract created.
  Contract deployed successfully!
  Transaction Hash: 0x493f75ba81d3820e256b508d0faac21ee3a90f8b1930b80eac6edca8d46835d2
  
  # This hash is the address of the contract, and can be used to call transactions or track it in future blocks.
  ~~~~~~~~~
  
  
  
  
  
  
  
  
  
