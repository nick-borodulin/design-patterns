"""
LSP or Liskov Substitution Principle states that if a program is using a parent class from a class
hierarchy, then substituting the parent with child should not alter the meaning or intent of the program.
I.e. the parent and the child should do roughly the same thing.

Analogy:  lamp socket is designed to accept a standard light bulb. LSP says that if you have different types 
of light bulbs (an incandescent bulb, an LED bulb, a CFL bulb) that all fit the same socket,
you should be able to swap one for the other, and the lamp should still work as expected (turn on and provide light), 
even though how they produce light is different. 
You wouldn't expect putting an LED bulb in to suddenly make the lamp start playing music!


LSP violation example:

class User:
    def send_message(self, message_content):
        print(f"Sending message to user: {message_content}")
        # Assume this involves looking up contact info and sending
        # In a real system, this would interact with email/SMS services
        pass

class GuestUser(User):
    def send_message(self, message_content):
        # This subclass changes the expected behavior dramatically!
        # It violates the assumption that send_message actually SENDS a message.
        print("Attempted to send message to Guest User. Operation not supported.")
        # Maybe it logs an error, or worse, does nothing silently.
        # It definitely doesn't 'send' in the same way a regular User does.
        # It might even raise an error unexpectedly in a real scenario.
        raise NotImplementedError("Guest users cannot receive messages")


# Code that uses the User base type
def send_welcome_message(user: User):
    print(f"Preparing welcome message for {type(user).__name__}...")
    user.send_message("Welcome to our service!")
    print("Welcome message process initiated.")

GuestUser violates the base User contract by not sending the message.

LSP-compliant version is below.
"""

# Possible LSP Compliant Approach (Option 2)


class UserLSP:
    def can_receive_message(self) -> bool:
        """Returns True if the user can receive messages."""
        return True  # Default behavior for most users

    def send_message(self, message_content):
        """Sends a message IF the user can receive it."""
        if self.can_receive_message():
            print(f"Sending message to user: {message_content}")
            # ... sending logic ...
        else:
            print(f"User {type(self).__name__} cannot receive messages. Skipping.")


class GuestUserLSP(UserLSP):
    def can_receive_message(self) -> bool:
        """Guest users cannot receive messages."""
        return False  # Changes behavior, but fulfills the contract

    # We don't need to override send_message if the base handles the check


# Code that uses the UserLSP base type
def send_welcome_message_lsp(user: UserLSP):
    """Sends a standard welcome message if the User object can receive it."""
    print(f"Preparing welcome message for {type(user).__name__}...")
    # Now the caller relies on the base class's check
    user.send_message("Welcome to our service!")
    print("Welcome message process finished.")
