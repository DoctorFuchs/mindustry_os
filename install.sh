cd ~/mindustry_os

sudo apt install git default-jdk python3 python3-pip -y 
python3 -m pip install requests httpie

echo "git pull https://github.com/DoctorFuchs/mindustry_os.git" >> ~/.bashrc
echo "python3 ~/mindustry_os/loader.py" >> ~/.bashrc
