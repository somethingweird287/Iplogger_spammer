# Iplogger_spammer

Spams ip logging url with from random locations with tor.
This is my first github repo. Please forgive and report any mistakes made.

# Setup

## 1. Install tor

### Debian users

```
sudo apt-get install tor
```

### Arch Users

```
sudo pacman -S tor
```

### Fedora Users

```
dnf install tor
```

## 2.Generate the hashed Password

```
tor --hash-password <your_password_here>
```

Copy the hashed password.

## Configure torrc

Edit file `/etc/tor/torrc` or `/usr/local/etc/tor/torrc`

```
ControlPort 9051
HashedControlPassword <your hashed password here>
CookieAuthentication 0

```

Change the following.

## Restart tor

```
sudo systemctl restart tor
```

## Install dependency

```
pip install stem
```

## Change the `target_url` to desired ip logger link in `iplogger_spammer.py`.

## Run the file

```
python3 iplogger_spammer.py
```
