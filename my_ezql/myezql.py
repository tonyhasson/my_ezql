"""This library was made by Tony Hasson , a 25 year old student of Computer Science.

I made this project because I noticed that I had to use to much SQL queries in Python
and that didn't seem right to me,so I wanted to make a library that will Mysql more
pythonic and easier to use(hence the name my_ezql).

Feel free to use this library freely and suggest any approvments that come to mind.

Different ways to contact me for any reason ( feel free =] )

linkedIn- https://www.linkedin.com/in/tony-hasson-a14402205/
GitHub- https://github.com/tonyhasson
Pypi- https://pypi.org/project/my-ezql/

Thanks for reading and I hope you enjoy the library!

"""

import mysql.connector
from mysql.connector import Error
import pandas as pd

"""A quick guide how to start using the library correctly:
   (0) Before you can use this library,you MUST have a Mysql server!



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




"""

"""
    How to use sql queries in my_ezql?
    ********************************
    You have two options,the first option is the same as before,enter a sql string into self.query,and send it to either
    self.execute_query/self.read_query depending on the operation.

    The second option(which is why I made the library in the first place) is to use Command function,
    scroll down to see a full guide on how to use it correctly.
"""


class ezql():

    def __init__(self):
        self.connection = None  # connection with the Mysql server
        self.query = None  # sql query
        self.host_name = None  # server host_name
        self.user_name = None  # user name in Mysql connection
        self.user_password = None  # user password in Mysql connection
        self.database_name = None  # database name in Mysql server
        self.table_name = None  # current table name that the user is addressing
        self.__arithmetic_sign = ['+', '-', '*', '/', '=', '<', '>', '!', '%', '^', '&', '|', '(', ')']
        self.__operator_names = ["AND", "OR"]

    """displaying data about Mysql server connection
    for example: print(sql_obj)                  """

    def __str__(self):
        return "host:%s\nname:%s\npassword:%s\ndatabase:%s\n" % (
            self.host_name, self.user_name, self.user_password, self.database_name)

    """creating server connection(with/wihtout database name)"""

    def create_server_connection(self, host_name, user_name, user_password, database_name=None):

        # self.connection = None
        try:

            # if already had a previous connection
            if self.connection != None:
                print("recreating connection..\n")

            # if user didn't enter any database name(maybe database doesn't exist yet)
            if database_name == None:
                self.connection = mysql.connector.connect(
                    host=host_name,
                    user=user_name,
                    passwd=user_password,
                )

                print("MySQL connection without database was successful\n")

            # if user didn't enter any database name(maybe database doesn't exist yet)
            else:
                self.connection = mysql.connector.connect(
                    host=host_name,
                    user=user_name,
                    passwd=user_password,
                    database=database_name
                )
                print("MySQL connection with database was successful\n")

            # saving server connection data inside ezql object
            self.__enter_conn_data(host_name, user_name, user_password, database_name)


        except Error as err:
            print(f"Error: '{err}'")

    """to use this function,one must create server connection first!"""
    """creating a new database with the desired database name and change the connection to this database
    for example:  sql_obj.create_database("ezql_db")    
    """

    def create_database(self, database_name):

        cursor = self.connection.cursor()
        try:
            query_type = "CREATE DATABASE """ + str(database_name) + ""
            cursor.execute(query_type)
            print("Database created successfully\n")

            """recreate connection with new database """
            self.create_server_connection(self.host_name, self.user_name, self.user_password, database_name)

        except Error as err:
            print(f"Error: '{err}'")

    """for feeding data to the table"""

    def execute_query(self, action=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(self.query)
            self.connection.commit()
            print("%s Query successful" % (action))
        except Error as err:
            print(f"Error: '{err}'")

    """for reading data from table"""



    def read_query(self, pandas=False, *col):

        cursor = self.connection.cursor()
        results = None
        try:
            cursor.execute(self.query)
            results = cursor.fetchall()

            # if the user decided that he wants the data in dataframe form
            if pandas == True:

                # if the user wanted to recieve data about all of the columns
                if col[0] == '*':

                    ##query for getting all the table cols in right order

                    q1="""SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE table_name = '""" + str(self.table_name) + """'
                    AND table_schema='""" + str(
                        self.database_name) + """'
                    ORDER BY ORDINAL_POSITION"""

                    # get all of the columns
                    cursor.execute(q1)
                    r1 = cursor.fetchall()
                    col = self.__clean_all_col(r1)

                # build the pandas dataframe using the col for getting the columns requested
                df = pd.DataFrame(results, columns=col)
                results = df

            return results
        except Error as err:
            print(f"Error: '{err}'")

    """modify tables functions:

    create_table-
    to create a table simply send the wanted table_name,send the column names with their data type as well,
    and there is a default ID that increments itself so no need to create one,but you need a diffrent one you can just
    send False to it.

    code example: sql_obj.create_table("new_table",name="str",age="int")  

    delete_table-
    to delete a table simply send the wanted table_name and that's it!

    code example: sql_obj.delete_table("new_table")


    clear_table-
    to delete a table simply send the wanted table_name and that's it!

    code example: sql_obj.clear_table("new_table")

    copy_table-
    to copy one table to the other you need to send the name of the table where you want to take data from,and
    a table where you want to send your data to,the default is to send all of data from the first table to the second,
    but you can change that and only copy the columns by choosing full_or_empty to be False.

    PS , if your "to_table" has different columns than "from_table" ,"to_table" will be deleted and created as a new copy of "from_table".

    code example: sql_obj.copy_table("from_table","to_table")

     """

    """create table inside database"""
    """auto creates an ID that is a primary key and auto increments"""

    def create_table(self, table_name, auto_id=True, **cols):
        self.__command("CREATE_TABLE", table_name, auto_id, **cols)

    """deletes selected table from database"""

    def delete_table(self, table_name):
        self.__command("DELETE_TABLE", table_name)

    """clears selected table without deleting it"""

    def clear_table(self, table_name):
        self.__command("CLEAR_TABLE", table_name)

    """copies  data from one table to the other"""
    """full_or_empty means that if it is True,copy all of the data,if False,copy only the columns"""

    def copy_table(self, table_data_from, table_data_to, full_or_empty=True):
        self.__command("copy_table", table_data_from, table_data_to, full_or_empty)


    """
    CRUD operations:
    
    In this summary of operations of CRUD functions I will introduce each argument and their meaning/how to use them.
    
    function details:
    
    (1)  select - 
             select lets you select data according to what columns you choose and which conditions.
             enter desired columns into *col and conditions into **conditions.

             code example: results=sql_obj.select("test_ezql","ALL_COL",where=True,pandas_df=True,name="(str)=idk")
             in this example you will select all of the columns where name is idk.

             code example:  results=sql_obj.select("test_ezql","name","age",pandas_df=True,where=True,age="(int)>=20",c1="AND",c2="(",city="(str)=yavne",c3="OR",gender="(str)!=girl",c4=")")
             in this long example you will select the name and the age where the age is bigger or greater than 80 and (city is yavne or gender is not a girl)

    (2)  insert -
            insert lets you insert data to desired columns.
            enter columns and values into **conditions.

            code example: sql_obj.insert("test_ezql",age="(int)82",name="(str)idk",city="(str)kfar saba")
            in this example , age=82,name=idk and city=kfar saba will be entered into test_ezql.
    
    
    (3)  update-
            update lets you update desired data through choosing their columns and matching with conditions.
            enter columns and values through conditions.
            **(WARNING! if you omit the where argument,the operation will update all of the table!)**

            code example: sql_obj.update("test_ezql",where=True,city="(str)=rehovot",where_cond="where_cond",idnew_table="(int)=11")
            in this example, you will update city to rehovot where idnew_table is 11,the where_cond separates between the value we want to
            update to the condition. 
            
    (4)  delete-
            delete will delete the row wherever he found a matching value,
            insert columns and values through conditions.
            **(WARNING! if you omit the where argument,the operation will delete all of the rows in the table!)**

            code example: sql_obj.delete("test_ezql",where=True,name="(str)=idk")
            in this example,you will delete every row where the name is idk.
    
    
    More information about those functions arguments:
    
    (1)   table_name-
            the table_name you want to get/insert data to.
            it is important that the table already exists in that database or else the operations won't succeed.
    
    (2)   *col-
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
    """


    def select(self, table_name, *col, pandas_df=False, where=False, **conditions):
        return self.__command("select",table_name,*col,pandas_df=pandas_df,where=where,**conditions)


    def insert(self,table_name,**conditions):
        self.__command("insert",table_name,**conditions)


    def update(self,table_name,where=True,**conditions):
        self.__command("update",table_name,where=where,**conditions)


    def delete(self,table_name,where=True,**conditions):
        self.__command("delete", table_name, where=where, **conditions)




    """private inner class helper functions:"""


    """many of the other functions are sent to be implemented in this function"""
    def __command(self, type_query, table_name, *col, pandas_df=False, where=False, **conditions):

        # change type query to uppercase(SQL is case sensitive)
        type_query = type_query.upper()
        ##save table name inside object
        self.table_name = table_name

        # if chosen type to be SELECT
        if type_query == "SELECT":

            ##build the string query
            query = str(type_query)
            query += " "

            # if ALL_COL or * are inside col,then switch all of col to '*'

            if ("ALL_COL" or '*') in col:
                col = "*"

            # enter columns

            for i in range(len(col)):
                query += str(col[i])
                if i < len(col) - 1:
                    query += ","
                else:
                    query += " FROM "
            query += str(self.database_name)
            query += "."
            query += str(table_name)

            # if chosen SELECT without WHERE
            if where == False:
                query += ";"
                self.query = query


            # if chosen SELECT with WHERE
            else:
                query += " WHERE "
                for column, value in conditions.items():

                    # if column doesn't start with 'c' and value is not an operator condition(AND,OR,etc..) or arithmetic sign
                    if str(column)[0] != 'c' or (str(value).upper() not in self.__operator_names and str(
                            value).upper() not in self.__arithmetic_sign):
                        query += str(column)
                        value_cleaned, sign = self.__get_type(value)
                        query += str(sign)  ##add arithmetic sign (=,<,>)

                        query += str(value_cleaned)

                    # if column starts with 'c' and value is an operator condition(AND,OR,etc..)
                    else:
                        query += " "
                        query += str(value)
                        query += " "

                query += ";"
                self.query = query

            return self.read_query(pandas_df, *col)


        # if chosen type to be INSERT
        elif type_query == "INSERT":

            ##build the string query

            query = str(type_query)
            query += " "
            query += "INTO "
            query += str(self.database_name)
            query += "."
            query += str(table_name)
            query += "("

            # if ALL_COL or * are inside col,then switch all of col to '*'

            if ("ALL_COL" or '*') in col:
                col = "*"

            # enter columns

            ##if entering columns and values from condition
            if len(col) == 0:
                i = 0
                for column, value in conditions.items():

                    query += str(column)
                    if i < len(conditions) - 1:
                        query += ","
                    else:
                        query += ")"
                    i += 1


            ##fixme- need sure if I need entering columns through col and values from condition since changed command function
            ##if entering columns through col and values from condition
            else:

                for i in range(len(col)):

                    query += str(col[i])
                    if i < len(col) - 1:
                        query += ","
                    else:
                        query += ")"

            query += " VALUES ("

            i = 0
            # enter values into the string query
            for column, value in conditions.items():

                value_cleaned, sign = self.__get_type(value)  ##sign not necessary here
                query += str(value_cleaned)
                if i < len(conditions) - 1:
                    query += ","
                i += 1

            query += ");"
            self.query = query
            self.execute_query(type_query)

        ##if chosen update
        elif type_query == "UPDATE":

            ##build the string query
            query = str(type_query)
            query += " "
            query += str(self.database_name)
            query += "."
            query += str(table_name)
            query += " SET "

            ##enter columns:

            pos_of_where_cond = 0

            ##if entering columns and values from condition
            if len(col) == 0:
                i = 0
                for column, value in conditions.items():
                    if "where_cond" == column or "where_cond" == value:
                        pos_of_where_cond = i + 1
                        break

                    if i >= 1:
                        query += ","
                    query += str(column)
                    query += " "
                    value_cleaned, sign = self.__get_type(value)  ##no use for sign here
                    query += str(sign)  ##adds = sign
                    query += str(value_cleaned)

                    i += 1



            ##fixme: (not sure if need this)
            # if entering columns from col and values from condition
            else:
                for i in range(len(col)):

                    query += str(col[i])
                    if i < len(col) - 1:
                        query += ","

            ##if chosen UPDATE without WHERE
            if where == False:
                query += ";"
                self.query = query
                self.execute_query(type_query)

            # if chosen UPDATE with WHERE
            else:
                query += " WHERE "

                for column, value in conditions.items():

                    ##skip over the columns until arriving to where_cond
                    if pos_of_where_cond > 0:
                        pos_of_where_cond -= 1
                        continue

                    """if column doesn't start with 'c' and value is not an operator condition(AND,OR,etc..) or arithmetic sign"""
                    if str(column)[0] != 'c' or (str(value).upper() not in self.__operator_names and str(
                            value).upper() not in self.__arithmetic_sign):
                        query += str(column)
                        value_cleaned, sign = self.__get_type(value)
                        query += str(sign)  ##add arithmetic sign (=,<,>)

                        query += str(value_cleaned)

                        """if column starts with 'c' and value is an operator condition(AND,OR,etc..)"""
                    else:
                        query += " "
                        query += str(value)
                        query += " "

                query += ";"
                self.query = query
                self.execute_query(type_query)



        ##if chosen delete
        elif type_query == "DELETE":

            ##build the string query
            query = str(type_query)
            query += " FROM "
            query += str(self.database_name)
            query += "."
            query += str(table_name)

            ##if chosen DELETE without WHERE then delete all of the rows in the table
            if where == False:
                query += ";"
                self.query = query
                self.execute_query(type_query)

            # if chosen DELETE with WHERE
            else:
                query += " WHERE "
                for column, value in conditions.items():

                    """if column doesn't start with 'c' and value is not an operator condition(AND,OR,etc..) or arithmetic sign"""
                    if str(column)[0] != 'c' or (str(value).upper() not in self.__operator_names and str(
                            value).upper() not in self.__arithmetic_sign):
                        query += str(column)
                        value_cleaned, sign = self.__get_type(value)
                        query += str(sign)  ##add arithmetic sign (=,<,>)

                        query += str(value_cleaned)

                        """if column starts with 'c' and value is an operator condition(AND,OR,etc..)"""
                    else:
                        query += " "
                        query += str(value)
                        query += " "

                query += ";"
                self.query = query
                self.execute_query(type_query)

        ##if chosen create table
        elif type_query == "CREATE_TABLE":

            ##build query string

            query = "CREATE TABLE "
            query += table_name
            query += "("
            ##if auto id is enabled
            if col[0] == True:
                query += """ ID INT NOT NULL AUTO_INCREMENT,
                PRIMARY KEY (ID)"""

            ##if user entered columns
            if len(conditions) > 0:
                query += ","
                ##insert columns and data types into the query
                i = 0
                for column, value in conditions.items():
                    query += str(column)
                    query += " "
                    if value == "str":
                        query += "varchar(255)"
                    else:
                        query += value
                    if i < len(conditions) - 1:
                        query += ","
                    else:
                        query += ");"
                    i += 1

            ##if user entered an empty table
            else:
                query += ");"

            self.query = query
            self.execute_query(type_query)


        ##if chosen delete table
        elif type_query == "DELETE_TABLE":
            query = "DROP TABLE "
            query += str(table_name)
            query += ";"
            self.query = query
            self.execute_query(type_query)

        ##if chosen clear table
        elif type_query == "CLEAR_TABLE":
            query = "TRUNCATE TABLE "
            query += str(table_name)
            query += ";"
            self.query = query
            self.execute_query(type_query)


        ##if chosen copy table
        elif type_query == "COPY_TABLE":

            ##checking if the table exists
            tf = self.__table_exists(str(col[0]))
            ##if the table exists,delete it so you can recreate it with matching columns
            if tf == True:
                ##need to keep table name because it changes when i summon delete_table
                tmp_table_name = self.table_name
                self.delete_table(str(col[0]))
                self.table_name = tmp_table_name

            query = ""
            ##copying all the data from one table to the other
            if col[1] == True:
                query += """CREATE TABLE """ + str(self.database_name) + """.""" + str(col[0]) + """
                AS  
                SELECT *
                FROM """ + str(self.database_name) + """.""" + str(self.table_name) + """;"""


            ##copying only the columns
            else:

                query += """CREATE TABLE """ + str(self.database_name) + """.""" + str(col[0]) + """ LIKE """ + str(
                    self.database_name) + """.""" + str(self.table_name) + """;"""

            self.query = query
            self.execute_query(type_query)



        else:
            print("\nUnknown Type Query\n")



    """entering data about Mysql server connection (inner class function)"""

    def __enter_conn_data(self, host_name=None, user_name=None, user_password=None, database_name=None):
        self.host_name = host_name  # server host_name
        self.user_name = user_name  # user name in Mysql connection
        self.user_password = user_password  # user password in Mysql connection
        self.database_name = database_name  # database name in Mysql server

    """checks if the table_name exists in the database"""

    def __table_exists(self, table_name):

        query = """SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = '""" + str(
            self.database_name) + """') AND (TABLE_NAME = '""" + str(table_name) + """')"""

        self.query = str(query)
        r1 = self.read_query()
        if r1[0][0] == 0:
            return False
        else:
            return True

    """used for making the columns more readable, if you choose the option of viewing the data of all the columns in the table """

    def __clean_all_col(self, results):
        arr = []
        for result in results:
            arr.append(list(result)[0])
        return arr

    """find type of value in WHERE condition"""

    def __get_type(self, value):

        type = ""
        sign = ""
        i = 0

        ##building the type of the variable
        while value[i] != ")":
            if value[i] != "(":
                type += str(value[i])
            i += 1

        i += 1

        ##building the arithmetic type of the operation
        while value[i] in self.__arithmetic_sign:
            sign += str(value[i])
            i += 1

        if type == "str":
            type = '"'
            type += value[i:len(value)]
            type += '"'
        elif type == "int":
            type = value[i:len(value)]

        return type, sign





