from flask import Blueprint, current_app
from flask_security import hash_password

commands = Blueprint("commands", __name__)


@commands.cli.command("init_users")
def init_users():
    """Initialize Users and Roles"""

    if current_app.testing:
        return

    with current_app.app_context():
        print("Initialize Users and Roles")
        # security = current_app.security
        security = current_app.extensions.get("security")
        # security.datastore.db.create_all()
        security.datastore.find_or_create_role(
            name="admin",
            permissions={"admin-read", "admin-write", "user-read", "user-write"},
            description="Admin user",
        )
        security.datastore.find_or_create_role(
            name="staff",
            permissions={"staff-read", "staff-read"},
            description="Staff user",
        )
        security.datastore.find_or_create_role(
            name="user", permissions={"user-read", "user-write"}, description="User"
        )

        if not security.datastore.find_user(email="admin@me.com"):
            security.datastore.create_user(
                email="admin@me.com",
                password=hash_password("password"),
                roles=["admin"],
            )
        if not security.datastore.find_user(email="staff1@me.com"):
            security.datastore.create_user(
                email="staff1@me.com",
                password=hash_password("password"),
                roles=["staff"],
            )

        security.datastore.db.session.commit()
