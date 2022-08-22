#MSB is left, LSB is right
def list_to_num( mylist, base):
    rslt = 0
    positions = len(mylist)
    for j in range(  positions  ):
        if(mylist[j]>=base):
          print("ALERT! list_to_num function: value in the list exceeds the base!!! ")
        mypower = positions - 1 - j
        rslt    = rslt + ( (mylist[j])*((base)**(mypower)) )
    return rslt

#starting from the carrier, plot out the frequency shifts and corresponding magnitude for each pixel
def black_white_mag_frequency_list( height,width,row_col_luma_list,luma_carrier,frequency_step_size ):
    #row is [0],col is [1], luma is [2] in the row_col_list
    mag_freq_list = []
    for x in range( len(row_col_luma_list) ):
        new_frequency = luma_carrier + 
                                   ( 
                                      list_to_num( [row_col_luma_list[x][0],row_col_luma_list[x][1]], width )
                                                   *
                                      frequency_step_size
                                   )
        new_mag       = row_col_luma_list[x][2]
        mag_freq_list = mag_freq_list + [ [new_mag,new_frequency] ]
    return mag_freq_list
