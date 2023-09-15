from project.models import User


# https://martinfowler.com/bliki/GivenWhenThen.html
def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, role fields are defined correctly
    """
    user = User(email='testuser@gmail.com',
                name='doom',
                password='password',
                weight_value=190,
                weight_unit='lb',
                height_value=185,
                height_unit='cm',
                membership_status='basic'
                )
    assert user.email == 'testuser@gmail.com'
    assert user.membership_status == 'basic'
    assert user.weight_unit == 'lb'
    assert user.weight_value == 190
    assert user.height_unit == 'cm'
    assert user.height_value == 185
    assert user.password == 'password'
    assert user.name == 'doom'




