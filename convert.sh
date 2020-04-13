FILES=$(find . -type f -name '*.*')
for f in $FILES
do
    if test -f $f; then
        CHARSET="$( file -bi "$f"|awk -F "=" '{print $2}')"
        if [ "$CHARSET" != utf-8 ]; then
            echo -e "\nConverting $f from $CHARSET to utf-8"
            # iconv -f "$CHARSET" -t utf-8 "$f" -o "$f.temp"
            iconv -f GBK -t UTF-8 "$f" > "$f.temp"
            mv -f "$f.temp" $f
        fi
    else
        echo -e "\nSkipping $f - it's a regular file";
    fi
done