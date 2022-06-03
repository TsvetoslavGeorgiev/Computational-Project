for i in `seq 0 19` ;
do
  echo $i
  screen -S p$i p4 analyseHet.py -- $i
done
