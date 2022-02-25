#!/bin/bash

IFS=$'\n' read -ra ADDR -d $'\0' <<< "$PAYLOAD"

for LINE in "${ADDR[@]}"
do
    if [[ "$LINE" =~ ^(PREVIOUS_REF=).* ]]; then
        PREVIOUS_REF=${LINE##*=}
    fi
    if [[ "$LINE" =~ ^(CURRENT_REF=).* ]]; then
        CURRENT_REF=${LINE##*=}
    fi
done

echo "::set-output name=previous_ref::$PREVIOUS_REF"
echo "::set-output name=current_ref::$CURRENT_REF"

echo -e "previous_ref: $PREVIOUS_REF"
echo -e "current_ref: $CURRENT_REF"

