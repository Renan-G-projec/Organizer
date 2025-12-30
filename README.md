# 🗃️ Python note organizer
This is a simple python script developed to organize notes (markdown or text files) by date in a month using the files metadata. **Currently, it is developed only for linux systems**.

## 🚀 Features
- **Smart Categorization**: The user can define a designed path to move the notes.wh
- **Documentation** This can help you to organize a daily log in a nice way.

## 🔋 Technologies
- **Python 3.11**
- **OS module**
- **Shutil module**

## 🔨 How to use
1. Clone the repository using:
```git clone https://github.com/Renan-G-projec/Organizer.git```
2. Open the terminal in the folder `/organizer/` and run:
```python config.py```
3. Answer the wizard questions.
4. Run `organizer.py` to move all all the files in the `/filebuffer/` folder to the designed path! Command:
```python organizer.py``` 

## ⏱️ Future Features
- [ ] **Conflict Resolution**: Logic to handle files with identical names caused by multiple files in the buffer.
- [ ] **Naming Strategies**: Option to merge content or add suffixes (e.g., `30-day-1.md`).