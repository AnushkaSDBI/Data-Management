import pandas as pd

def process_employee_data(df):
    # 1. Average salary of all employees (before filtering)
    avg_salary = df['Salary'].mean()
    
    # 2. Oldest employee (before filtering)
    oldest_idx = df['Age'].idxmax()
    oldest_name = df.loc[oldest_idx, 'Employee_Name']
    oldest_dept = df.loc[oldest_idx, 'Department']
    
    # 3. Filter employees from the IT department
    df_filtered = df[df['Department'] == 'IT'].copy()
    
    # 4. Return results as new columns
    df_filtered['Average_Salary_All_Employees'] = float(avg_salary)
    df_filtered['Oldest_Employee_Name'] = oldest_name
    df_filtered['Oldest_Employee_Department'] = oldest_dept
    
    return df_filtered

def get_output_schema():
    return pd.DataFrame({
        'Employee_ID': prep_string(),
        'Employee_Name': prep_string(),
        'Department': prep_string(),
        'Age': prep_int(),
        'Salary': prep_int(),
        'Hire_Date': prep_string(),
        'City': prep_string(),
        'Average_Salary_All_Employees': prep_decimal(),
        'Oldest_Employee_Name': prep_string(),
        'Oldest_Employee_Department': prep_string()
    })