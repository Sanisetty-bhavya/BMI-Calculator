**`INTRODUCTION:`**

Nowadays information and communication technology plays a great role in different areas or fields among thus Health Care System belongs to this. We took the scenario of a person  who needs a general checkup to prepare code evenly.

It stores data and enables functionality that organizes and maintains the medication use process within pharmacies. This project is focused on creating medical assistance using Python. 

This project is divided into two branches.

BRANCH 1: It deals with body mass index BMI. Body mass index is a value derived from the mass and height of a person. It estimates body fat and a good gauge of your risk for diseases that can occur with more body fat.

BRANCH 2: It helps us to find the suitable medicine for a disease. It also provides diet should be taken when diseased. It can lead to error free, secure, reliable and fast management system.

The provided code is a BMI (Body Mass Index) calculator implemented in Python. It includes functions to calculate BMI based on user-provided weight and height, as well as functionalities to determine the BMI category and potential health risks associated with that category. The program also incorporates an OTP (One-Time Password) verification system for access control.

This project contains 5 codes : 

1. **BMI Calculation:**
   - The `calculate` function takes user input for weight and height, calculates the BMI, and categorizes it into different classes (e.g., underweight, normal, overweight, obese).
   - It also prints the user's details and BMI in tabular form using the `tabulate` library.

2. **BMI Category and Health Risks:**
   - The `switch` function handles user input to either calculate BMI or inquire about health risks associated with specific BMI categories.
   - For each BMI category selected by the user, the code provides information about potential health risks and suggests dietary precautions, vitamins, and minerals needed.

3. **User Input and OTP Verification:**
   - The main program prompts the user to enter personal details such as name, gender, age, weight, and height.
   - An OTP (One-Time Password) is generated using the `random` module and presented to the user for access verification.
   - The user must enter the correct OTP to gain access to the BMI calculator functionality.

4. **Program Flow:**
   - The program uses nested loops to repeatedly prompt the user for OTP until the correct OTP is entered.
   - Once access is granted, the user can choose to calculate BMI, inquire about health risks, or exit the program.

5. **Exit Functionality:**
   - If the user chooses to exit, the program displays a thank-you message and terminates using `sys.exit()`.

It's important to note that this code seems to be designed for interactive use in a console or similar environment, given the use of user input prompts and console-based text display.

If you have any specific questions or if there's anything specific you'd like to know or modify in the code, feel free to let me know!

**`OUTPUT:`**

![image](https://github.com/Sanisetty-bhavya/BMI-Calculator/assets/114378144/1a88f805-d592-4add-b85d-ca8c16202586)
![image](https://github.com/Sanisetty-bhavya/BMI-Calculator/assets/114378144/08f482cf-6a33-4539-9321-b6a6692f5560)
![image](https://github.com/Sanisetty-bhavya/BMI-Calculator/assets/114378144/8b73bf60-2573-4933-af0a-67ae972f6c26)

**`CONCLUSION:`**
1. The code introduces classes such as `calculate` and `switch` to facilitate the functionality of a BMI calculator and health information tool. It utilizes the `tabulate` library for tabular data representation and integrates random OTP generation for user access.
2. The `calculate` function computes BMI based on user-provided weight and height, categorizes BMI, and prints relevant health information. The `switch` function directs users to disease details corresponding to their BMI category or allows them to exit the program.
3. The main program captures user details, validates access through OTP, and provides a menu-driven interface for BMI calculation and health information retrieval. The code emphasizes user engagement, offering a user-friendly experience for assessing BMI-related health risks.
4. The inclusion of specific health conditions associated with each BMI category demonstrates a thoughtful approach to user awareness and health education. The code encourages proactive engagement with one's well-being through informative outputs.
5. While the code achieves its intended purpose, it could benefit from further organization, comments, and possibly modularization to enhance readability and maintainability. Additionally, error handling mechanisms could be integrated to improve user experience.
