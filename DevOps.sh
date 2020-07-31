## aws ssh - 
## ssh -i ~/Downloads/green-team.pem ec2-user@green.develeap.com


## copy files from host to aws -
## scp -i ~/Downloads/green-team.pem /home/shaked/Downloads/Dockerfile_jenkins ec2-user@green.develeap.com:~/


## docker run -it --rm alpine:test3 sh |awk '{print $2}' to get the output (echo "result" at the end)

## check=`docker run -it --rm alpine:test | grep -c 200`
## if [ $check -eq 200 ] ; then
##        echo "test succeeded"
## else
##        echo "test failed with exit: $check"
## fi
