import pandas as pd

def data_load_parsing(): 
    """
    This function is for loading each of the files in TerrorAttack and TerroristRel
    and parsing them into tables of panda dataframe format that we can use.
    
    input: none
    output:
        terrorist_rel_labels: terrorist relationship types (colleague, family, ...)
        terrorist_rel_edges: terrorists that have some kind of relationship are linked
        terrorist_rel_coll: terrorists who are 'colleagues' are linked
        terrorist_rel_cong: terrorists who are 'congregates' are linked
        terrorist_rel_cont: terrorists who are 'contacts' are linked
        terrorist_rel_fam: terrorists who are 'families' are linked.
        
        *the columns of each dataframe are type integer and begins with 0, ...
    """
    
    # file paths
    file_path1 = '../data/TerroristRel/TerroristRel.edges'
    file_path2 = '../data/TerroristRel/TerroristRel.labels'
    file_path3 = '../data/TerroristRel/TerroristRel_Colleague.nodes'
    file_path4 = '../data/TerroristRel/TerroristRel_Congregate.nodes'
    file_path5 = '../data/TerroristRel/TerroristRel_Contact.nodes'
    file_path6 = '../data/TerroristRel/TerroristRel_Family.nodes'

    '''Load and parse TerroristRel.edges'''
    terrorist_rel_edges = pd.read_csv(file_path1, sep='\t', header=None)
    
    '''Load and parse TerroristRel.labels'''
    terrorist_rel_labels = pd.read_csv(file_path2, header=None)
    
    '''Load and parse TerroristRel_Colleage.nodes'''
    # Parse using tab and space delimiters
    terrorist_rel_coll = pd.read_csv(file_path3, sep='\t|' '', header=None)
    
    '''Load and parse TerroristRel_Congregate.nodes'''
    # Parse using tab and space delimiters
    terrorist_rel_cong = pd.read_csv(file_path4, sep='\t|' '', header=None)
    
    '''Load and parse TerroristRel_Contact.nodes'''
    # Parse using tab and space delimiters
    terrorist_rel_cont = pd.read_csv(file_path5, sep='\t|' '', header=None)
    
    '''Load and parse TerroristRel_Family.nodes'''
    # Parse using tab and space delimiters
    terrorist_rel_fam = pd.read_csv(file_path6, sep='\t|' '', header=None)
    
    return terrorist_rel_labels, terrorist_rel_edges, terrorist_rel_coll, \
terrorist_rel_cong, terrorist_rel_cont, terrorist_rel_fam