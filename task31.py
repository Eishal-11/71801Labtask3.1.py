class Patient:
    def __init__(self, bme_name, bme_age, bme_heartRate, bme_spo2):
        self.bme_name = bme_name
        self.bme_age = bme_age
        self.bme_heartRate = bme_heartRate
        self.bme_spo2 = bme_spo2
        self.bme_status = "Not assessed"
    def assessStatus(self):
        bme_isCritical = False
        print("\nAssessing patient:", self.bme_name)
        if self.bme_heartRate < 60:
            print("Warning: Heart rate is very low")
            bme_isCritical = True
        if self.bme_heartRate > 100:
            print("Warning: Heart rate is still not  normal")
            bme_isCritical = True
        if self.bme_spo2 < 95:
            print("Warning: SpO2 level is abnormal")
            bme_isCritical = True
        if bme_isCritical:
            self.bme_status = "Critical"
        else:
            self.bme_status = "Stable"
        print("Patient Status:", self.bme_status)
    def displayInfo(self):
        print("\n----- Patient Information -----")
        print("Name:", self.bme_name)
        print("Age:", self.bme_age)
        print("Heart Rate:", self.bme_heartRate, "bpm")
        print("SpO2 Level:", self.bme_spo2, "%")
        print("Status:", self.bme_status)
bme_patient1 = Patient("fatima", 30, 78, 98)
bme_patient2 = Patient("meerab", 55, 112, 97)
bme_patient3 = Patient("rabia", 70, 52, 91)
bme_patient1.assessStatus()
bme_patient1.displayInfo()
bme_patient2.assessStatus()
bme_patient2.displayInfo()
bme_patient3.assessStatus()
bme_patient3.displayInfo()