from tkinter import N



setting = {"INPUT_FPS" : "30" , "OUTPUT_FORMAT" : "mp4", "YOLOV4-TINY" : "False", "FRAMEWORK" : "tf" , "MODEL" : "Yolov3" , 
            "IOU Threshold" : "0.45" , "Score" : "0.55" , "Dont_show" : "False" , "Info" : "True"} 

settingOption = {"1" : "INPUT_FPS" , "2" : "OUTPUT_FORMAT", "3" : "YOLOV4-TINY", "4" : "FRAMEWORK" , "5" : "MODEL" , 
            "6" : "IOU Threshold"  , "7" : "Score"  ,  "8" : "Dont_show"  , "9" : "Info"  , 0 : "All" } 



print("\nDefault Setting : \n")
print(setting)
print("\n")

default = input("Use default setting? (Y/N) : ")

if default == "Y":
    print("\nUsing default setting\n")
elif default == "N":
    print("\nChoose setting to change : \n")
    for key in settingOption:
        print(str(key) + " " + settingOption[key])
    keychosen = input("\nType separate by space : ").split()
    if "0" in keychosen: 
        print("Changing all setting option")
        for key,value in setting.items():
            setting[key] = input(key + " : ")
    else: 
        for i in keychosen:
            setting[settingOption[i]] = input(settingOption[i] + " : ")

print(setting)