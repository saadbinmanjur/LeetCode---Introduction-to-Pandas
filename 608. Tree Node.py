import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    
    tree = tree.where(pd.notnull(tree), -1)
    ids, p_ids, nodes = tree['id'].to_list(),tree['p_id'].to_list(), []

    for i in range(len(ids)):
        if p_ids[i] == -1   : nodes.append("Root")
        elif ids[i] in p_ids: nodes.append("Inner")
        else                : nodes.append("Leaf")
    
    return pd.DataFrame({'id':ids, 'type':nodes})