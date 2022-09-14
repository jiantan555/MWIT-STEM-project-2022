coding environment:
    ubuntu 22.04 (jammy jellyfish)
    virtual environment from anaconda
    python version 3.10.4
    flask version 2.1.3
    pyserial version 3.5


recieve data module: inputer.py

line 4: 
    define variable named arduino connecting to usb port with serial module
line 6: repeat this following forever:
    line 7: read data from port (sent by arduino uno)
    line 9-14: if data has number 1 do this following:
        1. note this moment's time into file state.txt
        2. stop module for 10 seconds
    line 15: wait 0.1 seconds


main program: app.py

line 7-11: 
    declare variable:
        1.  a for collecting sequence of number that show if each washing machine is empty (value=0 for unoccupied one value=1 for occupied one)
        2.  t for collecting sequence of time that each washing machine had started
        3.  z for collecting the remaining time for each washing machine to finish working (total 52 minutes)
        4.  reserve for colcting number sequence showing if each washing machine had reserved (value=0 for unreserved one value=1 for reserved one)
line 17-22:
    check if there new using washing machine (data in state.txt=0) and set variable a to 1 (occupied) and t to time(that noted in state.txt)
line 32-83:
    input data from html file if each washing machine has been occupied or reserved then set variable
line 85-86:
    set variable z (52-time)
line 87:
    push index.html with value of these variable:
        a: is occupied?
        z: time remained to finish
        reserve: is reserve?

# MWIT-STEM-project-2022
