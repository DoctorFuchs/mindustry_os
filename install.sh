sudo apt update
sudo apt install git default-jdk python3 python3-pip -y 
python3 -m pip install requests httpie

echo "cd ~/mindustry_os" >> ~/.bashrc
echo "git pull https://github.com/DoctorFuchs/mindustry_os.git" >> ~/.bashrc
echo "sudo python3 ~/mindustry_os/loader.py" >> ~/.bashrc
