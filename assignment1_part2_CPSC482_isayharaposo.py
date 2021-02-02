# Assignment 1
# Part 2 (Python Source Code)
# CPSC 482
# Isayha Raposo
# Student Number: 230133508

import sys
from files import *

hospitalData, studentData = getData(sys.argv)

totalSlotsAvailable = 0 # Contains the total number of slots (positions) available across all hospitals
hospitalSlots = [] # Contains the number of slots (positions) available at each hospital
hospitalPrefLists = [] # Contains list of hospital's preferred students (ordered from most to least preferred) for each hospital
studentPrefLists = [] # Contains list of student's preferred hospitals (ordered from most to least preferred) for each student

hospitalCount = 0
dataLine = hospitalData.readline().strip('\n')
while not (dataLine == ""):
    slots, prefsLine = dataLine.split(": ")
    hospitalSlots.append(slots)
    totalSlotsAvailable += int(slots)
    prefs = prefsLine.split(", ")
    hospitalPrefLists.append([int(student) for student in prefs])
    hospitalCount += 1
    dataLine = hospitalData.readline().strip('\n')

studentCount = 0
dataLine = studentData.readline().strip('\n')
while not (dataLine == ""):
    prefs = dataLine.split(", ")
    studentPrefLists.append([int(hospital) for hospital in prefs])
    studentCount += 1
    dataLine = studentData.readline().strip('\n')

hospitalSlots = [int(slots) for slots in hospitalSlots]

if studentCount < totalSlotsAvailable:
    print("Data issue detected:")
    print("totalSlotsAvailable greater than studentCount.")
    print("Please check and/or correct data.")
    print("Exiting...")
    sys.exit(1)

matches = [None] * studentCount

print(str(hospitalSlots) + "\n") # TEST ONLY
print(str(studentPrefLists) + "\n") # TEST ONLY
print(str(hospitalPrefLists) + "\n") # TEST ONLY

while any(hospitalSlots):
    for hospital, hospitalPrefList in enumerate(hospitalPrefLists):
        print(hospital)
        if hospitalSlots[hospital] > 0:
            for student in hospitalPrefList:
                otherHospital = matches[student]
                if otherHospital is None:
                    matches[student] =  hospital
                    hospitalSlots[hospital] -= 1
                elif not (otherHospital == hospital):
                    hospitalRanking = studentPrefLists[student][hospital]
                    otherHospitalRanking = studentPrefLists[student][otherHospital]
                    if hospitalRanking > otherHospitalRanking:
                        matches[student] = hospital
                        hospitalSlots[hospital] -= 1
                        hospitalSlots[otherHospital] += 1
                print(matches)
                print(hospitalSlots)
                if hospitalSlots[hospital] == 0:
                    break

print(matches)

# Change hospitals to numbers? That way the pref list for students can just have index = hospital and value = rank, rather than the opposite
# Maybe use "any()"?

# Main input file processing:
# .readline()

# What we don't know:
# Maybe we do two input files?
# Maybe we do more than one .py/proper OOP?
# Do hospitals have more than one slot?
# Does each hospital need to rank each student (and vice versa)?
    # (Can there be exclusions)
# Can there be "tied" rankings among hospitals (or students)
    # This is the same as *indifference* in the rankings

# What we do know:
# Assume a surplus of students
# Hospitals "propose" (provide offers) to students
    # In the Gale-Shapley Algorithm this would make the
    # Hospitals men and the Students women
# Should terminate when no hospital (hospital slot?) is free
    # While there is a hospital who is free and hasn't provided an
    # offer to every student...
    # Should be O(m*n)
        # (At most, every Hospital proposes to every Student)

