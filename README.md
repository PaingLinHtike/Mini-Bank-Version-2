Here’s a polished, professional, Gen-Z-friendly **README.md** for your **file-based MiniBank system**. It’s clean, complete, and ready for GitHub.

---

# 🏦 MiniBank (File-Based Version)

MiniBank is a console-based banking system written in Python. This version extends the basic model by adding **persistent storage**, allowing all user data to be saved to and loaded from a text file (`userdata.txt`).

It supports user registration, login, money transfer, withdrawals, and account updates — all stored safely between sessions.

---

## ⭐ Key Features

### 🔐 User Authentication

* Register with a username, passcode, and starting balance.
* Log in using stored credentials from `userdata.txt`.

### 💾 Persistent Storage

* All user accounts are saved in a simple text file.
* Data reloads automatically every time the program runs.

### 💸 Banking Operations

* Transfer money to other users.
* Withdraw money from your own account.

### 🛠 Account Management

* Update username
* Change passcode
* Adjust balance (admin-like feature)

### 📘 Clean Data Management

* `loadData()` — reads from file
* `saveData()` — appends a new user
* `saveAllData()` — rewrites the entire file
* `updateUser()` — modifies data and persists changes

---

## ▶️ How to Run

1. Save the program as `mini_bank.py`
2. Make sure Python is installed.
3. Run the script:

```bash
python mini_bank.py
```

4. Choose:

   * **Press 1** → Login
   * **Press 2** → Register

---

## 🧠 How Data Is Stored

All user info is saved line-by-line in `userdata.txt`:

```
user_id,username,passcode,amount
1,john,1234,500
2,alice,2222,900
```

When the program starts:

* It loads this data into a dictionary:

```python
main_userInfo = {
    1: {"r_username": "john", "r_userpasscode": 1234, "amount": 500},
    2: {"r_username": "alice", "r_userpasscode": 2222, "amount": 900},
}
```

When updates happen (transfer, password change, etc.):

* Data is rewritten to the file.

---

## 📌 Function Overview

### **firstOption()**

Shows menu to choose login/register.

### **loadData()**

Reads all users from `userdata.txt`.

### **saveData()**

Appends a new user during registration.

### **saveAllData()**

Rewrites the file with updated user info.

### **existUser()**

Checks if login credentials match.

### **menu()**

Provides:

* Transfer
* Withdraw
* Update account info

### **updateUser()**

Modifies username, passcode, or balance and saves changes.

---

## 🧪 Example Flow

### Registration

1. Enter username
2. Enter and confirm passcode
3. Enter starting amount
4. System saves to `userdata.txt`

### Login

* Enter username + passcode
* If correct → enter banking menu

### Transfer

* Type target username
* Enter amount
* System checks balance, updates sender & receiver, rewrites file

---

