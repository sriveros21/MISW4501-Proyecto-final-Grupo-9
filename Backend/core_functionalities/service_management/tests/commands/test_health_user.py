from src.commands.health_user import PingCommand

class TestPingCommand():
  
  def test_ping_micro_user(self):
    result=PingCommand().execute()
    assert result=="pong"
