''' Converts a json object into a string to enable 0mq to filter
messages by the author and their source code.
FORMAT:
~~~~~~~~
data = {'author':'127.0.0.1',
        'source': 'hallo',
        'variations': {
            '0x18239uyehriofeb':{
                'bytecode_runtime':'0x18239sdasdsadadsdad',
                'abi':'this is abi',
                'voters':['miner1']
                  } ,
            '0x98py413uh2reogiu43e':{
                'bytecode_runtime':'0x98pyasdasdsaorqgihejb',
                'abi':'this is another abi',
                'voters':['miner3','miner4'], 
                  } ,
            }
        }
'''

def encode(data,
           delimiter = '///',
           delimiter2 = '***'):
    string = ''.join( [ 
        data['author'], ' ', delimiter,
        data['source'], delimiter, 
        str(len( data['variations'] )),
        ] ) 
            
    for bytecode in data['variations'].keys():
        mini_string = ''.join( [ 
            delimiter,bytecode,delimiter,
            data['variations'][bytecode]['bytecode_runtime'], delimiter, 
            data['variations'][bytecode]['abi'], delimiter,
            ] )
        
        for j in range(len( data['variations'][bytecode]['voters'] )):
            mini_string += data['variations'][bytecode]['voters'][j]
            mini_string += delimiter2
                 
        string += mini_string
    return string


def decode(data,
           delimiter = '///',
           delimiter2 = '***' ):
    data = data.split( delimiter )
    json_file = { 'author': data[0].strip(),
                  'source': data[1],
                  }
    assert int( data[2] )
    variations = {}
    for i in range(int( data[2] )):
        bytecode = data[ 3 + 4*i ]
        variant = { 'bytecode_runtime': data[ 4 + 4*i ],
                    'abi': data[ 5 + 4*i ],
                    'voters': data[ 6 +4*i ].split( delimiter2 )[:-1]
                    }
        variations[bytecode] = variant
    json_file['variations'] = variations
    return json_file
