from datetime import date

from python_graphql_client import GraphqlClient


def get_client(token: str) -> GraphqlClient:
  headers = {
    "Authorization": f"Bearer {token}"
  }
  return GraphqlClient(endpoint="https://api.github.com/graphql", headers=headers)


def handler(pd: "pipedream"):
  token = f"{pd.inputs['github']['$auth']['oauth_access_token']}"
  client = get_client(token)
  query = """
    query($username: String!, $date: DateTime) {
      user(login: $username) {
        contributionsCollection(from: $date, to: $date) {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                contributionCount
                weekday
                date
              }
            }
          }
        }
      }
    }
  """
  variables = {
    "username": "attakei",
    "date": date.today().strftime("%Y-%m-%dT00:00:00"),
  }
  result = client.execute(query=query, variables=variables)
  print(result["data"])
  return {
    "date": date.today().strftime("%Y-%m-%d"),
    "contributions": result["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"][0]["contributionDays"][0]["contributionCount"]
  }
