import string


# this function will return a list of possible time slots
def get_interview_slots(*participants):

    list_dict= get_list_slots(participants[0])

    one_list =[]
    for e in list_dict:
        one_list = one_list+ e

    final_list_slots=[]
    for i in range(len(one_list)):

        count=0
        for k in range(i,len(one_list)):

            if one_list[i]["dayName"]== one_list[k]["dayName"] and one_list[i]["Slots"]== one_list[k]["Slots"]:
                count = count+1
                if count  == len(participants[0])-1:

                    result='WeekNumber: {0} , {1}  {2} '.format(one_list[i]["WeekNumber"],one_list[i]["dayName"],one_list[i]["Slots"])
                    final_list_slots.append(result)
    return final_list_slots


# this function creates for each participant: a list of dictionaries containing
# possible time slots per day name, weekNumber, interview name and  participant name

def time_slot_factory(availability_dict,participantName, interviewName):

    fullList=[]
    for j in availability_dict["dayName"]:
        new_dict ={}
        new_dict["WeekNumber"]= availability_dict["WeekNumber"]
        new_dict["dayName"]=j
        startTime=time_start_manipulate(availability_dict["TimeStart"])
        endTime= time_end_manipulate(availability_dict["TimeEnd"])
        new_dict["Slots"]=create_intervals(startTime,endTime)
        new_dict["participantName"]=participantName
        new_dict["interviewName"]=interviewName
        fullList.append(new_dict)
    return fullList

#this function will concatenate all the dictionaries in one list
def list_time_slot(*participants):
    final_list=[]

    for par in participants[0]:

        for k in range(len(par.availability)):
            final_list.append(time_slot_factory(par.availability[k],
            par.participantName,par.interviewSubject))
    total_list= []
    for i in final_list:
        total_list=total_list+i
    return total_list

#this function will find the time slots for a couple of participants
def get_list_slots(*participants):

    full_list=[]
    for i in range(len(participants[0])-1):
        dict_slots= list_time_slot(participants[0][i:i+2])

        listSlot=[]
        for i in range(len(dict_slots)):

            for j in range(len(dict_slots)):
                if dict_slots[i]["participantName"]!=dict_slots[j]["participantName"]:
                    if dict_slots[i]["WeekNumber"]== dict_slots[j]["WeekNumber"]:
                        if dict_slots[i]["dayName"] == dict_slots[j]["dayName"]:
                            new_dict= {}
                            new_dict["dayName"]=  dict_slots[j]["dayName"]
                            new_dict["WeekNumber"]=  dict_slots[j]["WeekNumber"]
                            new_dict["Slots"]=intersection(dict_slots[i]["Slots"],dict_slots[j]["Slots"])
                            if new_dict["Slots"] == []:
                                continue
                            elif (new_dict not in listSlot):
                                listSlot.append(new_dict)
        full_list.append(listSlot)

    return full_list



# this function is used to parse the TimeStart value
def time_start_manipulate(t):
    if ":" in t:
        start=int(t.split(":")[0])
        start=start +1
    else:
        start=int(t.strip(string.ascii_letters))
    if "pm" in t:
        start= start+12
    return start

# this function is used to parse the TimeEnd value
def time_end_manipulate(t):
    if ":" in t:
        end=int(t.split(":")[0])

    else:
        end= int(t.strip(string.ascii_letters))
    if "pm" in t:
        end= end+12

    return end

# this function is used to create time slots of one hour
def create_intervals(timeStart,timeEnd):
    listOfTime=[]
    for i in range(timeStart,timeEnd):
        list=[]
        list.append(i)
        list.append(i+1)
        listOfTime.append(list)
    return listOfTime

# this function is used to find intersection of elements inside two lists
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3