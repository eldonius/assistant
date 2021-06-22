import names
import datetime

Name = ""
minlength = 0
maxlength = 9999
excluded = ""
timeout = 1000000
Help = {"help", "commands"}
Exit = {"exit", "close", "go away"}
Time = {"time", "date", "day"}
Write = {"write", "type", "overwrite"}
Read = {"open",}
Append = {"append", "write more", "type more"}
while 1==1:
    x = str(input())
    if x in Help:
        print("help: shows a list of commands\nexit: close the program\ntime: output time and date\nwrite: write and save a text document\nopen: read a text document\nappend: write in a text document without overwriting existing text\nname: generate a name")
    elif x in Exit:
        print("Shutting down")
        break
    elif x in Time:
        print(datetime.datetime.now())
    elif x in Write:
        f = open (str(input())+".txt", "w")
        f.write(str(input()))
        f.close
    elif x in Read:
        try:
            f = open(str(input()) + ".txt", "r")
            print(f.read())
            f.close()
        except:
            print("That file is missing, corrupt, or doesn't exist")
    elif x in Append:
        f = open (str(input())+".txt", "a")
        f.write(str(input()))
        f.close
    elif "name" in x:
        print("What do you want to see in your name?\ninclude: name must contain set characters\nminlength: name must be at or above set length\nmaxlength: name must be at or below set length\ngenerate: make the name\nexclude: name must not contain set characters\nsettings: preview the conditions\ntimeout: configure timeout")
        while 1==1:
            y = input()
            if "include" in y:
                Name = input()
            elif "minlength" in y:
                minlength = int(input())
            elif "maxlength" in y:
                maxlength = int(input())
            elif "settings" in y:
                if Name == "":
                    NAME = "None"
                else:
                    NAME = Name
                print ("including: " + str(NAME) + "\nminlength: " + str(minlength) + "\nmaxlength: " + str(maxlength) + "\nexcluding: " + excluded + "\ntimeout: " + str(timeout))
            elif "exclude" in y:
                excluded = input()
            elif "timeout" in y:
                Timeout = int(input())
                if Timeout >= 2000001:
                    assurance = input("timeout is higher than recommended. Are you sure? (y/n)")
                    if assurance == "y":
                        timeout = Timeout
                else:
                    timeout = Timeout
            else:
                break
        for i in range(timeout):
            correction = True
            output = names.name(1)
            separation = len(output)
            for j in range (len(output)):
                if output[j] not in excluded:
                    separation -= 1
            if Name in output:
                if minlength <= len(output):
                    if maxlength >= len(output):
                        if separation == 0:
                            print(output)
                            correction = False
                            break
        if correction:
            print("Could not generate a name containing " + Name)
            if excluded in Name:
                print("Cannot include " + Name + " while excluding " + excluded)
            if len(Name) > maxlength:
                print(Name + " is too large for maximum length")
    else:
        print("Invalid command")