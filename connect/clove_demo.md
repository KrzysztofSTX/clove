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
  
  # Contract Mining 
  Meanwhile, the miners would see (in the background, nevertheless) the start of the following process pipeline:
  
  # INSERT M2
  
  There are a few ports for connecting contract publishers like Alice to the miners. Afterwards, miners use other specialized ports to connect amongst themselves and combine their efforts into compiling the contract and sharing their results. For illustartion, here is what it would look like when the functions are called directly from the command line:
  ~~~~~~~~~
  from clove.connect import zmq_tools
  messages = source_listener()
  print( messages )
  >>> 127.0.0.1///pragma solidity ^{{solidity_version}};

  contract {{contract_name}} {...
  ~~~~~~~~~
  
