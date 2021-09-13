def pattern_stringHEAD_stringTAIL_list(test_string,head_string,tail_string):
  ptr_start_list=[]
  ptr_end_list=[]
  frame_string_list=[]
    for j in range(len(test_string)):
      for k in range(len(head_string)):
        if((test_string[j+k])==head_string[k]):
          ptr_start_list =ptr_start_list + []
      for m in range(len(tail_string)):
        if((test_string[j+m])==tail_string[m]):
          ptr_end_list =ptr_end_list + []
      number_of_frames_string = len( ptr_start_list )
      if(len(ptr_end_list)<len(ptr_start_list)):
        number_of_frames_string = len(len(ptr_end_list)
      for x in range(number_of_frames_string):
        frame_string_list= frame_string_list + test_string[ ptr_start_list[ x+len(head_string)]:ptr_end_list[x] ]
      return frame_string_list
                                      
