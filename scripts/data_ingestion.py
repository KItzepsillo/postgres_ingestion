import psycopg2
import faker

connection = psycopg2.connect(
    host="localhost", database="demo", user="postgres", password="123"
)

cursor = connection.cursor()

cursor.execute("SELECT version()")

record = cursor.fetchone()

def check_create_table(table_name: str):
    """
    check_create_table
    """

    create_table_query = """
      CREATE TABLE IF NOT EXISTS person(
        ID      SERIAL PRIMARY KEY,
        NAME    TEXT NOT NULL,
        ADDRESS TEXT NOT NULL
      );
    """

    cursor.execute(create_table_query)
    connection.commit()

def ingestion_table(table: str, name: str, address: str):
    """
    ingestion_table

    Parameters:
    table (str): Name of table
    name (str): Nombre de la persona
    address (str): Direccion de la persona
    """

    insert_sql = f"INSERT INTO {table} (NAME, ADDRESS) VALUES ('{name}','{address}')"

    cursor.execute(insert_sql)
    connection.commit()
    print('ok')


table_name = "person"
check_create_table(table_name)

fake = faker.Faker()

for person in range(0,100):
    name, address = fake.name(), fake.address()
    ingestion_table(table_name, name, address)

