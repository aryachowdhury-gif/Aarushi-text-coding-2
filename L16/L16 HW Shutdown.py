import os

shutdown = input("Do you wish to shutdown your computer ? (Yes/No): ")

if shutdown.lower() == "No":
    exit()
elif shutdown.lower() == "Yes":
    os.system("shutdown /s /t 1")
else:
    print("invalid input")