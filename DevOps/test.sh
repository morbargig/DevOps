check = docker run -it --rm alpine:test | grep -c 200
if [ $check -eq 0 ]; then

        echo "test faild"
else
        echo "test sucsess"
fi
#
