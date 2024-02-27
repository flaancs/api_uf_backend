def test_set_value(mock_redis, mocker):
    mock_redis._client.set.return_value = True
    result = mock_redis.set_value("test_key", "test_value")
    mock_redis._client.set.assert_called_once_with("test_key", "test_value")
    assert result is True

def test_get_value(mock_redis, mocker):
    mock_redis._client.get.return_value = "test_value"
    value = mock_redis.get_value("test_key")
    mock_redis._client.get.assert_called_once_with("test_key")
    assert value == "test_value"
