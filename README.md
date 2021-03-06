# nrmp-algorithm
A Python implementation of (a derivative of) the National Residency Matching Program (NRMP) algorithm. This algorithm is similar to the Gale-Shapley algorithm; hospitals provide offers to students and students make decisions (either accept or decline said offers). Some key differences between this NRMP derivation and the Gale-Shapley include:
1. A hospital may be "matched" with one *or more* student(s) (depending on the number of "slots" said hospital has)
2. The total (cumulative) number of slots across all hospitals is less than the total number of students, meaning that some students will not be matched to a hospital (there is a *surplus* of students) <br>

Differences between this NRMP derivation and the original NRMP include:
1. Rankings (preferences lists) are exhaustive for both students and hospitals, meaning that each student must rank each hospital and vice versa (no exclusions)
2. There may be no *tied* (equal) rankings of students or hospitals (there may be no *indifference*)

## Instructions
### How to run
- To run the program, simply run `assignment1_part2_cpsc482_isayharaposo.py`
    - For reference, this program was written in Python 3.8.6, and requires the package `tabulate`, which can be installed using Pip by running `pip install tabulate`
    - The program will ask for the names of two desired input data files during execution unless two names are specified as arguments on the command line when running the program:
        - e.g., `assignment1_part2_cpsc482_isayharaposo.py example1_hospital_data.txt example1_student_data.txt` will run the program with the hospital and student data files used in example 1 (see **Examples**) specified
        - Note that the hospital data file should be the first argument, and the student data file should be the second
        - Also note that the file extension must be specified when specifying input data file names
        - Also note that the input data files must be in the same directory as the program itself
### Examples
- Two sets of example data are given:
    - example1_hospital_data.txt, example1_student_data.txt
    - example2_hospital_data.txt, example2_student_data.txt
- Images of the example data sets (inputs) can be found under the file names:
    - example1_input.png
    - example2_input.png
- Images of the corresponding outputs can be found under the file names:
    - example1_output.png
    - example2_output.png
### How to format input data
- For data input, this program accepts two distinctly formatted text files: one for hospital data, and one for student data
    - Said files must be formatted correctly, otherwise the program will either catch data formatting issue(s) and exit,
    output incorrect results, or simply crash
        - Data formatting issues that *are* caught by the program include:
            - Improper separation of slot count and preference list for some hospital(s)
            - Slot count of less than 1 for some hospital(s)
            - Preference list of size not equal to hospital count for some student(s)
            - Total (cumulative) slot count greater than or equal to student count
    - All data is numeric; hospitals and students are each referred to via numbers (sequential and beginning at 0)

- Correct formatting of the hospital data file is as follows:
    - Each line should contain data for a single hospital (line 0 contains data regarding hospital 0, etc.)
    - Each line should start with the hospital slot count, followed by the hospital's preference list; the two should be separated by a colon followed by a space (`: `)
    - A hospital's preference list should be ordered from most desired to least desired when read left to right. The indexes correspond to ranks, and the values correspond to student numbers:
        - e.g., The student number (value) at rank (index) 0 is more desired than that at rank (index) 1, etc.
    - Each student number in a hospital's preference list should be separated by a comma followed by a space (`, `)

- Correct formatting of the student data file is as follows:
    - Each line should contain data for a single student (line 0 contains data regarding student 0, etc.)
    - A student's preference list, unlike those of the hospitals, *should NOT be ordered from most desired to least desired when read left to right*. Instead, *to ensure the proper time complexity of the program*, the preference lists of the students are arranged in an *inverse* manner:
        - In other words, in a student's preference list, the *indexes* correspond to hospital numbers and the *values* correspond to ranks:
            - e.g., The first item (index 0) in a student's preference list has a value that corresponds to their *ranking* of *hospital 0*, the second item (index 1) in a student's preference list has a value that corresponds to their *ranking* of *hospital 1*, etc.
            - e.g., If the value at index 0 is less than that at index 2 in some student's preference list, this means that said student *prefers hospital 0 over hospital 2*.
    - Each line consists solely of the corresponding student's preference list, and so each ranking therein should be separated by a comma followed by a space (`, `)

- If any confusion arises about the difference between the hospital data format and the student data format, a demonstration image is included: `data_demonstration.png`

- For examples, see:
    - example1_hospital_data.txt, example2_hospital_data.txt for hospital data formatting
    - example1_student_data.txt, example2_student_data.txt for student data formatting
