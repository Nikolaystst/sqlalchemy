from models import User, Order
from main import Session

# with Session() as session:
    # new_user = User(username='jiki', email='jiki@abv.bg')
    # session.add(new_user)
    # session.commit()

    # users = session.query(User).all()
    # for user in users:
    #     print(f"{user.username}, {user.email}")

    # user_for_update = session.query(User).filter_by(username='jiki').first()
    #
    # if user_for_update:
    #     user_for_update.email = "kiki@abv.bg"
    #     session.commit()
    #     print('User updated successfully')
    # else:
    #     print('User not found')

    # user_for_delete = session.query(User).filter_by(username='jiki').first()
    # if user_for_delete:
    #     session.delete(user_for_delete)
    #     session.commit()
    #     print('User deleted successfully')
    # else:
    #     print('User not found')

    # new_user = User(username='john', email='john@abv.bg')
    # new_user2 = User(username='sarah', email='sarah@abv.bg')
    # new_user3 = User(username='mike', email='mike@abv.bg')
    # new_user4 = User(username='emma', email='emma@abv.bg')
    # new_user5 = User(username='david', email='david@abv.bg')
    # session.add_all([new_user, new_user5, new_user4, new_user3, new_user2])
    # session.commit()

    # session.add_all([Order(user_id=7), Order(user_id=9)])
    # session.commit()

    # orders = session.query(Order).order_by(Order.user_id.desc()).all()
    # if orders:
    #     for ord in orders:
    #         user = ord.user
    #         print(f'Order number {ord.id}, Is completed: {ord.is_completed}, Username: {user.username}')
    #     else:
    #         print('No orders yet.')

# session = Session()
# try:
#     session.begin()
#     session.query(User).delete()
#     session.commit()
#     print("All users deleted successfully")
# except Exception as e:
#     session.rollback()
#     print(f'An error occurred: {str(e)}')
# finally:
#     session.close()
