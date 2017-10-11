def encode(data,
           delimiter = '///',
           delimiter2 = '***'):
    ''' Converts a json object into a string to enable 0mq to filter
    messages by the author and their source code.
    
    FORMAT:
    ~~~~~~~
    data = {'author':'Bob',
            'source':'Ayyy',
            'variations':
                [
                    { 'bytecode':'0x18239uyehriofeb',
                       'abi':'this is abi', # convert abi to string
                       # to avoid differences in Solc for python / javascript
                       'voters':['miner1']
                      } ,
                    { 'bytecode':'0x98py413uh2reogiu43e',
                       'abi':'this is another abi',
                       'voters':['miner3','miner4'], # exluded # voters, use len()
                      } ,
                ]
            }
    '''

    string = ''.join( [ 
        data['author'], ' ', delimiter,
        data['source'], delimiter, 
        str(len( data['variations'] )),
        ] ) 
            
    for i in range(len( data['variations'] )):
        mini_string = ''.join( [ 
            delimiter,
            data['variations'][i]['bytecode'], delimiter, 
            data['variations'][i]['abi'], delimiter,
            ] )
        
        for j in range(len( data['variations'][i]['voters'] )):
            mini_string += data['variations'][i]['voters'][j]
            mini_string += delimiter2
                 
        string += mini_string
    return string

            

def decode(data,
           delimiter = '///',
           delimiter2 = '***' ):
    ''' Decodes the string supplied by the 'encode' function back into json
    format. 
    '''
    data = data.split( delimiter )
    json_file = { 'author': data[0],
                  'source': data[1],
                  }
    assert int( data[2] )
    variations = []
    for i in range(int( data[2] )):
        variant = { 'bytecode': data[ 3 + 3*i ],
                    'abi': data[ 4 + 3*i ],
                    'voters': data[ 5 +3*i ].split( delimiter2 )[:-1]
                    }
        variations.append(variant)
    json_file['variations'] = variations
    return json_file
        
data = {'author':'Bob',
        'source':'Ayyy',
        'variations':
            [
                { 'bytecode':'0x18239uyehriofeb',
                   'abi':'this is abi', # convert abi to string
                   # to avoid differences in Solc for python / javascript
                   'voters':['miner1']
                  },
                { 'bytecode':'0x98py413uh2reogiu43e',
                   'abi':'this is another abi',
                   'voters':['miner3','miner4']
                  },
            ]
        }
