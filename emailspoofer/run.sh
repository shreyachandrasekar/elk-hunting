# Usage: ./run.sh email_list.txt email_list2.txt

#shift

# Startup SMTP server on port 25
#sudo postfix start
#java -cp ".:lib/*" SpoofEmail $@
java -cp ".:lib/*" SpoofEmail $@
