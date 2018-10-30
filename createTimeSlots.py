import string

# this function creates for each participant: a list of dictionaries containing
# possible time slots per day name, weekNumber, interview name and  participant name
def timeSlotFactory(aDict,participantName, interviewName):
    fullList=[]
    for i in aDict["WeekNumber"]:
        for j in aDict["dayName"]:
            newDict ={}
            newDict["WeekNumber"]= i
            newDict["dayName"]=j
            startTime=timeStartManipulate(aDict["TimeStart"])
            endTime= timeEndManipulate(aDict["TimeEnd"])
            newDict["Slots"]=createIntervals(startTime,endTime)
            newDict["participantName"]=participantName
            newDict["interviewName"]=interviewName
            fullList.append(newDict)
    return fullList

#this function will concatenate all the dictionaries in one list
def listTimeSlot(*participants):
    finalList=[]

    for par in participants[0]:

        l =[]
        for k in range(len(par.availability)):
            finalList.append(timeSlotFactory(par.availability[k],
            par.participantName,par.interviewSubject))
    totalList= []
    for i in finalList:
        totalList=totalList+i
    return totalList

#this function will find the time slots for the interview
def getTimeSlots(*participants):

    fullList=[]
    for i in range(len(participants[0])-1):
        dictSlots= listTimeSlot(participants[0][i:i+2])

        listSlot=[]
        for i in range(len(dictSlots)):

            for j in range(len(dictSlots)):
                if dictSlots[i]["participantName"]!=dictSlots[j]["participantName"]:
                    if dictSlots[i]["WeekNumber"]== dictSlots[j]["WeekNumber"]:
                        if dictSlots[i]["dayName"] == dictSlots[j]["dayName"]:
                            dictio= {}
                            dictio["dayName"]=  dictSlots[j]["dayName"]
                            dictio["WeekNumber"]=  dictSlots[j]["WeekNumber"]
                            dictio["Slots"]=intersection(dictSlots[i]["Slots"],dictSlots[j]["Slots"])
                            if dictio["Slots"] == []:
                                continue
                            elif (dictio not in listSlot):
                                listSlot.append(dictio)
        fullList.append(listSlot)

    return fullList

def finalF(*participants):

    listDict= getTimeSlots(participants[0])

    bla =[]
    for e in listDict:
        bla = bla+ e

    for i in range(len(bla)):
        count=0
        for k in range(i,len(bla)):

            if bla[i]["dayName"]== bla[k]["dayName"] and bla[i]["Slots"]== bla[k]["Slots"]:
                count = count+1
                if count  == len(participants[0])-1:

                    print("WeekNumber",": ",bla[i]["WeekNumber"],"  " ,bla[i]["dayName"],"  " ,bla[i]["Slots"])
                #print(listDict[0][i]["WeekNumber"])

# this function is used to parse the TimeStart value
def timeStartManipulate(t):
    if ":" in t:
        start=int(t.split(":")[0])
        start=start +1
    else:
        start=int(t.strip(string.ascii_letters))
    if "pm" in t:
        start= start+12
    return start

# this function is used to parse the TimeEnd value
def timeEndManipulate(t):
    if ":" in t:
        end=int(t.split(":")[0])

    else:
        end= int(t.strip(string.ascii_letters))
    if "pm" in t:
        end= end+12

    return end

# this function is used to create time slots of one hour
def createIntervals(timeStart,timeEnd):
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