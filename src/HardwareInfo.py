import wmi 
from subprocess import check_output as sbp



class SystemInfo:


    @staticmethod
    def cpu():

        global system_os, system_username, system_cpu, system_cpu_cores, system_cpu_threads, system_virtualization, system_motherboard, system_memory, system_graphics 


        computer = wmi.WMI()
        computer_info = computer.Win32_ComputerSystem()[0]
        os_info = computer.Win32_OperatingSystem()[0]
        cpu_info = computer.Win32_Processor()[0]
        gpu_info = computer.Win32_VideoController()[0]

        system_username = computer_info.Username

        system_os = os_info.Caption

        system_os_version = os_info.Version

        system_cpu, system_cpu_cores, system_cpu_threads, system_virtualization = cpu_info.Name, cpu_info.NumberOfCores, cpu_info.ThreadCount, cpu_info.VirtualizationFirmwareEnabled

        system_motherboard = computer_info.Model

        system_motherboard_manafacturer = computer_info.Manufacturer

        system_memory = round((int(computer_info.TotalPhysicalMemory) / 1073741824))

        system_graphics = gpu_info.Name


       
SystemInfo.cpu()

def disk_info():

    disk_id = sbp('wmic logicaldisk get deviceid', shell=True).decode()
    disk_size = sbp('wmic logicaldisk get size', shell=True).decode()
    global primary_disk_signal, secondary_disk_signal, tertiary_disk_signal, quaternary_disk_signal, primary_disk, secondary_disk, tertiary_disk, quaternary_disk, one_system_disk, two_system_disk, three_system_disk, four_system_disk
    #Primary Disk
    try:
        primary_disk = str(disk_id.splitlines()[2]).replace(" ", "") + " " + str(round(float(disk_size.splitlines()[2]) / 1048576000)) + " GB"
        primary_disk_signal = True
    except ValueError:
        primary_disk_signal = False

    #Secondary Disk 
    try:
        secondary_disk = str(disk_id.splitlines()[4]).replace(" ", "") + " " + str(round(float(disk_size.splitlines()[4]) / 1048576000)) + " GB"
        secondary_disk_signal = True
    except ValueError:
        secondary_disk_signal = False

    #Tertiary Disk
    try:   
        tertiary_disk = str(disk_id.splitlines()[6]).replace(" ", "") + " " + str(round(float(disk_size.splitlines()[6]) / 1048576000)) + " GB"
        tertiary_disk_signal = True
    except ValueError:
        tertiary_disk_signal = False

    #Quaternary Disk
    try:
        quaternary_disk = str(disk_id.splitlines()[8]).replace(" ", "") + " " + str(round(float(disk_size.splitlines()[8]) / 1048576000)) + " GB"
        quaternary_disk_signal = True
    except ValueError:
        quaternary_disk_signal = False

    four_system_disk = False
    three_system_disk = False
    two_system_disk = False
    one_system_disk = False


    
    if quaternary_disk_signal == True:
        four_system_disk = True
    elif tertiary_disk_signal == True:
        three_system_disk = True
    elif secondary_disk_signal == True:
        two_system_disk = True
    elif primary_disk_signal == True:
        one_system_disk = True
    else:
        pass

    
    
    
    
    
    
    



SystemInfo.cpu()
disk_info()