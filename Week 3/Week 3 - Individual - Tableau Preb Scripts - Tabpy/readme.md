# Week 3 - Individual - Tableau Preb Scripts - Tabpy
Anushka Sawant

1. Objective
This exercise aimed to show how Python scripts can be embedded in a Tableau Prep workflow through the TabPy analytics extension. The task involved taking an employee dataset (employee_tableau_prep_python_sample.csv) and filtering it by department while also calculating and attaching company-wide statistics to the output.


2. Dataset Overview
The dataset contained 15 employee records across the following fields:

Employee_ID (String)
Employee_Name (String)
Department (String)
Age (Integer)
Salary (Integer)
Hire_Date (Date/String)
City (String)


An initial inspection of the raw data showed no missing values. Employees spanned several departments including IT, Finance, HR, and Marketing.
3. Workflow Configuration and Execution
A local TabPy server was launched from the command line on port 9004, after which Tableau Prep was pointed to that analytics extension to enable the integration.

The Python Script
A Python script (prep_employee_script.py) was written using the pandas library to carry out the necessary transformations. It was built around two main functions:

get_output_schema(): Defined the output DataFrame's expected structure for Tableau Prep, with data types correctly mapped (e.g., prep_string(), prep_int(), prep_decimal()).
process_employee_data(df): Contained the core transformation logic:

Metric Calculation: Computed the mean salary across all records using df['Salary'].mean().
Identification: Located the oldest employee in the company by finding the maximum Age value and pulling the corresponding Employee_Name and Department.
Filtering: Narrowed the DataFrame down to only those employees where Department == 'IT'.
Column Appending: Added the computed metrics (Average_Salary_All_Employees, Oldest_Employee_Name, Oldest_Employee_Department) as new columns on the filtered IT dataset.



4. Results and Output
The TabPy script executed within Tableau Prep and produced the expected results without any discrepancies:

Row Filtering: The full 15-row dataset was successfully trimmed to include only IT department employees.
Calculated Columns: Three new columns were correctly added to every remaining row:

Average_Salary_All_Employees: Reflected the mean salary computed from all 15 original records.
Oldest_Employee_Name: Correctly captured the oldest person in the company before any filtering took place.
Oldest_Employee_Department: Captured the department that oldest employee belonged to.


5. Conclusion
This exercise demonstrated how TabPy can meaningfully extend what Tableau Prep can do on its own. Although Tableau Prep handles standard data cleaning well, bringing Python into the mix enables more sophisticated, multi-step logic — such as deriving global statistics before applying row-level filters — all within a single Script Step. The resulting dataset came out correctly structured, filtered, and enriched with additional metrics, ready to be visualized in Tableau Desktop.