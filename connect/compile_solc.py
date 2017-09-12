from solc import compile_source, compile_files, link_code

''' Functions
1. compile_from_file( file_path ) - file_path is string or list of strings
2. compile_from_source(source) - source is string or list of strings

Shortcuts
3. cff() - compile from file
4. cfs() - compile from source
'''

def compile_from_file(file_path):
    multiple = False
    if type(file_path) == str:
        compiled = compile_files([ file_path ])
    elif type(file_path)==list:
        compiled = compile_files( file_path )
        multiple = True
        
    elif type(file_path) not in (str, list):
        print( 'Incorrect input: needs to be file path or list of file paths' )
        
    if multiple:
        files = len( file_path )
    files = 1
    print( 'Compiled %d files' % files )
    
    compiled = compiled['Example']['bin']
    compiled += '0x'
    return compiled


def compile_from_source(source):
    # Source has to be Solidity-formatted script
    if type(source)==str:
        compiled = compile_source(source)
        compiled = [ '0x' + compiled['Example']['bin'] ]
    elif type(source)==list:
        files = []
        for s in source:
            files.append( '0x' + compile_source(s)['Example']['bin'] )
    print( 'Compiled %d sources' % len( compiled ) )
    return compiled


def cff(a)
    return compile_from_file(a)


def cfs(a)
    return compile_from_source(a)





