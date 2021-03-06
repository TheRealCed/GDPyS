# GDPyS
GDPyS is a Python based Geometry Dash server, which can be used for making Private Servers.

# What works?
GDPyS is still in **very** early development. This means that most things aren't completed and some things may not work as intended. So here is what is currently done:
- Registering
- Logging in
- Loading user data
- Updating user data
- Loading account comments
- Creating account comments
- Updating account settings
- Leaderboards (only top and creators)
- Saving user data
- Loading user data
- Likes
- Level searching (most filters done)
- Online level download
- Custom songs
- Comment posting
- Comment viewing
- Rating levels
- Permissions
- Sending messages
- Searching users

# Why GDPyS?
GDPyS is made with convenience and performance in mind. It provides performance benefits over existing alternatives while convenient features (such as error logs for easier debugging and automatic cron). Additionally, it is designed to be directly swappable with Cvolton's GMDPrivateServer, meaning you will able to reuse your existing database, save and level files.

# Cheatless

Cheatless is the GDPyS AntiCheat! It performs various tasks such as score analysis to keep obvious cheaters off your server. It is currently in heavy development but once finished, it will provide protection against cheaters. Each part of it can be enabled and disabled at will via the GDPyS config.

# Requirements
The requirements for GDPyS are different to existing alternatives. They include:
- Anything that can run Python such as a Linux VPS (required to run Python apps, any free hosting won't do)
- Python 3.5+ (tested with 3.6.9 and 3.7.5)
- Nginx/Apache (required to proxypass)
- MySQL Server
- Roughly 17 character domain such as devvgdpys.ussr.pl (more or less, few tweaks when editing the exe and routes could allow for more or less)

Read [the wiki](https://github.com/RealistikDash/GDPyS/wiki/How-to-set-up-GDPyS) for more information.

# Credits
- Some of this code is a direct port of [Cvolton's GMDPrivate Server](https://github.com/Cvolton/GMDprivateServer) into Python. Furthermore, his database structure has been used as a base.

# License
GDPyS is licensed under the [GNU General Public License v3.0](https://github.com/RealistikDash/GDPyS/blob/master/LICENSE)
