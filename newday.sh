mkdir $1
touch $1/$1.py
touch $1/test_input
touch $1/input
touch $1/challenge.md
cd $1
echo "\"\"\"" > $1.py
echo "Preocts <preocts@preocts.com>" >> $1.py
echo "Preocts#8196" >> $1.py
echo "AOC Day ${1}" >> $1.py
echo "\"\"\"" >> $1.py
clear
echo "Plan. Implement. Execute."
