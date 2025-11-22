class MiniBank:

    main_userInfo: dict = {}

    def firstOption(self):
        option : int = int(input("Press1 to Login.\nPress2 to register."))
        if option == 1:
            self.login()
        else:
            self.register()

    def returnId(self, transfer_username):
        userInfo_length : int = len(self.main_userInfo)
        for i in range(1, userInfo_length+1):
            if self.main_userInfo[i]["r_username"] == transfer_username:
                return i
        return None

    def menu(self,loginId):
        menu_input = int(input("Press1 to Transfer\nPress2 to Withdraw\nPress3 to update user data:"))
        if menu_input == 1:
            transfer_username : str = input("\nEnter username to transfer: ")
            transfer_id : int = self.returnId(transfer_username)
            if transfer_id == None:
                print("\nThere is no such user.\n")
            else:
                if transfer_id == loginId:
                    print("\nCan't Transfer to own account.\n")
                else:
                    print("\nTransfer Id: ", transfer_id)
                    print("My Id: ", loginId)
                    amount :int = int(input("\nEnter amount to transfer {0}:".format(self.main_userInfo[transfer_id]["r_username"])))
                    if amount > self.main_userInfo[loginId]["amount"]:
                        print("You don't have enough money!")
                    else:
                        self.main_userInfo[loginId]["amount"] -= amount
                        self.main_userInfo[transfer_id]["amount"] += amount
                        self.saveAllData()
                        print("\nYou have transferred a total of ${0} to {1}.\n".format(amount, transfer_username))
                    print("Current amount: $", self.main_userInfo[loginId]["amount"],"\n\n")

        elif menu_input == 2:
            wcurrent_amount :int = self.main_userInfo[loginId]["amount"]
            print("\nCurrent amount: $", wcurrent_amount)
            amount: int = int(input("Enter amount to withdraw: "))
            if amount > wcurrent_amount:
                print("\nYou don't have enough money!\n")
            else:
                new_balance = wcurrent_amount - amount
                self.updateUser(loginId, new_amount=new_balance)
            print("Latest amount: $", self.main_userInfo[loginId]["amount"],"\n")
        elif menu_input == 3:
            user_info = self.main_userInfo[loginId]
            uoption :int = int(input("\nPress1 to change name\nPress2 to change password\nPress3 to change amount:"))
            if uoption == 1:
                new_name :str = input("\nEnter new username: ")
                self.updateUser(loginId, new_username=new_name)
            elif uoption == 2:
                new_password :int = int(input("\nEnter new password: "))
                self.updateUser(loginId, new_passcode=new_password)
            elif uoption == 3:
                new_amount :int = int(input("\nEnter new amount: "))
                self.updateUser(loginId, new_amount=new_amount)

    def login(self):
        print("\n______________This is login______________\n")

        l_username : str = input("Pls enter username to Login: ")
        l_userpasscode : int = int(input("Pls enter passcode to Login: "))

        existUser = self.existUser(l_username, l_userpasscode)
        if(existUser):
            print("\n______________Login Successful______________\n")
            loginId=self.returnId(l_username)
            self.menu(loginId)
        else:
            print("\nU can't Login!\n")

    def existUser(self, l_username, l_userpasscode):
        self.loadData()
        user_count = len(self.main_userInfo)
        for i in range(1,user_count+1):
            if (self.main_userInfo[i]["r_username"] == l_username and
                self.main_userInfo[i]["r_userpasscode"] == l_userpasscode):
                return True
        return False

    def register(self):
        print("\n______________This is register______________\n")
            # id: int = self.checkUserCount()
            # userInfoForm: dict = {id:{"r_username":r_username, "r_userpasscode":r_userpasscode1, "amount":r_amount}}
            # self.main_userInfo.update(userInfoForm)
        self.saveData()

    def loadData(self):
        try:
            with open("userdata.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if line == "":
                        continue

                    user_id, username, passcode, amount = line.split(",")

                    user_id = int(user_id)
                    passcode = int(passcode)
                    amount = int(amount)

                    self.main_userInfo[user_id] = {
                        "r_username": username,
                        "r_userpasscode": passcode,
                        "amount": amount
                    }

        except FileNotFoundError:
            print("File not found. Starting with empty data.\n\n")

    def saveData(self):
        self.loadData()

        if len(self.main_userInfo) == 0:
            new_id = 1
        else:
            new_id = max(self.main_userInfo.keys()) + 1

        r_username : str = input("Pls enter username to Register: ")
        for user_id in range(1, max(self.main_userInfo.keys()) + 1):
            if r_username == self.main_userInfo[user_id]["r_username"]:
                print("Username already taken.\n")
                return

        r_userpasscode1: int = int(input("Pls enter passcode to Register: "))
        r_userpasscode2: int = int(input("Pls enter again passcode to com: "))

        if r_userpasscode1 == r_userpasscode2:
            r_amount: int = int(input("Pls enter amount to register: "))
            with open("userdata.txt", "a") as file:
                contents = f"{new_id},{r_username},{r_userpasscode1},{r_amount}\n"
                file.write(contents)
        else:
            print("Doesn't match passwords.\n\n")
            return
        print("______________Successfully Registered_____________\n\n")
        print(self.main_userInfo)

    def updateUser(self,user_id, new_username=None, new_passcode=None, new_amount=None):
        self.loadData()

        userData = self.main_userInfo[user_id]

        if new_username is not None:
            userData["r_username"] = new_username
        if new_passcode is not None:
            userData["r_userpasscode"] = new_passcode
        if new_amount is not None:
            userData["amount"] = new_amount

        self.saveAllData()
        print("\nNew User Details: ", userData)

    def saveAllData(self):
        with open("userdata.txt", "w") as file:
            for user_id, data in self.main_userInfo.items():
                line = f"{user_id},{data['r_username']},{data['r_userpasscode']},{data['amount']}\n"
                file.write(line)
        print("Updated data saved to file.\n")

if __name__ == '__main__':
    miniBank : MiniBank = MiniBank()
    while True:
        miniBank.firstOption()
        miniBank.main_userInfo


