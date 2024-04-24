import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Stillwater!1009",
    "database": "Glazer"
}

def db_query(query, params=None, is_select=False):
    """
    Executes the given SQL query and returns the result.

    Parameters:
        query (str): The SQL query to execute.
        params (tuple): Optional parameters to pass with the query.
        is_select (bool): Indicates if the query is a SELECT query.

    Returns:
        result: The result of the query execution.
    """
    try:
        with mysql.connector.connect(**db_config) as mydb:
            with mydb.cursor() as cursor:
                cursor.execute(query, params)
                if is_select:
                    result = cursor.fetchall()
                else:
                    mydb.commit()
                    result = cursor.lastrowid
                return result
    except mysql.connector.Error as err:
        print("Error executing query:", err)
        return None



# get activity name based on activity id
def fetch_activity_name(activity_id):
    """
    Fetches the activity name from the activity table based on the given activity ID.
    Parameters:
        activity_id (int): The ID of the activity to fetch the name for.
    Returns:
        str: The name of the activity.
    """
    query = "SELECT act_name FROM Activities WHERE activity_id = %s"
    result = db_query(query, (activity_id,), is_select=True)
    if result:
        return result[0][0]  # Assuming the first column in the result set is the activity name
    else:
        return None

def fetch_activity_desc(activity_id):
    """
    Fetches the activity description from the activity table based on the given activity ID.
    Parameters:
        activity_id (int): The ID of the activity to fetch the description for.
    Returns:
        str: The description of the activity.
    """
    query = "SELECT act_desc FROM Activities WHERE activity_id = %s"
    result = db_query(query, (activity_id,), is_select=True)
    if result:
        return result[0][0]  # Assuming the first column in the result set is the activity name
    else:
        return None

# fetches activity extension
def fetch_activity_extend(activity_id):
    """
    Fetches the activity extension from the activity table based on the given activity ID.
    Parameters:
        activity_id (int): The ID of the activity to fetch the extension for.
    Returns:
        str: The extension of the activity.
    """
    query = "SELECT activity_extend FROM Activities WHERE activity_id = %s"
    result = db_query(query, (activity_id,), is_select=True)
    if result:
        return result[0][0]  # Assuming the first column in the result set is the activity name
    else:
        return None

def fetch_whats_learned(activity_id):
    """
    Fetches what is learned from the activity table based on the given activity ID.
    Parameters:
        activity_id (int): The ID of the activity to fetch the what is learned info for.
    Returns:
        str: The what is learned info of the activity.
    """
    query = "SELECT whats_learned FROM Activities WHERE activity_id = %s"
    result = db_query(query, (activity_id,), is_select=True)
    if result:
        return result[0][0]  # Assuming the first column in the result set is the activity name
    else:
        return None


# fetches exhibit name
def fetch_exhibit_name(exhibit_id):
    """
    Fetches exhibit name from the exhibit table based on the given exhibit ID.
    Parameters:
        exhibit_id (int): The ID of the exhibit to fetch the exhibit name for.
    Returns:
        str: The name of the exhibit.
    """
    query = "SELECT ex_name FROM Exhibits WHERE exhibit_id = %s"
    result = db_query(query, (exhibit_id,), is_select=True)
    if result:
        return result[0][0]
    else:
        return None

def fetch_exhibit_desc(exhibit_id):
    """
    Fetches exhibit description from the exhibit table based on the given exhibit ID.
    Parameters:
        exhibit_id (int): The ID of the exhibit to fetch the exhibit description for.
    Returns:
        str: The description of the exhibit.
    """
    query = "SELECT ex_desc FROM Exhibits WHERE exhibit_id = %s"
    result = db_query(query, (exhibit_id,), is_select=True)
    if result:
        return result[0][0]
    else:
        return None

# fetch play name
def fetch_play_name(play_id):
    """
    Fetches type of play from the play table based on the given play ID.
    Parameters:
        play_id (int): The ID of the play type to fetch the play name for.
    Returns:
        str: The type of play.
    """
    query = "SELECT play_type FROM Play WHERE play_id = %s"
    result = db_query(query, (play_id,), is_select=True)
    if result:
        return result[0][0]
    else:
        return None

# fetch play desc
def fetch_play_desc(play_id):
    """
    Fetches play description from the play table based on the given play ID.
    Parameters:
        play_id (int): The ID of the play type to fetch the play description for.
    Returns:
        str: The description of the play type.
    """
    query = "SELECT play_desc FROM Play WHERE play_id = %s"
    result = db_query(query, (play_id,), is_select=True)
    if result:
        return result[0][0]
    else:
        return None
playdesc = fetch_play_desc(4)
print(playdesc)