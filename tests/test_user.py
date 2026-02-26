from models.user import User

def test_user_creation():
    user = User("Alex", "alex@email.com")
    assert user.name == "Alex"
    assert user.email == "alex@email.com"
    assert user.projects == []