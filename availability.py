# this is an example of how availability can be expressed

# WeekNumber: is a number indicating if it is the current
#   week with value = 0 or you can increment by 1 for each additional week
#   for example for saying next week you can use 1
# dayName :is a list of day names
# Time start: is the hour in a day indicating at what time a Participant
# is available
# TimeEnd : is the hour in a day indicating at what time
#   a Participant is no longer available

# in case the time interval (TimeStart,TimeStart) and WeekNumber
# are  the same for different dayName we can use dayName as lists
# otherwise new objects should be created.


a1={"WeekNumber":1,'dayName':["Monday",'Tuesday',"Wednesday",'Thursday',"Friday"],
   'TimeStart':"9am",'TimeEnd':"4pm"}


a2={"WeekNumber":1,'dayName':["Monday","Wednesday"],
    'TimeStart':"12am",'TimeEnd':"6pm"}

a3={"WeekNumber":1,'dayName':['Tuesday','Thursday'],
    'TimeStart':"9am",'TimeEnd':"12am"}

a4={"WeekNumber":1,'dayName':["Monday",'Tuesday',"Wednesday",'Thursday',"Friday"],
    'TimeStart':"9am",'TimeEnd':"10am"}

a5={"WeekNumber":1,'dayName':["Wednesday"],
    'TimeStart':"10am",'TimeEnd':"12am"}


#a11={"WeekNumber":1,'dayName':['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    #'TimeStart':"9am",'TimeEnd':"4pm"}

#a12={"WeekNumber":1,'dayName':[ 'Friday'],
#    'TimeStart':"9am",'TimeEnd':"10am"}
