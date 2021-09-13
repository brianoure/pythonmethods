"""
pattern_stringHEAD_stringTAIL_list( "brianxxxcvbpythonvvvvvvvvvgghhbrianpppfgpython","brian","python") returns ["xxxcvb","pppfg"]
pattern_stringHEAD_stringTAIL_list( "susanvenezuelastronggghhsusancanadastrong","susan","strong") returns ["venezuela","canada"]
pattern_stringHEAD_stringTAIL_list( "boatxvmotorvvvmotorvgghmotor","boat","motor") returns ["xv"]
"""
def pattern_stringHEAD_stringTAIL_list(test_string,head_string,tail_string):
    ptr_start_list=[]
    ptr_end_list=[]
    frame_string_list=[]
    for j in range(len( test_string )):
          if((test_string[j:j+len(head_string)]) == head_string):   ptr_start_list = ptr_start_list + [j]
          if((test_string[j:j+len(tail_string)]) == tail_string):   ptr_end_list = ptr_end_list + [j]
    number_of_frames = len( ptr_start_list )
    if(len(ptr_end_list)<len(ptr_start_list)):  number_of_frames = len( ptr_end_list )
    for x in range(number_of_frames_string):
          frame_string_list = frame_string_list + test_string[ (ptr_start_list[ x+len(head_string)]) : ptr_end_list[x]   ]
    return frame_string_list
                                      
