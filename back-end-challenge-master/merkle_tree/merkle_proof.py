from utils import *
from merkle_tree import *
from hash_data_structures import *


def merkle_proof(tx, merkle_tree):
    """Given a tx and a Merkle tree object, retrieve its list of tx's and
    parse through it to arrive at the minimum amount of information required
    to arrive at the correct block header. This does not include the tx
    itself.

    Return this data as a list; remember that order matters!
    """
    "*** YOUR CODE HERE ***"

    leaves = merkle_tree.leaves
    tx_pos = merkle_tree.leaves.index(tx)
    tree_size = len(merkle_tree.leaves)

    answer = []

    while (tree_size!=1):
        tree_size //=2
        if tree_size == 1:
            if tx_pos %2 == 0:
                answer.append(leaves[tx_pos+1])
            else:
                answer.append(leaves[tx_pos-1])
        else:
            if tx in leaves[:tree_size]:
                answer.append(concat_and_hash_list(leaves[tree_size:]))
            else:
                answer.append(concat_and_hash_list(leaves[:tree_size]))
    return answer

def verify_proof(tx, merkle_proof):
    """Given a Merkle proof - constructed via `merkle_proof(...)` - verify
    that the correct block header can be retrieved by properly hashing the tx
    along with every other piece of data in the proof in the correct order
    """
    "*** YOUR CODE HERE ***"
    for x in reversed(merkle_proof):
        tx = concat_and_hash_list([tx,x])
    return tx
