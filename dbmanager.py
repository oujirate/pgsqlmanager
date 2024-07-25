import psycopg2 as pg
from psycopg2 import OperationalError

class dbmanager:
    def __init__(self,host,port,username,password,dbname):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.dbname = dbname
        self.conn = None
        self.cur = None
    
    def connect(self):
        try:
            connection_string = f"""host='{self.host}' port={self.port} user='{self.username}' 
            password='{self.password}' dbname='{self.dbname}'"""
            self.conn = pg.connect(connection_string)
            self.cur = self.conn.cursor()

        except OperationalError as ex:
            print(f"Connection Failed! Error: {ex}")
    
    def close(self):
        if self.conn is not None and self.cur is not None:
            try:
                self.cur.close()
                self.conn.close()
            except OperationalError as ex:
                print(f"Close Failed! Error: {ex}")
        else:
            print("Message: Connection Not Found!")

    def version_pgsql(self):
        try:
            self.connect()
            self.cur.execute("SELECT version();")
            version = self.cur.fetchone()
            print(f"PostgreSQL Version: {version[0]}")

        except OperationalError as ex:
            print(f"Error: {ex}")

        finally:
            self.close()
    
    def get_columnname(self,table,idenable=False):
        try:
            self.connect()
            column_data = []
            query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}' ORDER BY ordinal_position"
            self.cur.execute(query)
            column = self.cur.fetchall()
            if idenable == 1:
                for i in column:
                    column_data.extend(i)
            else:
                for i in column[1:]:
                    column_data.extend(i)
            return column_data
        
        except OperationalError as ex:
            print(f"Error: {ex}")

        finally:
            self.close()

    def getall_tablename(self):
        try:
            self.connect()
            table_name = []
            query = f"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name"
            self.cur.execute(query)
            table = self.cur.fetchall()
            for i in table:
                table_name.extend(i)
            return table_name
        
        except OperationalError as ex:
            print(f"Error: {ex}")

        finally:
            self.close()
    
    def auth_columntable(self,table,column):
        try:
            columns = self.get_columnname(table=table,idenable=True)
            for i in columns:
                if i == column.strip():
                    return True
            return False
        
        except Exception as ex:
            print(f"Error: {ex}")
    
    def create_data(self,table,values):
        try:
            column = self.get_columnname(table=table)
            self.connect()
            query = f"INSERT INTO {table} ({','.join(column)}) VALUES ({','.join(['%s'] * len(values))})"
            self.cur.execute(query,values)
            self.conn.commit()

        except OperationalError as ex:
            print(f"Error: {ex}")

        finally:
            self.close()

    def read_data(self,select='*',table="",join="",where="",groupby="",orderby=""):
        query = f"SELECT"
        count = 0
        switch_join = False
        fragment = ""
        try:
            self.connect()
            if table.strip() in self.getall_tablename():
                select_list = select.strip().split(",")
                tables_data = (join or "").strip().split(",")
                tables_data.append(table)
                
                if join:
                    for i in select_list:
                        for j in tables_data:
                            column = self.get_columnname(table=j,idenable=True)
                            if i in column:
                                fragment = f" {j}.{i}"
                                query += fragment
                                count += 1
                                query += "," if count < (len(select_list)) else ""
                                continue

                    fragment = f" FROM {table}"
                    query += fragment

                    for i in tables_data:
                        column_pk = self.get_columnname(table=i,idenable=True)
                        for j in tables_data:
                            column_fk = self.get_columnname(table=j,idenable=True)
                            for k in column_fk:
                                if column_pk[0] == k and j != i: 
                                    fragment = f" JOIN {i} ON {i}.{column_pk[0]} = {j}.{k}"
                                    query += fragment

                    switch_join = True

                else:
                    fragment = f"{" *" if select == '*' else select.strip()} FROM {table}"
                    query += fragment
            
                if where:
                    if join:
                        raise Exception("The use of WHERE cannot be used with JOIN!")
                    else:
                        fragment = f" WHERE %s"
                        query += fragment

                if orderby:
                    if join:
                        raise Exception("The use of ORDER BY cannot be used with JOIN!")
                        
                    else:
                        fragment = f" ORDER BY {orderby.strip()}"
                        query += fragment

                self.cur.execute(query)
                result = self.cur.fetchall()
                print(result)
                exit()

            else:
                raise Exception("Tabel is None")
            
        except Exception as ex:
            print(f"Error: {ex}")
        finally:
            self.close()
            
    def update_data(self,table,idcolumn,values):
        try:
            count = 0
            query = f"UPDATE {table} SET"
            column = self.get_columnname(table=table,idenable=True)
            self.connect()
            for i in column[1:]:
                fragment = f" {i} = %s"
                query += fragment
                count += 1
                if count < len(values):
                    query += f","
            fragment = f" WHERE {column[0]} = {idcolumn}"
            query += fragment
            self.cur.execute(query,values)
            self.conn.commit()

        except Exception as ex:
            print(f"Error: {ex}")

        finally:
            self.close()

    def delete_data(self,table,id_column):
        try:
            self.connect()
            columnanme_pk = self.get_columnname(table=table,idenable=1)
            query = f"DELETE FROM {table} WHERE {id_column} = {columnanme_pk[0]}"
            self.cur.execute(query)
            self.conn.commit()

        except Exception as ex:
            print(f"Error: {ex}")

        finally:
            self.close()
