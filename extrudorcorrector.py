def main():
    print("ExtruderCorrector v0.1")
    print("Measure 120mm of filament of the edge of your extruder and mark it")
    print("Let the extruder run for 100mm")
    print("Now measure the remaining filament of the edge to the mark")
    old_steps = float(input("Please enter the STEPS/MM of your printer : "))
    measured_length = float(input("Please enter the measured length : "))
    real_length = 120 - measured_length
    if(measured_length > 20):
        new_steps = (old_steps / real_length) * 100
    elif(measured_length == 20):
        pass
    else:
        new_steps = (old_steps / real_length) * 100
    print("Please configure the steps of your printer to be : " + str(new_steps))
    print("Then test again.")


if __name__=='__main__':
    main()


