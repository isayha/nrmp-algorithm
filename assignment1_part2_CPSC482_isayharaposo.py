# Assignment 1
# Part 2 (Python Source Code)
# CPSC 482
# Isayha Raposo
# Student Number: 230133508

import sys
from files import *
from tabulate import tabulate # Requires package "tabulate" (pip install tabulate)

hospitalData, studentData = getData(sys.argv)

totalSlotsAvailable = 0 # The total number of slots (positions) available across all hospitals
hospitalSlots = [] # Contains the number of slots (positions) available at each hospital
# index = hospital number, value = slots available
hospitalPrefLists = [] # Contains each hospital's list of preferred students ordered from most to least preferred
# index = hospital number, value = preference list, preference list index = rank (least index = most preferred), preference list value = student number
studentPrefLists = [] # Contains each student's list of preferred hospitals ordered from most to least preferred
# index = student number, value = preference list, preference list index = rank (least index = most preferred), preference list value = hospital number
hospitalsToMatch = [] # Used to optimize situations in which a later hospital matches to a student previously
# matched to an earlier hospital, which unmatches said student from the earlier hospital
# (Contains only the hospital numbers of hospitals where the number of slots available is greater than 0, and thus
# removes any need for checking the number of available slots at each hospital to determine whether or not they have slots
# to fill)
# index = arbitrary, value = hospital number

# Parse hospitalData:
hospitalCount = 0 # The total number of hospitals
dataLine = hospitalData.readline().strip('\n')
while not (dataLine == ""):
    try:
        slots, prefsLine = dataLine.split(": ")
    except ValueError:
        handleDataIssue(True, ("hospitalData incorrectly formatted for hospital " + str(hospitalCount) + "."))

    handleDataIssue((int(slots) < 1), ("Hospital " + str(hospitalCount) + " has less than 1 slot available."))

    hospitalSlots.append(int(slots))
    totalSlotsAvailable += int(slots)
    prefs = prefsLine.split(", ")
    hospitalPrefLists.append([int(student) for student in prefs])
    hospitalsToMatch.append(hospitalCount)
    hospitalCount += 1
    dataLine = hospitalData.readline().strip('\n')

# Parse studentData:
studentCount = 0 # The total number of students
dataLine = studentData.readline().strip('\n')
while not (dataLine == ""):
    prefs = dataLine.split(", ")

    handleDataIssue((len(prefs) != hospitalCount), ("Preference list length for student " + str(studentCount) + " not equal to hospitalCount."))
    
    studentPrefLists.append([int(hospital) for hospital in prefs])
    studentCount += 1
    dataLine = studentData.readline().strip('\n')

handleDataIssue((studentCount <= totalSlotsAvailable), "totalSlotsAvailable greater than or equal to studentCount.")

matches = [None] * studentCount # Used to store matches (index = hospital number, value = student number)

nextHospitalsToMatch = [] # List of hospitals that will have slots available to fill in the next iteration of the while loop below (if any)
# See inline comment for hospitalsToMatch (lines 17 - 19)

while totalSlotsAvailable > 0:
    for hospital in hospitalsToMatch:
        hospitalPrefList = hospitalPrefLists[hospital]
        while len(hospitalPrefList) > 0:
            student = hospitalPrefList[0]
            otherHospital = matches[student]
            if otherHospital is None:
                matches[student] =  hospital
                hospitalSlots[hospital] -= 1
                totalSlotsAvailable -= 1
            elif not (otherHospital == hospital):
                hospitalRanking = studentPrefLists[student][hospital]
                otherHospitalRanking = studentPrefLists[student][otherHospital]
                if hospitalRanking > otherHospitalRanking:
                    matches[student] = hospital
                    if hospitalSlots[otherHospital] == 0:
                        nextHospitalsToMatch.append(otherHospital)
                    hospitalSlots[hospital] -= 1
                    hospitalSlots[otherHospital] += 1
            hospitalPrefList.pop(0)
            if hospitalSlots[hospital] == 0:
                break
    hospitalsToMatch = nextHospitalsToMatch

print("\nResults:")
print(tabulate(enumerate(matches), headers=["Student:", "Hospital:"]))

