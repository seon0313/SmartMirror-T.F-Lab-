import dbus

def is_media_playing():
    bus = dbus.SessionBus()
    for service in bus.list_names():
        if service.startswith('org.mpris.MediaPlayer2.'):
            player = dbus.SessionBus().get_object(service, '/org/mpris/MediaPlayer2')
            status = player.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
            if status == 'Playing':
                return True
    return False

if is_media_playing():
    print("Media is playing")
else:
    print("Media is not playing")