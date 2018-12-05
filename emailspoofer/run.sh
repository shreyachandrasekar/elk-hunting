# Usage: ./run.sh email_list.txt email_list2.txt

#shift

# Startup SOCKS5 proxy to tor on port 9050
#java -cp ".:lib/*" SpoofEmail $@
java -cp ".:lib/*" SpoofEmail $@
