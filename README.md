#JSON To SQL INSERT

### JSON Structure

Name of the JSON needs to be the name of the table you want to insert data into, CUSTOMERS.json etc.

[ {},{},{} ] Each object within being a customer row to insert.

Each key in the object must be the exact name of each field in the table.

### Run File
When the file is ran, it will ask for an input of the file you wish to convert. 
Enter the path to the file using forward slashes. C:/Users/..../Customers.json or local path ./Customers.json

### Output File
It will output a complete SQL file with all rows given title "INSERT-Customer.sql"