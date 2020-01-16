Instructions:

This is a very simple rest API built for the AI Dungeon 2 code

Instructions to be provided to the clients are via /api/pending_client_actions
Instructions to be sent to AI for determining responses are via /api/pending_server_actions

This could probably be replaced with a message queue system

This API is built to work with the "Ultimate Bot API For Discord" (UBAD) https://github.com/trippedoutfish/ubad

use "flask run" to start, configure UBAD to point at flask instance, enjoy.

Manual tweaking required if not using CUDA GPUs.

Remove / (modify to PCI = 0 if only 1 GPU) lines 15 & 16 for CPU support, as well as using tensorflow instead of tensorflow-gpu package in requirements.txt


Credit for initial code & model goes to the AI Dungeon project. 

"Infinite adventures await! http://www.aidungeon.io/"
