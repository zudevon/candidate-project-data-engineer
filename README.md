# Solution
##### By Devon Rasch
##### Date: 12/14/2022

***

## Creating a Data source
I will start by placing the excel file into an s3 location but this process would be excellent if it had this data already stored in Athena so that other tables can be queried from it. 
o have this data already stored in Athena so that other tables can be queried from it with out the hassle of creating a lot of tables from the initial data retrieval. 

### Step 1 (Glue Script)
Create a python glue script to get data from the source and place data in parquet files in S3 reflecting the tables that will be assigned from this original table.

### Step 2 (Athena DDLs)
Make all of the DDLs for Athena to pick up the parquet files in s3 locations.

### Step 3 (Create Setup tools)
An egg for libraries will have to be used in this process because the libraries needed will not be accessible for us in Glue. Because of this, there will have to be an egg/wheel file with the needed packages so that glue will have the correct python packages it needs to run the script. 

### Step 4 (IAM Roles)
First create a policy for glue and for glue to access s3. After create a role that uses this policy.

### Step 5 (Glue Job)
Here I will paste in the script, assign the egg with the needed libraries that I created with the setup tools and placed in s3. Save the job and then run the job to make sure that it succeeds. Next I will create a trigger that runs on a cron schudule in the triggers tab within the Glue console.

Now that data will extract on a daily/hourly basis, the tables with all of the data is now located and accessible for other teams in Athena. 

## Other Databases?
When using the Glue process, we can put the data anywhere. Glue has the capability to connect to Redshift, RDS, and many other databases that maybe need data extracted from. 

## IaC

Starting with my aws passwords that are located in my class “boto4” that is a small wrapper for boto3. We can store these passwords in s3, and retrieve these keys by accessing s3 only from glue. There are also so many password managers out there that can also hold most of the config files needed. There isn’t much configuration around this build but if we could dive deeper 
