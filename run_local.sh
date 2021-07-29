set -e

CURRENT_DIR=$(pwd)

case "$1" in

    "python")
        cd src/python
        python3 app.py ${CURRENT_DIR}/events/UserPresenceChange.json
        ;;

    "node")
        cd src/typescript
        ts-node src/app.ts ${CURRENT_DIR}/events/UserPresenceChange.json
        ;;

    *)
        printf "Usage: %s python|node\n" $0
        exit 1
        ;;
esac
