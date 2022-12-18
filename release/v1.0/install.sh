chown root rgb_anims.service
chown -R root scripts
chown root main.py
cp rgb_anims.service /etc/systemd/system
mkdir /etc/rgb_anims/
cp main.py /etc/rgb_anims/
cp -r scripts /etc/rgb_anims/
systemctl enable rgb_anims.service
