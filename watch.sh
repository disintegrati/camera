#!/bin/bash
inotifywait -m /home/nuc/Scrivania/camera/video -e create -e moved_to |
    while read path action file; do
        echo "The file '$file' appeared in directory '$path' via '$action'"
        # do something with the file
        sleep 15
        curl -i -X POST -F "url=@/home/nuc/Scrivania/camera/video/$file" -F "caption=video_upload" -F "published=true" -F "access_token=EAASJMHw5q08BAJRRXZA1GkMQIPtkpWLIRdvcOZBvX9q56gkG2orsWUNkfEw87fD0o6Wt1Hk6JsofJYJmZBO3WbX2QCSxs8U9KD0SQwleCcJuGIFcy7tXbpLnqV5VmZC4e6hNFrAOZA5NjvyNEGnTQblwciWBUL0ZBR0ocxsqPzhWfqtGIRpntd" "https://graph.facebook.com/v2.10/1736575526639458/videos"
    done
