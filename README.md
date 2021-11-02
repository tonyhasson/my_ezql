# my_ezql
 A library for python made by me,to make the use of MySQL easier and more pythonic


This library was made by Tony Hasson , a 25 year old student of Computer Science.

I made this project because I noticed that I had to use too much SQL queries in Python
and that didn't seem right to me,so I wanted to make a library that will make MySQL more
pythonic and easier to use(hence the name my_ezql).

Feel free to use this library freely and suggest any approvments that come to mind.

Different ways to contact me for any reason ( feel free =] )

linkedIn- https://www.linkedin.com/in/tony-hasson-a14402205/

GitHub- https://github.com/tonyhasson

Pypi- https://pypi.org/project/my-ezql/

Thanks for reading and I hope you enjoy the library!


********************************

#setup guide

installation:
 
    pip install my_ezql
import
    
    from my_ezql import ezql

A quick guide how to start using the library correctly:

   (0) Before you can use this library,you *MUST* have a Mysql server!
   
   
   
   (1) First of all,create a ezql object,this object will contain your database,tables,etc..
   
    for example- ezql_obj=ezql()
    
            
   (2) Once you've created your ezql object,you need to create a connection with your Mysql server and database
   ( if you don't have a database yet,skip to (2.1)+(2.2) ).
            
    for example- sql_obj.create_server_connection("host_name","user_name","password","database_name")
    
    host_name- usually 127.0.0.1 
    user_name and password- the user name and password for your Mysql server.
    database_name- your database name. (duh)
                     
        
    
   (2.1) In case you didn't create a database yet,first of all create a connection with your Mysql server.
          
    for example- sql_obj.create_server_connection("host_name","user_name","password")
       
    host_name- usually 127.0.0.1 
    user_name and password- the user name and password for your Mysql server.
          
          
   (2.2) Now we will create a database in your server,once you create the database,it will automatically restart your connection
        with the server and with your newly created default database.
        
    for example- sql_obj.create_database("database_name")
    
    database_name- your database name. (duh)
    
    
    
   (3) And that's it! you're ready to use the library.
   
   
   
   
********************************   
 #How to use sql queries in my_ezql?

    You have two options,the first option is the same as before,enter a sql string into self.query,and send it to either
    self.execute_query/self.read_query depending on the operation.
    
    The second option(which is why I made the library in the first place) is to use the Crud operations,
    scroll down to see a full guide on how to use it correctly.
   




********************************
   #CRUD operations:
    
   In this summary of operations of CRUD functions I will introduce each argument and their meaning/how to use them.
    
   ##function details:
    
   (1)  select
    
             select lets you select data according to what columns you choose and which conditions.
             enter desired columns into *col and conditions into **conditions.

             code example: results=sql_obj.select("test_ezql","ALL_COL",where=True,pandas_df=True,name="(str)=idk")
             in this example you will select all of the columns where name is idk.

             code example:  results=sql_obj.select("test_ezql","name","age",pandas_df=True,where=True,age="(int)>=20",c1="AND",c2="(",city="(str)=yavne",c3="OR",gender="(str)!=girl",c4=")")
             in this long example you will select the name and the age where the age is bigger or greater than 80 and (city is yavne or gender is not a girl)

   (2)  insert 
    
            insert lets you insert data to desired columns.
            enter columns and values into **conditions.

            code example: sql_obj.insert("test_ezql",age="(int)82",name="(str)idk",city="(str)kfar saba")
            in this example , age=82,name=idk and city=kfar saba will be entered into test_ezql.
    
    
   (3)  update
    
            update lets you update desired data through choosing their columns and matching with conditions.
            enter columns and values through conditions.
            **(WARNING! if you omit the where argument,the operation will update all of the table!)**

            code example: sql_obj.update("test_ezql",where=True,city="(str)=rehovot",where_cond="where_cond",idnew_table="(int)=11")
            in this example, you will update city to rehovot where idnew_table is 11,the where_cond separates between the value we want to
            update to the condition. 
            
   (4)  delete
    
            delete will delete the row wherever he found a matching value,
            insert columns and values through conditions.
            **(WARNING! if you omit the where argument,the operation will delete all of the rows in the table!)**

            code example: sql_obj.delete("test_ezql",where=True,name="(str)=idk")
            in this example,you will delete every row where the name is idk.
    
    
   ####More information about those functions arguments:
    
    
   (1) table_name
   
            the table_name you want to get/insert data to.
            it is important that the table already exists in that database or else the operations won't succeed.
    
   (2)   *col
   
            a python *args object that will contain all of the desired columns.
            *col is used in only in select function.
            (you can enter '*' or "ALL_COL" if you want to view the data about all of the columns)


   (3)   pandas_df-
            
            boolean, option to return the result as a pandas dataframe.
            this option is defaulted to False,so to activate it simply send True.
            pandas_df is used in only in select function.


   (4)   where- 
            
            boolean, lets you use where statement.
            this option is defaulted to False in select,and True in update and delete.
            used in type_query:select,update and delete.
            (see warning about update and delete in function details (3) and (4))


   (5)   **conditions-
           
            a python **kwargs object,designed as shown below:
          
            **(it is IMPORTANT to note that conditions usage varies between different function types)**
          
            in select:
          
                  {col/condition_number="(data type)(combination of arithmetic signs)desired value"} 
    
                  for example :  city="(str)=yavne",   age="(int)<20"
    
                  if you want to use AND/OR you can write them as one of the objects
                  inside condition with the letter c and a number,and in the value enter AND/OR.
    
                  for example :  c1="AND"
    
                  you can add parenthesis '(' OR ')' the same way you did for AND/OR to make more complex queries.
              
          
            in insert:
          
                  {col="(data type)desired value"}
                  for example : age="(int)82" ,   city="(str)kfar saba"
            
          
            in update:
          
                  {col="(data type)(combination of arithmetic signs)desired value"} OR {where_cond="where_cond"}
                
                  for example : city="(str)=rehovot",   where_cond="where_cond",    idnew_table="(int)=11"
                
                  where_cond="where_cond" means that whatever is written afterwards is part of the where condition.
          
            in delete:                        
                  {col="(data type)(=)desired value"}
            
                  for example : name="(str)=idk"   ,   idnew_table="(int)=11"  
********************************
  #modify tables functions:
    
   (1)create_table
   
    to create a table simply send the wanted table_name,send the column names with their data type as well,
    and there is a default ID that increments itself so no need to create one,but you need a diffrent one you can just
    send False to it.
        
    code example: sql_obj.create_table("new_table",name="str",age="int")  
     
   (2)delete_table
   
    to delete a table simply send the wanted table_name and that's it!
    
    code example: sql_obj.delete_table("new_table")
     
     
   (3)clear_table
   
    to delete a table simply send the wanted table_name and that's it!
    
    code example: sql_obj.clear_table("new_table")
     
   (4)copy_table
   
    to copy one table to the other you need to send the name of the table where you want to take data from,and
    a table where you want to send your data to,the default is to send all of data from the first table to the second,
    but you can change that and only copy the columns by choosing full_or_empty to be False.
    
    PS , if your "to_table" has different columns than "from_table" ,"to_table" will be deleted and created as a new copy of "from_table".
    
    code example: sql_obj.copy_table("from_table","to_table")

