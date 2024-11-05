#
# Retrieves and returns all movies in the 
# MovieLens database running in AWS.
#

import json
import boto3
import os
import datatier

from configparser import ConfigParser

def serialize_datetime(obj):
  return obj.isoformat()

def lambda_handler(event, context):
  try:
    print("**call to lambda movies**")
    
    #
    # setup AWS based on config file:
    #
    config_file = 'movielens-config.ini'
    os.environ['AWS_SHARED_CREDENTIALS_FILE'] = config_file
    
    configur = ConfigParser()
    configur.read(config_file)
    
    #
    # configure for RDS access
    #
    rds_endpoint = configur.get('rds', 'endpoint')
    rds_portnum = int(configur.get('rds', 'port_number'))
    rds_username = configur.get('rds', 'user_name')
    rds_pwd = configur.get('rds', 'user_pwd')
    rds_dbname = configur.get('rds', 'db_name')

    #
    # open connection to the database:
    #
    print("**opening connection**")
    
    dbConn = datatier.get_dbConn(rds_endpoint, rds_portnum, rds_username, rds_pwd, rds_dbname)
    
    #
    # now retrieve all the movies:
    #
    print("**retrieving data**")

    rows = []
    
    #
    # TODO:
    #
    # sql = ???
    #
    # rows = datatier.???
    #
    # N = len(rows)
    #
    # print("retrieved", N, "movies")
    # 
    # print("first movie:", rows[0])
    # print("last movie:", rows[N-1])
    #

    #
    # respond in an HTTP-like way, i.e. with a status
    # code and body in JSON format:
    #
    print("**done, returning rows**")
    
    return {
      'statusCode': 200,
      'body': json.dumps(rows, default=serialize_datetime)
    }
    
  except Exception as err:
    print("**ERROR**")
    print(str(err))
    
    return {
      'statusCode': 500,
      'body': json.dumps(str(err))
    }
