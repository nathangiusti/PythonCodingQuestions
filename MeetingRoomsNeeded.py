
# Given a collection of meetings (each has a start time and an end time, positive integer type, start time is inclusive and end time is exclusive, input is always valid).
# Return how many meeting rooms are needed at least to hold all the meetings.
# [(1,3), (6,8), (4,5)] -> 1
# ##*******
# *****##**
# ***#*****
#
# [(1,2), (4,6), (3,5)] -> 2
# #*********
# ***##*****
# **##******
#
# [(1,7), (2,4), (5,6)] -> 2
# ######****
# *##*******
# ****#*****
#
# [(1,7), (2,5), (4,6)] -> 3
# ######****
# *###******
# ***##*****

NUM_HOURS = 9


def get_number_of_meeting_rooms(schedule):
    schedule_block = [0] * NUM_HOURS
    for start, end in schedule:
        schedule_block[start] = schedule_block[start] + 1
        schedule_block[end] = schedule_block[end] - 1

    num_rooms = 0
    counter = 0

    for entry in schedule_block:
        counter += entry
        num_rooms = counter if counter > num_rooms else num_rooms

    return num_rooms


print(get_number_of_meeting_rooms([(1, 3), (6, 8), (4, 5)]))
print(get_number_of_meeting_rooms([(1, 2), (4, 6), (3, 5)]))
print(get_number_of_meeting_rooms([(1, 7), (2, 4), (5, 6)]))
print(get_number_of_meeting_rooms([(1, 7), (2, 5), (4, 6)]))




