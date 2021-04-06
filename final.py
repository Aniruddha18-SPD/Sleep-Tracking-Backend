input_val_hr = ""
input_val_min = ""
total_time_slept = storage_val = 0 
day_count = 1 
total_val = curr_val = curr_val1 = i = status_count1 = status_count2 = 0
storage = dict()

input_error_msg = "Error while entering value" + "\n" + "The number of hours you slept must be between 0 and 24 and the number of minutes must be between 0 and 60"
input_error_msg2 = "Error while entering value" + "\n" + "choose from the two options. Either 'Good' or 'Not Good'"
def input_process():
    day_count = 1 
    i = 0 
    how_feel = ""
    rows, cols = (7, 2)
    print("Enter your sleep time for everyday in a week" + "\n")
    arr = [[0 for i in range(cols)] for j in range(rows)] 
    while i < 7:
        
        input_val_hr = input("Enter the number of hours you slept for day " + str(day_count) + " : ")
        input_val_hr = int(input_val_hr)
        input_val_min = input("Enter the number of minutes you slept : ")
        input_val_min = int(input_val_min)
        if (input_val_hr >= 0 and input_val_hr < 24) and (input_val_min >= 0 and input_val_min < 60):
            
            total_time_slept = ((int(input_val_hr) * 60) + int(input_val_min))
        else:
            print(input_error_msg)
            exit()
        
        print("\n" + "Enter how you felt when you woke you" + "\n" + "Good or Not Good?" + "\n")
        
        how_feel = input("How do you feel today? ")
        how_feel = how_feel.lower()
        
        if how_feel != "good" and how_feel != "not good":
            print(input_error_msg2)
            exit()
        
        arr[i][0] = total_time_slept
        arr[i][1] = how_feel
        
        i = i + 1 
        day_count = day_count + 1 
    
    return arr

def generate_output(import_val):
  total_val=0
  status_count1=0
  status_count2=0
  for val in range(7):
    curr_val = import_val[val][0]
    total_val = total_val + curr_val
    curr_val1 = import_val[val][1]
    if curr_val1 == "good":
      status_count1 = status_count1 + 1 
    else:
      status_count2 = status_count2 + 1 
    if ((total_val >= 42*60) and total_val <= (56*60)) and (status_count1 > status_count2):
      sleep_status = "you got enough sleep and on average you felt good when you woke up"
    elif ((total_val > (56*60) and total_val < (168 * 60))) and (status_count1 > status_count2):
      sleep_status = "you slept more than required but on average you felt good when you woke up"
    elif ((total_val > (56*60) and total_val <= (168 * 60))) and (status_count1 < status_count2):
      sleep_status = "you slept more than required and on average you didn't feel good when you woke up"
    else:
      sleep_status = "you didn't get enough sleep. Try getting more sleep. This much sleep isn't enough for you. We are worried about your health"
  total_val = round((total_val / 60), 1)
  with open('draft.txt', 'r') as dt:
        draft_val = dt.read()
  with open('return_file.txt', 'w') as rft:
        rft.write(draft_val.replace('<insert>', sleep_status).replace('<time>', str(total_val)))
  with open('return_file.txt', 'r') as rtft:
        final_output_val = rtft.read()
    
  return final_output_val
    
if __name__ == "__main__":    
    import_val = input_process()
    print(generate_output(import_val))

#assigned_val = [[61, 'good'], [121, 'not good'], [61, 'good'], [61, 'good'], [121, 'good'], [62, 'good'], [61, 'good']]

#def test_output():
    #c = generate_output(assigned_val) 
    #print(c.encode())
#test_output()
