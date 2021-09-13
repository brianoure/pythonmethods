"""
pattern_stringHEAD_stringTAIL_list( "brianxxxcvbpythonvvvvvvvvvgghhbrianpppfgpython","brian","python") returns ["xxxcvb","pppfg"]
pattern_stringHEAD_stringTAIL_list( "susanvenezuelastronggghhsusancanadastrong","susan","strong") returns ["venezuela","canada"]
pattern_stringHEAD_stringTAIL_list( "boatxvmotorvvvmotorvgghmotor","boat","motor") returns ["xv"]
"""
def pattern_stringHEAD_stringTAIL_list(test_string,head_string,tail_string):
    ptr_start_list=[] #pointer to a valid head
    ptr_end_list=[]   #pointer to a valid tail
    frame_string_list=[] #list containing strings found between header and tail
    for j in range(len( test_string )): #look throughout the test_string for a head and a tail noting their locations/pointers
          if((test_string[j:j+len(head_string)]) == head_string):   ptr_start_list = ptr_start_list + [j]
          if((test_string[j:j+len(tail_string)]) == tail_string):   ptr_end_list = ptr_end_list + [j]
    number_of_frames = len( ptr_start_list ) #it is expected that valid strings require an equal amount of head and tail strings
    if(len(ptr_end_list)<len(ptr_start_list)):  number_of_frames = len( ptr_end_list ) #choose least value of pointers to determine number of valid strings available
    for x in range(number_of_frames_string):
          frame_string_list = frame_string_list + test_string[ (ptr_start_list[ x+len(head_string)]) : ptr_end_list[x]   ] #store the valid strings in a list
    return frame_string_list
                                      
