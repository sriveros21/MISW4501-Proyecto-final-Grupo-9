from ..queries.base_queries import BaseQueries

class PingCommand(BaseQueries):
  def execute(self):
    return "pong"
