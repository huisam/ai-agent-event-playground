from ai_agent_event_playground.main import main


def test_main_prints_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from ai-agent-event-playground!\n"
