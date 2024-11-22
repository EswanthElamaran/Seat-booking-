import csv

class PassengerRegistration():
    #constructor
    def __init__(self):
        self.passengerName = None
        self.noOfPassenger = None
        self.showtime = None
        self.ddmmyyyy = None
        self.seatNo = None
        self.selectBusType = None
        self.busFare = None
        self.autoInc = 1
        self.countcol= 0
        
    def getPassengerInfo(self):
        
        print("1: kANGUVA")
        print("2: AMARAN")
        print("3: PUSHPA 2 THE RULE")
        print("4: DEADPOOL AND WOLVERINE")
        self.noOfPassenger     = int(input("Enter Movie name :"))

        # Enter departure Location Name START
        print("1. 8.00")
        print("2. 11.30")
        print("3. 2.15")
        print("4. 6.45")
        print("5. 9.45")
        self.dl = int(input("Enter Show Time"))
        if self.dl == 1:
            self.showtime = "8.00"
        elif self.dl == 2:
            self.showtime = "11.30"
        elif self.dl == 3:
            self.showtime = "2.15"
        elif self.dl == 4:
            self.showtime = "6.45"
        elif self.dl == 5:
            self.showtime = "9.45"
        else:
            print("Please Enter correct choice  :")
        # departure Location Name END

        self.ddmmyyyy = input("Enter Date of movie to watch Like 07-05-1992   :")  #Date of Journey

        #Booking Seat Start 
        print("[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]")
        print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]")
        print("[21]_[22]_[23]_[24]_[25]_[26]_[27]_[28]_[29]_[30]")
        print("[31]_[32]_[33]_[34]_[35]_[36]_[37]_[38]_[39]_[40]")

        seatNoList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
        self.bookingList=[]
        while True:
            self.seatNo = int(input("Choose a Seat Number & Max To Max You Can Book Two Ticket  :"))
            if self.seatNo <=40:
                
                if  self.seatNo in seatNoList:
                    self.bookingList.append(self.seatNo)
                    del seatNoList[self.seatNo+1]
                    count = len(seatNoList)
                else:
                    print("Ticket Allready Booked")
                print("Do You Want To Book One More Seat Enter (Yes/No)") 
                y = input("") 
                if y == "Yes":
                    pass
                else:
                    break

            else:
                print("Don't Choose a Seat Number Which is Not Available")    
        # Booking Seat END
        
        print(" 1. 2D  = 150 Fare")
        print(" 2. 3D  =  200 Fare")
        self.busType = int(input("Select  Type  :"))
        
        if self.busType == 1:
            self.selectBusType = "2D"
            self.busFare = self.noOfPassenger*150
        elif self.busType == 2:
            self.selectBusType = "3D"
            self.busFare = self.noOfPassenger*200
           
        # Booking Seat END
#=============================================
#saving Passenger Data into csv File
#=============================================
class PassengerDataCsv(PassengerRegistration):
    def saveInfo(self):
        try:
            with open("passengerData.csv",'r+',newline="") as f:
                r =  csv.reader(f)
                data = list(r)
                #print(self.data)
                for  i in data:
                    self.autoInc += 1
                    for j in i:
                        self.countcol +=1
                    print()
                print("Number of Records Are Found In Database :",self.autoInc)    
            
        except:
            print("File has not available")
        finally:     
            with open("passengerData.csv",'a+',newline="") as f:
                w =  csv.writer(f)
                #w.writerow(["Auto Increment","passenger Name","Number of Passenger","","Destination Location","ddmmyyyy","Seat No","Select Bus Type","Bus Fare"])
                w.writerow([self.autoInc,self.passengerName,self.noOfPassenger,self.showtime,self.ddmmyyyy,self.bookingList,self.selectBusType,self.busFare])
                print("Data Save successfully")
                print()
        

'''pd_obj = PassengerDataCsv()
pd_obj.getPassengerInfo()
pd_obj.saveInfo()'''
