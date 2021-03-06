consts = {
        "timeout": 30,
        "emoji_numbers": ["\u0030\u20E3","\u0031\u20E3","\u0032\u20E3","\u0033\u20E3","\u0034\u20E3","\u0035\u20E3", "\u0036\u20E3","\u0037\u20E3","\u0038\u20E3","\u0039\u20E3"],
        
        "reaction_dict": {
            0 : {
                "⏮️": "backward",
                "⏹️": "stop",
                "⏭️": "forward"
            },
            1 : {
                "🆗": "forward"
            },
            5: {
                "🆗": "stop"
            }
        },
        "on_error": {
            "BadArgument": ["{user}, use {help}!"],
            "Default": ["{user}, Something went wrong... I couldn't catch the error, it was too fast lol.", "You might want to report this bug, {user}. Join the main discord and submit a bug report!"],
            "BotMissingPermissions": ["Bot has no permissions!", "No permissions for me, give me em."],
            "CommandOnCooldown": ["{user}, you are on cooldown! Try again in **{seconds}**!", "You got **{seconds}** remaining! Don't rush, {user}.", "{user}, You got about **{seconds}** left. Try again then."]
        },
        "embed_dict": {
            0 : "Menu Module"

        }
    }

        
