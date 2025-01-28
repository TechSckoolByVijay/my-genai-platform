## CSV_manipulation.ps1

This script is used for manipulating CSV data. It performs the following operations:

1. Imports a CSV file named 'sample.csv' using the 'Import-Csv' cmdlet.
2. Filters and retrieves records where the SalaryGrade starts with 'A'.
3. Filters and retrieves records where the SalaryGrade starts with 'A' and the Department is 'CS'.
4. Replaces the SalaryGrade value with 'High' if it starts with 'A' and with 'Medium' if it starts with 'B'.
5. Adds a new row to the data with values for EmployeeName, Role, Department, and SalaryGrade.
6. Adds a new column 'Group' based on the 'Department' value. Employees in the 'Sales' department are assigned to the 'Non-Technical' group, while others are assigned to the 'Technical' group.
7. Removes all columns from the data except for the selected columns.
8. Exports the modified data to a CSV file named 'sample.csv'.

### Prerequisites

- PowerShell

### Usage

1. Open a PowerShell terminal.
2. Navigate to the directory containing the script: `cd C:\Learning Lab\my-genai-platform\out`.
3. Run the script: `.\CSV_manipulation.ps1`.

### Script Execution Flow

1. Import the 'sample.csv' file using the 'Import-Csv' cmdlet.
2. Filter the data to fetch records where the SalaryGrade starts with 'A'.
3. Filter the data to fetch records where the SalaryGrade starts with 'A' and the Department is 'CS'.
4. Replace the SalaryGrade value with 'High' if it starts with 'A' and with 'Medium' if it starts with 'B'.
5. Add a new row to the data with values for EmployeeName, Role, Department, and SalaryGrade.
6. Add a new column 'Group' based on the 'Department' value.
7. Assign employees in the 'Sales' department to the 'Non-Technical' group.
8. Assign employees in other departments to the 'Technical' group.
9. Remove all columns from the data, except for the selected columns.
10. Export the modified data to the 'sample.csv' file.

### Example

Input:

```
EmployeeName,Role,Department,SalaryGrade
John Doe,Manager,CS,A1
Jane Smith,Developer,IT,B2
```

Output:

```
EmployeeName,Role,Department,SalaryGrade,Group
John Doe,Manager,CS,High,Technical
Jane Smith,Developer,IT,Medium,Non-Technical
NewName,PowerShell,Platform,Highest,Technical
```

### Notes

- Make sure to replace the 'sample.csv' file in the script with your actual CSV file name if it differs.
- This script assumes that the 'sample.csv' file exists in the same directory as the script.
- The script will overwrite the 'sample.csv' file with the modified data.

Download the script: [CSV_manipulation.ps1](./CSV_manipulation.ps1)