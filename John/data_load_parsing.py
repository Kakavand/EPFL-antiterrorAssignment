def data_load_parsing(): 
    """
    This function is for loading each of the files in TerrorAttack and TerroristRel
    and parsing them into tables of panda dataframe format that we can use.
    
    input: none
    output:
        terr_attack_labels: terrorist attack types (bombing, weapon attack, ...)
        terr_attack_nodes: nodes that represent the terrorist attacks themselves
        terr_attack_edges_v1: edges that connect terrorist attacks (nodes) with co-locations
        terr_attack_edges_v2: edges that connect terrorist attacks (nodes) with co-locations performed by the same organization
        
        terrorist_rel_labels: terrorist relationship types (colleague, family, ...)
        terrorist_rel_edges: terrorists that have some kind of relationship are linked
        terrorist_rel_coll: terrorists who are 'colleagues' are linked
        terrorist_rel_cong: terrorists who are 'congregates' are linked
        terrorist_rel_cont: terrorists who are 'contacts' are linked
        terrorist_rel_fam: terrorists who are 'families' are linked.
    """
    
    import pandas as pd
    
    # Modify your file paths and run the code below
    file_path1 = '../data/TerrorAttack/terrorist_attack.labels'
    file_path2 = '../data/TerrorAttack/terrorist_attack.nodes'
    file_path3 = '../data/TerrorAttack/terrorist_attack_loc.edges'
    file_path4 = '../data/TerrorAttack/terrorist_attack_loc_org.edges'
    
    file_path5 = '../data/TerroristRel/TerroristRel.edges'
    file_path6 = '../data/TerroristRel/TerroristRel.labels'
    file_path7 = '../data/TerroristRel/TerroristRel_Colleague.nodes'
    file_path8 = '../data/TerroristRel/TerroristRel_Congregate.nodes'
    file_path9 = '../data/TerroristRel/TerroristRel_Contact.nodes'
    file_path10 = '../data/TerroristRel/TerroristRel_Family.nodes'
    
    #-----------------------------------------------------#
    '''Load and parse attack labels data'''
    terr_attack_labels = pd.read_csv(file_path1, sep='#', header=None)[1]
    #-----------------------------------------------------#
    
    #-----------------------------------------------------#
    '''Load 'terrorist_attack.nodes' using tab delimiter'''
    data = pd.read_csv(file_path2, sep='\t', header=None)
    
    # Parse the first and last columns using '#' and delimiter
    attacks = data[0].str.split('#',expand=True)[1]
    attack_labels = data[107].str.split('#',expand=True)[1]
                        
    # Set the index of the first 0-1 attribute to 0 (instead of 1)
    data.columns.values[1:107] = data.columns.values[1:107] - 1
    data.columns.values[0] = -1
    # Change the column data type from int to str
    data.columns = data.columns.astype(str)
    
    # Join the attacks and attack labels to the features.
    terr_attack_nodes = pd.concat([attacks, attack_labels, data.loc[:,'0':'105']], axis=1)
    
    # Rename the first and second columns
    terr_attack_nodes.columns.values[0] = 'Terrorist Attack'
    terr_attack_nodes.columns.values[1] = 'Attack Label'
    #-----------------------------------------------------#
    
    #-----------------------------------------------------#
    '''Load and parse 'terrorist_attack_loc.edges'''
    data = pd.read_csv(file_path3, sep='#', header=None)
    terr_attack_edges_v1 = pd.concat([data[1].str.split(' ',expand=True)[0], data[2]], axis=1)
    
    # Rename the second column. Column type is int.
    terr_attack_edges_v1.columns.values[1] = 1
    #-----------------------------------------------------#
    
    #-----------------------------------------------------#
    '''Load and parse 'terrorist_attack_loc_org.edges'''
    data = pd.read_csv(file_path4, sep='#', header=None)
    terr_attack_edges_v2 = pd.concat([data[1].str.split(' ',expand=True)[0], data[2]], axis=1)
    
    # Rename the second column. Column type is int.
    terr_attack_edges_v2.columns.values[1] = 1
    #-----------------------------------------------------#
    
    #-----------------------------------------------------#
    '''Load and parse TerroristRel.edges'''
    data = pd.read_csv(file_path5, sep='#', header=None)
    terrorist_rel_edges = pd.concat([data[1].str.split('_',expand=True)[0], 
                                     data[2].str.split(' ',expand=True)[0]], axis=1)
    
    
    # Rename the second column. Column type is int.
    terrorist_rel_edges.columns.values[1] = 1
    
    # Parse the second time but only the second column using tab delimiter
    terrorist_rel_edges = pd.concat([terrorist_rel_edges[0], 
                                     terrorist_rel_edges[1].str.split('\t',expand=True)[0]], axis=1)
    
    # Rename the second column again. Column type is int.
    terrorist_rel_edges.columns.values[1] = 1
    #-----------------------------------------------------#
    
    #-----------------------------------------------------#
    '''Load and parse TerroristRel.labels'''
    terrorist_rel_labels = pd.read_csv(file_path6, header=None)
    #-----------------------------------------------------#
    
    #-----------------------------------------------------#
    '''Load and parse TerroristRel_Colleages.nodes'''
    # Parse using tab and space delimiters
    data = pd.read_csv(file_path7, sep='\t|' '', header=None)
    
    # Parse first column with '#' delimiter
    temp = data[0].str.split('#',expand=True)
               
    # Extract terrorist names from temp and concatenate with the 0-1 features
    terrorist_rel_coll = pd.concat([temp[1].str.split('_',expand=True)[0], 
                                    temp[2], data.loc[:,1225], data.loc[:,1:1224]], axis=1)
    
    # Temporariliy assign the first three columns' names to something else
    terrorist_rel_coll.columns.values[0] = -1
    terrorist_rel_coll.columns.values[1] = -2
    terrorist_rel_coll.columns.values[2] = -3
    
    # Subtract 1 so the index of features begin with 0
    terrorist_rel_coll.columns.values[3:1227] = terrorist_rel_coll.columns.values[3:1227] - 1
    
    # Change the column data type from int to str
    terrorist_rel_coll.columns = terrorist_rel_coll.columns.astype(str)
    terrorist_rel_coll.columns.values[0] = 'Terrorist1'
    terrorist_rel_coll.columns.values[1] = 'Terrorist2'
    terrorist_rel_coll.columns.values[2] = 'Relationship'
    #-----------------------------------------------------#
    
    #-----------------------------------------------------#
    '''Load and parse TerroristRel_Congregate.nodes'''
    # Parse using tab and space delimiters
    data = pd.read_csv(file_path8, sep='\t|' '', header=None)
    
    # Parse first column with '#' delimiter
    temp = data[0].str.split('#',expand=True)
               
    # Extract terrorist names from temp and concatenate with the 0-1 features
    terrorist_rel_cong = pd.concat([temp[1].str.split('_',expand=True)[0], 
                                    temp[2], data.loc[:,1225], data.loc[:,1:1224]], axis=1)
    
    # Temporariliy assign the first three columns' names to something else
    terrorist_rel_cong.columns.values[0] = -1
    terrorist_rel_cong.columns.values[1] = -2
    terrorist_rel_cong.columns.values[2] = -3
    
    # Subtract 1 so the index of features begin with 0
    terrorist_rel_cong.columns.values[3:1227] = terrorist_rel_cong.columns.values[3:1227] - 1
    
    # Change the column data type from int to str
    terrorist_rel_cong.columns = terrorist_rel_cong.columns.astype(str)
    terrorist_rel_cong.columns.values[0] = 'Terrorist1'
    terrorist_rel_cong.columns.values[1] = 'Terrorist2'
    terrorist_rel_cong.columns.values[2] = 'Relationship'
    #-----------------------------------------------------#
    
    #-----------------------------------------------------#
    '''Load and parse TerroristRel_Contact.nodes'''
    # Parse using tab and space delimiters
    data = pd.read_csv(file_path9, sep='\t|' '', header=None)
    
    # Parse first column with '#' delimiter
    temp = data[0].str.split('#',expand=True)
               
    # Extract terrorist names from temp and concatenate with the 0-1 features
    terrorist_rel_cont = pd.concat([temp[1].str.split('_',expand=True)[0], 
                                    temp[2], data.loc[:,1225], data.loc[:,1:1224]], axis=1)
    
    # Temporariliy assign the first three columns' names to something else
    terrorist_rel_cont.columns.values[0] = -1
    terrorist_rel_cont.columns.values[1] = -2
    terrorist_rel_cont.columns.values[2] = -3
    
    # Subtract 1 so the index of features begin with 0
    terrorist_rel_cont.columns.values[3:1227] = terrorist_rel_cont.columns.values[3:1227] - 1
    
    # Change the column data type from int to str
    terrorist_rel_cont.columns = terrorist_rel_cont.columns.astype(str)
    terrorist_rel_cont.columns.values[0] = 'Terrorist1'
    terrorist_rel_cont.columns.values[1] = 'Terrorist2'
    terrorist_rel_cont.columns.values[2] = 'Relationship'
    #-----------------------------------------------------#
    
    #-----------------------------------------------------#
    '''Load and parse TerroristRel_Family.nodes'''
    # Parse using tab and space delimiters
    data = pd.read_csv(file_path10, sep='\t|' '', header=None)
    
    # Parse first column with '#' delimiter
    temp = data[0].str.split('#',expand=True)
               
    # Extract terrorist names from temp and concatenate with the 0-1 features
    terrorist_rel_fam = pd.concat([temp[1].str.split('_',expand=True)[0], 
                                    temp[2], data.loc[:,1225], data.loc[:,1:1224]], axis=1)
    
    # Temporariliy assign the first three columns' names to something else
    terrorist_rel_fam.columns.values[0] = -1
    terrorist_rel_fam.columns.values[1] = -2
    terrorist_rel_fam.columns.values[2] = -3
    
    # Subtract 1 so the index of features begin with 0
    terrorist_rel_fam.columns.values[3:1227] = terrorist_rel_fam.columns.values[3:1227] - 1
    
    # Change the column data type from int to str
    terrorist_rel_fam.columns = terrorist_rel_fam.columns.astype(str)
    terrorist_rel_fam.columns.values[0] = 'Terrorist1'
    terrorist_rel_fam.columns.values[1] = 'Terrorist2'
    terrorist_rel_fam.columns.values[2] = 'Relationship'
    
    return terr_attack_labels, terr_attack_nodes, terr_attack_edges_v1, \
terr_attack_edges_v2, terrorist_rel_labels, terrorist_rel_edges, \
terrorist_rel_coll, terrorist_rel_cong, terrorist_rel_cont, terrorist_rel_fam