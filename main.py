from Participant import Participant
from availability import *
from createTimeSlots import *

# create new participants
interv = Participant('Backend',"Philip",a1)
inter2 =Participant('Backend',"Sarah",a2,a3)
candidate =Participant('Backend',"Carl",a4,a5)
candidate2 =Participant('Backend',"Carl2",a4,a5)

# concat all the participants in one list
participants = [interv,candidate,inter2]

# call get_interview_slots function
print(get_interview_slots(participants))

