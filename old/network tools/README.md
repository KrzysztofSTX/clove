# ABI To String And Back

Converts a contract ABI in all its complexity into a string (which can additionally be encrypted) in order to be sent over ZMQ as a message. Also includes the tool to turn the string back into the original ABI. 

###### For this example we shall use the Ballot contract from the Remix home page.

~~~~~
ABI UNFORMATTED:

 [{'inputs': [{'type': 'address', 'name': 'to'}], 'name': 'delegate', 'payable': False, 'type': 'function', 'constant': False, 'stateMutability': 'nonpayable', 'outputs': []}, {'inputs': [], 'name': 'winningProposal', 'payable': False, 'type': 'function', 'constant': True, 'stateMutability': 'view', 'outputs': [{'type': 'uint8', 'name': '_winningProposal'}]}, {'inputs': [{'type': 'address', 'name': 'toVoter'}], 'name': 'giveRightToVote', 'payable': False, 'type': 'function', 'constant': False, 'stateMutability': 'nonpayable', 'outputs': []}, {'inputs': [{'type': 'uint8', 'name': 'toProposal'}], 'name': 'vote', 'payable': False, 'type': 'function', 'constant': False, 'stateMutability': 'nonpayable', 'outputs': []}, {'inputs': [{'type': 'uint8', 'name': '_numProposals'}], 'type': 'constructor', 'stateMutability': 'nonpayable', 'payable': False}] 

ENCODED ABI: <class 'str'> 

 startlist
    listelement
        startdict
            inputs
                startlist
                    listelement
                        startdict
                            type
                                address
                            name
                                to
                        enddict
                endlist
            name
                delegate
            payable
                False
            type
                function
            constant
                False
            stateMutability
                nonpayable
            outputs
                startlist
                endlist
        enddict
    listelement
        startdict
            inputs
                startlist
                endlist
            name
                winningProposal
            payable
                False
            type
                function
            constant
                True
            stateMutability
                view
            outputs
                startlist
                    listelement
                        startdict
                            type
                                uint8
                            name
                                _winningProposal
                        enddict
                endlist
        enddict
    listelement
        startdict
            inputs
                startlist
                    listelement
                        startdict
                            type
                                address
                            name
                                toVoter
                        enddict
                endlist
            name
                giveRightToVote
            payable
                False
            type
                function
            constant
                False
            stateMutability
                nonpayable
            outputs
                startlist
                endlist
        enddict
    listelement
        startdict
            inputs
                startlist
                    listelement
                        startdict
                            type
                                uint8
                            name
                                toProposal
                        enddict
                endlist
            name
                vote
            payable
                False
            type
                function
            constant
                False
            stateMutability
                nonpayable
            outputs
                startlist
                endlist
        enddict
    listelement
        startdict
            inputs
                startlist
                    listelement
                        startdict
                            type
                                uint8
                            name
                                _numProposals
                        enddict
                endlist
            type
                constructor
            stateMutability
                nonpayable
            payable
                False
        enddict
endlist

DECODED ABI: <class 'list'> 

 [{'inputs': [{'type': 'address', 'name': 'to'}], 'name': 'delegate', 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function', 'outputs': [], 'constant': False}, {'inputs': [], 'name': 'winningProposal', 'payable': False, 'stateMutability': 'view', 'type': 'function', 'outputs': [{'type': 'uint8', 'name': '_winningProposal'}], 'constant': True}, {'inputs': [{'type': 'address', 'name': 'toVoter'}], 'name': 'giveRightToVote', 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function', 'outputs': [], 'constant': False}, {'inputs': [{'type': 'uint8', 'name': 'toProposal'}], 'name': 'vote', 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function', 'outputs': [], 'constant': False}, {'inputs': [{'type': 'uint8', 'name': '_numProposals'}], 'stateMutability': 'nonpayable', 'type': 'constructor', 'payable': False}] 

ORIGINAL ABI: <class 'list'> 

 [{'inputs': [{'type': 'address', 'name': 'to'}], 'name': 'delegate', 'payable': False, 'type': 'function', 'constant': False, 'stateMutability': 'nonpayable', 'outputs': []}, {'inputs': [], 'name': 'winningProposal', 'payable': False, 'type': 'function', 'constant': True, 'stateMutability': 'view', 'outputs': [{'type': 'uint8', 'name': '_winningProposal'}]}, {'inputs': [{'type': 'address', 'name': 'toVoter'}], 'name': 'giveRightToVote', 'payable': False, 'type': 'function', 'constant': False, 'stateMutability': 'nonpayable', 'outputs': []}, {'inputs': [{'type': 'uint8', 'name': 'toProposal'}], 'name': 'vote', 'payable': False, 'type': 'function', 'constant': False, 'stateMutability': 'nonpayable', 'outputs': []}, {'inputs': [{'type': 'uint8', 'name': '_numProposals'}], 'type': 'constructor', 'stateMutability': 'nonpayable', 'payable': False}] 

VARIABLE CHECK: decoded == ab
 True
 ~~~~~
