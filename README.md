# my_ezql
 A library for python made by me,to make the use of MySQL easier and more pythonic


This library was made by Tony Hasson , a 25 year old student of Computer Science.

I made this project because I noticed that I had to use to much SQL queries in Python
and that didn't seem right to me,so I wanted to make a library that will Mysql more
pythonic and easier to use(hence the name my_ezql).

Feel free to use this library freely and suggest any approvments that come to mind.

Different ways to contact me for any reason ( feel free =] )

linkedIn- https://www.linkedin.com/in/tony-hasson-a14402205/

GitHub- https://github.com/tonyhasson

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
    
    The second option(which is why I made the library in the first place) is to use Command function,
    scroll down to see a full guide on how to use it correctly.
   
  
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
********************************
  #operations in command:  
    
   In this summary of operations of command function I will introduce each argument and their meaning/how to use them.
    
   (1) type query- type of sql command:
     
         (1.1) SELECT- select lets you select data according to what columns you choose and which conditions.
                       enter desired columns into col and conditions into conditions.
         
             code example: results=sql_obj.command("select","test_ezql","ALL_COL",where=True,pandas_df=True,name="(str)=idk")
             in this example you will select all of the columns where name is idk.
             
             code example:  results=sql_obj.command("select","test_ezql","name","age",pandas_df=True,where=True,age="(int)>=20",c1="AND",c2="(",city="(str)=yavne",c3="OR",gender="(str)!=girl",c4=")")
             in this long example you will select the name and the age where the age is bigger or greater than 80 and (city is yavne or gender is not a girl)
         
         
         
         (1.2) INSERT- insert lets you insert data to desired columns  
         enter desired columns into col and conditions into conditions,
         or you can insert the columns and values from conditions and leave col empty.
            
            code example: sql_obj.command("insert","new_table1","name","age","city","gender",c1="(str)john",c2="(int)25",c3="(str)new york",c4="(str)boy")
            in this example, I wrote the columns in col and sent them matching value through conditions(it's important to name them c and then a number).
                  
            code example: sql_obj.command("insert","test_ezql",age="(int)82",name="(str)idk",city="(str)kfar saba")
            in this example , age=82,name=idk and city=kfar saba will be entered into test_ezql,here I left col empty and used only conditions.
    
    
    
         (1.3) UPDATE-update lets you update desired data through choosing their columns and matching with conditions.
                      right now updates only works from entering columns and values through conditions.
                      **(WARNING! if you omit the where argument,the operation will update all of the table!)**
            
            code example: sql_obj.command("update","test_ezql",where=True,city="(str)=rehovot",where_cond="where_cond",idnew_table="(int)=11")
            in this example, you will update city to rehovot where idnew_table is 11,the where_cond separates between the value we want to
            update to the condition. 
            
            
            
         (1.4) DELETE-delete will delete the row wherever he found a matching value,
                      insert columns and values through conditions.
                      **(WARNING! if you omit the where argument,the operation will delete all of the rows in the table!)**
            
              code example: sql_obj.command("delete","test_ezql",where=True,name="(str)=idk")
              in this example,you will delete every row where the name is idk.
                      
 
   (2) table_name
                    
    the table_name you want to get/insert data to.
    it is important that the table already exists in that database or else the operations won't succeed.
                    
   (3) *col
    
    a python *args object that will contain all of the desired columns.
    *col is used in SELECT,can be used in INSERT,but is not used in UPDATE and DELETE.
    (you can enter '*' or "ALL_COL" if you want to view the data about all of the columns)
     
     
   (4) pandas
        
    boolean, option to return the result as a pandas dataframe.
    this option is defaulted to False,so to activate it simply send True.
                
                   
   (5) where
    
    boolean, lets you use where statement.
    this option is defaulted to False,so to activate it simply send True.
    used in type_query:select,update and delete.
    (see warning about update and delete in numbers (1.3) and (1.4))
     
     
   (6) **conditions
   
    a python **kwargs object,designed as shown below:
    
      {col/condition_number:"(data type)(combination of arithmetic signs)desired value"} 
      
      for example :  city="(str)=yavne",age="(int)<20"
      
      if you want to use AND/OR you can write them as one of the objects
      inside condition with the letter c and a number,and in the value enter AND/OR.
      
      for example :  c1="AND"
      
      you can add parenthesis '(' OR ')' the same way you did for AND/OR to make more complex queries.
                       
      (it is IMPORTANT to note that conditions usage varies between different type queries)