"""This python script is used to perform sql query on dremio."""
import os
import sys
from dremio_simple_query.connect import get_token, DremioConnection


def get_dremio_client() -> DremioConnection:
    # URL to Login Endpoint
    login_endpoint = "http://localhost:9047/apiv2/login"
    # Payload for Login
    payload = {
        "userName": os.getenv("DREMIO_USERNAME"),
        "password": os.getenv("DREMIO_PASSWORD"),
    }
    # Get token from API
    token = get_token(uri=login_endpoint, payload=payload)
    # URL Dremio Software Flight Endpoint
    arrow_endpoint = "grpc://localhost:32010"
    #  Establish Client
    return DremioConnection(token, arrow_endpoint)


def perform_dremio_query(conn: DremioConnection, sql_path: str):
    sql = open(sql_path).read()
    result = conn.query(sql, conn.client, conn.headers)
    return result


if __name__ == "__main__":
    conn = get_dremio_client()
    sqlfiles = os.listdir("sql")
    sqlfiles.sort()
    sql_index = int(sys.argv[1])
    perform_dremio_query(conn, f"sql/dremio/{sqlfiles[sql_index]}")
