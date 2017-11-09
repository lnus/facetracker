echo "Adds the necessary repos"
sudo add-apt-repository universe
sudo apt-get update

echo "Installing necessary stuff via apt-get..."
sudo apt-get install -y libboost-all-dev cmake python3 python3-pip

echo "Installing face_recognition and opencv via pip3"
sudo -H pip3 install face_recognition
pip3 install opencv-python
