#!/bin/bash

__create_user() {
# Create a user to SSH into as.
useradd user
SSH_USERPASS=password
echo -e "$SSH_USERPASS\n$SSH_USERPASS" | (passwd --stdin user)
echo -e "$SSH_USERPASS\n$SSH_USERPASS" | (passwd --stdin root)
echo ssh user password: $SSH_USERPASS
echo ssh root password: $SSH_USERPASS
}

# Call all functions
__create_user