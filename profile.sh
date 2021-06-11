#!/usr/bin/env bash

declare -a intervals_smallint=($(python -c 'print(f"[-10,50] [60,0] [3,100] [1000,100000]")'))
declare -a intervals_bigint=($(python -c 'print(f"[{-10**100},{-10**50}] [{-10**60},0] [3,{10**100}] [{10**1000},{10**100000}]")'))

printf "Timing small ints"
for i in {1..5}; do
   time python merge.py ${intervals_smallint[@]}
done

printf "\nProfiling small ints' memory footprint"
# Add profile decorator to get per-function timings in output
sed -i '' -e '/^def.*/i\
@profile' merge.py
mprof run merge.py ${intervals_smallint[@]} > /dev/null
mprof plot -o mprofile_smallint.png --backend agg  > /dev/null
printf "\nProfiling results written to mprofile_smallint.png"
# Remove profile decorator as Python would complain otherwise
sed -i '' -e '/^@profile$/d' merge.py

printf "\n\nTiming big ints"
for i in {1..5}; do
   time python merge.py ${intervals_bigint[@]}
done

printf "\nProfiling big ints' memory footprint"
# Add profile decorator to get per-function timings in output
sed -i '' -e '/^def.*/i\
@profile' merge.py
mprof run merge.py ${intervals_bigint[@]} > /dev/null
mprof plot -o mprofile_bigint.png --backend agg  > /dev/null
printf "\nProfiling results written to mprofile_bigint.png"
# Remove profile decorator as Python would complain otherwise
sed -i '' -e '/^@profile$/d' merge.py

rm mprofile_*.dat
