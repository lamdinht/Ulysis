option = {"INPUT_FPS" : "30" , "OUTPUT_FORMAT" : "mp4", "YOLOV4-TINY" : "False", "FRAMEWORK" : "tf" , "MODEL" : "Yolov3" , 
            "IOU Threshold" : "0.45" , "Score" : "0.55" , "Dont_show" : "False" , "Info" : "True"} 

default = input("Default setting? (Y/N) : ")
if default == "Y":
    print("Using default options")
elif default == "N":
    for key,value in option.items():
        option[key] = input(key + " : ")

print(option)