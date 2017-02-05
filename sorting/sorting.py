duplicity  --no-encryption --volsize=1024 --include=/home/magistr/zgate  --exclude=/** / file:///backup-duplicity


архивация полная:
sudo duplicity full --no-encryption --no-compression /media/flash/ file:///media/DATA/backup/flash072016

разархивация:
sudo duplicity restore --no-encryption --no-compression  file:///restore/ /home/magistr/backup2